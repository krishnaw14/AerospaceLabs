import os 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from linear_interpolate import linear_interpolate, k_value_linear_interpolate

import warnings
warnings.filterwarnings("ignore")

data_path = "Flat Plate/"
calculated_data_path = "Calculated Data/"

visc = 1.832e-5
rho = 1.189
nu = visc/rho

x = [11.7, 17, 22.3, 27.6,32.9, 38.3, 43.6, 48.9 ]

i = 0

if not os.path.exists(calculated_data_path):
	os.mkdir(calculated_data_path)

base_profile = pd.read_csv(calculated_data_path + "station4.csv")
base_k_values = base_profile["Kb"]
base_eta_values = base_profile["eta"]

for data_file_name in sorted(os.listdir(data_path)):
	print(data_file_name)
	data = pd.read_csv(data_path + data_file_name)

	P = data["P"]
	y = data["y"]
	y = data["y"] - data["y"][0] +0.02
	data["y (cm) - actual"] = pd.Series(y.astype(float).round(3), index=data.index)


	U = (2*P/(rho))**0.5

	data["U (m/s)"] = pd.Series(U.astype(float).round(3), index=data.index)

	Uinf = data.loc[data["U (m/s)"].idxmax()]["U (m/s)"]

	Uratio = U/Uinf

	data["U/Uinf"] = pd.Series(Uratio.astype(float).round(3), index=data.index)

	eta_values = 0.01*y*((Uinf/(nu*x[i]*0.01))**0.5)

	data["eta"] = pd.Series(eta_values.astype(float).round(3), index=data.index)

	Ub_values = []

	for eta in data["eta"]:
		Ub = linear_interpolate(eta)
		Ub_values.append(Ub)

	Ub_values = np.array(Ub_values)

	data["Ubratio"] = pd.Series(Ub_values.astype(float).round(5), index=data.index)

	Kb_values = data["Ubratio"]/data["U/Uinf"]

	data["Kb"] = pd.Series(Kb_values.astype(float).round(5), index=data.index)

	i += 1

	interpolated_k_values = []
	for eta in data["eta"]:
		interpolated_k = k_value_linear_interpolate(base_k_values, base_eta_values, eta)
		interpolated_k_values.append(interpolated_k)

	interpolated_k_values = np.array(interpolated_k_values)

	data["Interpolated K Values"] = pd.Series(interpolated_k_values.astype(float).round(5), index=data.index)

	plt.scatter(data["U/Uinf"]*interpolated_k_values, data["eta"], s = 5, cmap = "summer")

	data.to_csv(calculated_data_path + data_file_name)

legend = []
for i in range(1,9):
	legend.append(str(i))

eta_values = []

for i in range(17):
	eta_values.append(i*0.5)

Uratio_values = [
	0, 0.1659, 0.3298, 0.4868, 0.6298, 0.7513, 0.8460, 0.9130, 0.9555, 0.9795,
	0.9915, 0.9969, 0.9990, 0.9997, 0.9999, 1, 1]

plt.plot(Uratio_values, eta_values)
legend.append("Blacius")
# plt.legend(legend)
plt.show()
