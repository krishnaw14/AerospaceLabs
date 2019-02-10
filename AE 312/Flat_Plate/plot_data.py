import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import os 

blasius_eta_values = []
for i in range(17):
	blasius_eta_values.append(i*0.5)

blasius_Uratio_values = [
	0, 0.1659, 0.3298, 0.4868, 0.6298, 0.7513, 0.8460, 0.9130, 0.9555, 0.9795,
	0.9915, 0.9969, 0.9990, 0.9997, 0.9999, 1, 1]

x = [11.7, 17, 22.3, 27.6,32.9, 38.3, 43.6, 48.9 ]
legend = []
for i in range(1,9):
	legend.append("station" + str(i) + ": x = " + str(x[i-1]))
legend.append("Blasius Profile")

# data_path_1 = "Calculated Data/"
data_path = "/Users/krishna/Desktop/Calculated Data/"
saved_plots_directory = "saved_plots/"

if not os.path.exists(saved_plots_directory):
	os.mkdir(saved_plots_directory)

i = 0
for data_file_name in sorted(os.listdir(data_path)):

	if data_file_name == ".DS_Store":
		continue

	print(data_file_name)

	data = pd.read_csv(data_path + data_file_name)

	# plt.figure(1)
	label = "x = " + str(x[i]) + "cm"
	plt.scatter(data["U/Uinf"]*data["Interpolated K Values"],  data["eta"], s = 5, label = label)
	i += 1
	# plt.savefig(saved_plots_directory + "Uratio.png")
	# plt.show()

	# plt.figure(2)
	# plt.scatter(data["U/Uinf"]*data["Interpolated K Values"], data["eta"], s = 5)
	# plt.plot(blasius_Uratio_values, blasius_eta_values)
	# plt.legend(legend)
	# plt.xlabel("K*u/U")
	# plt.ylabel("eta")
	# plt.title("$ eta $ variation with $K \\frac{u}{U}$ for different $x$ values")
	# plt.savefig(saved_plots_directory + "KUratio.png")
	# plt.show()
plt.plot(blasius_Uratio_values, blasius_eta_values, label = "Blasius Profile")
plt.legend()
plt.xlabel("$K \\frac{u}{U}$")
plt.ylabel("$\\eta$")
plt.title("$ \\eta $ variation with $\\frac{Ku}{U}$ for different $x$ values")
plt.show()
