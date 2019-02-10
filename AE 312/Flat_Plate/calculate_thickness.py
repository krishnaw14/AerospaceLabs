import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import os 

data_path = "/Users/krishna/Desktop/Calculated Data/"

visc = 1.832e-5
rho = 1.189
nu = 1.56e-5
x_values = [11.7, 17, 22.3, 27.6, 32.9, 38.3, 43.6, 48.9]

displacement_thickness_values = []
blasius_displacement_thickness_values = []
displacement_thickness_error_values = []

energy_thickness_values = []

momentum_thickness_values = []
blasius_momentum_thickness_values = []
momentum_thickness_error_values = []

shape_factor_values = []

i = 0

for data_file_name in sorted(os.listdir(data_path)):

	if data_file_name == ".DS_Store":
		continue

	data = pd.read_csv(data_path + data_file_name)

	Uratio = data["U/Uinf"]
	y_values = data["y (cm) - actual"]
	Uinf = data.loc[data["U (m/s)"].idxmax()]["U (m/s)"]
	n = len(data)
	b = y_values[n-1]
	a = y_values[0]
	h = 0.01*(b-a)/n


	displacement_thickness = 0
	momentum_thickness = 0
	energy_thickness = 0
	for U in Uratio:
		displacement_thickness += (1 - U)
		momentum_thickness += (U*(1 - U))
		energy_thickness += (U*(1 - U*U))

	displacement_thickness *=  (h)
	momentum_thickness *=  (h)
	energy_thickness *= (h)

	# displacement_thickness = (2 - Uratio[0] - Uratio[n-1])
	print(data_file_name)
	print("Experimetal Result:")
	print("Displacement Thickness: ", displacement_thickness)
	print("Momentum thickness: ", momentum_thickness)
	print("Energy thickness: ", energy_thickness)
	# print(10*energy_thickness)

	# print("\n")
	print("Blasius Solution:")

	x = x_values[i]*0.01
	i += 1
	blasius_displacement_thickness = 1.72 * np.sqrt(nu*x/Uinf)
	blasius_momentum_thickness = 0.65 * np.sqrt(nu*x/Uinf)
	# blasius_energy_thickness 

	print("Displacement Thickness: ",blasius_displacement_thickness)
	print("Momentum thickness: ", blasius_momentum_thickness)

	# print("\n")
	print("Error (percent):")
	displacement_thickness_error = 100*abs(displacement_thickness -blasius_displacement_thickness)/blasius_displacement_thickness
	momentum_thickness_error = 100*abs(blasius_momentum_thickness - momentum_thickness)/blasius_momentum_thickness
	print("Displacement Thickness: ", displacement_thickness_error)
	print("Momentum thickness: ", momentum_thickness_error)

	print("Shape Factor")
	shape_factor = displacement_thickness/momentum_thickness
	print(shape_factor)

	displacement_thickness_values.append(1000*displacement_thickness)
	blasius_displacement_thickness_values.append(1000*blasius_displacement_thickness)
	displacement_thickness_error_values.append(displacement_thickness_error)

	momentum_thickness_values.append(1000*momentum_thickness)
	blasius_momentum_thickness_values.append(1000*blasius_momentum_thickness)
	momentum_thickness_error_values.append(momentum_thickness_error)

	shape_factor_values.append(shape_factor)
	energy_thickness_values.append(1000*energy_thickness)

	print("\n\n\n")

output_file_name = "Thickness.csv"
dataframe = pd.DataFrame()
dataframe["x (cm)"] = pd.Series(np.array(x_values).astype(float).round(3))

dataframe["displacement_thickness (mm)"] = pd.Series(np.array(displacement_thickness_values).astype(float).round(3))
dataframe["blasius_displacement_thickness (mm)"] = pd.Series(np.array(blasius_displacement_thickness_values).astype(float).round(3))
dataframe["displacement_thickness_error (%)"] = pd.Series(np.array(displacement_thickness_error_values).astype(float).round(3))

dataframe["momentum_thickness (mm)"] = pd.Series(np.array(momentum_thickness_values).astype(float).round(3))
dataframe["blasius_momentum_thickness (mm)"] = pd.Series(np.array(blasius_momentum_thickness_values).astype(float).round(3))
dataframe["momentum_thickness_error (%)"] = pd.Series(np.array(momentum_thickness_error_values).astype(float).round(3))

dataframe["Energy Thickness (mm)"] = pd.Series(np.array(energy_thickness_values).astype(float).round(3))

dataframe["Shape Factor"] = pd.Series(np.array(shape_factor_values).astype(float).round(3))

dataframe.to_csv(data_path + output_file_name)
