import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 
import os 

def plot(x1, y1, x2, y2, legend, title, xlabel, ylabel, serial):

	plt.plot(x1, y1)
	plt.plot(x2, y2)
	plt.title(title)
	plt.legend(legend)
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)
	plt.savefig(save_graphs_directory + "fig" + str(serial) + ".png")
	plt.show()


data_path = "Impulse-Turbine/"
save_graphs_directory = "graphs/"

if not os.path.exists(save_graphs_directory):
	os.mkdir(save_graphs_directory)

df_dictionary = {}
legend_names = ["4 Nozzles Open", "2 Nozzles Open"]

for data_file_name in os.listdir(data_path):

	data = pd.read_csv(data_path + data_file_name)

	if "Calculated" not in data_file_name:
		if '4' in data_file_name:
			if "Inlet" in data_file_name:
				df_dictionary["Observed-4-Nozzle-Contant_P1"] = data
			else:
				df_dictionary["Observed-4-Nozzle-Contant_N"] = data

		elif '2' in data_file_name:
			if "Inlet" in data_file_name:
				df_dictionary["Observed-2-Nozzle-Contant_P1"] = data
			else:
				df_dictionary["Observed-2-Nozzle-Contant_N"] = data

		continue


	elif '4' in data_file_name:
		if "Inlet" in data_file_name:
			df_dictionary["Calculated-4-Nozzle-Contant_P1"] = data
		else:
			df_dictionary["Calculated-4-Nozzle-Contant_N"] = data

	elif '2' in data_file_name:
		if "Inlet" in data_file_name:
			df_dictionary["Calculated-2-Nozzle-Contant_P1"] = data
		else:
			df_dictionary["Calculated-2-Nozzle-Contant_N"] = data


# Actual Power vs Pressure Ratio
plot(
	df_dictionary["Calculated-4-Nozzle-Contant_N"]["Pressure Ratio (P1/P2)"], df_dictionary["Calculated-4-Nozzle-Contant_N"]["Actual Power (W)"],
	df_dictionary["Calculated-2-Nozzle-Contant_N"]["Pressure Ratio (P1/P2)"], df_dictionary["Calculated-2-Nozzle-Contant_N"]["Actual Power (W)"],
	legend_names, "Actual Power vs Pressure Ratio", 
	"Pressure Ratio", "Actual Power (W)", 1
	)

# Actual Power Vs. RPM
plot(
	df_dictionary["Observed-4-Nozzle-Contant_P1"]["N"], df_dictionary["Calculated-4-Nozzle-Contant_P1"]["Actual Power (W)"],
	df_dictionary["Observed-2-Nozzle-Contant_P1"]["N"], df_dictionary["Calculated-2-Nozzle-Contant_P1"]["Actual Power (W)"],
	legend_names, "Actual Power vs RPM", 
	"RPM", "Actual Power (W)", 2
	)

# Efficiency Vs, Pressure Ratio
plot(
	df_dictionary["Calculated-4-Nozzle-Contant_N"]["Pressure Ratio (P1/P2)"], df_dictionary["Calculated-4-Nozzle-Contant_N"]["Efficiency"],
	df_dictionary["Calculated-2-Nozzle-Contant_N"]["Pressure Ratio (P1/P2)"], df_dictionary["Calculated-2-Nozzle-Contant_N"]["Efficiency"],
	legend_names, "Efficiency Vs, Pressure Ratio", 
	"Pressure Ratio", "Efficiency", 3
	)

# Efficiency Vs. RPM
plot(
	df_dictionary["Observed-4-Nozzle-Contant_P1"]["N"], df_dictionary["Calculated-4-Nozzle-Contant_P1"]["Efficiency"],
	df_dictionary["Observed-2-Nozzle-Contant_P1"]["N"], df_dictionary["Calculated-2-Nozzle-Contant_P1"]["Efficiency"],
	legend_names, "Efficiency Vs, RPM", 
	"RPM", "Efficiency", 4
	)

# Specific Air Consumption Vs. Actual Power (at constant Pressure Ratio)
plot(
	df_dictionary["Calculated-4-Nozzle-Contant_P1"]["Actual Power (W)"], df_dictionary["Calculated-4-Nozzle-Contant_P1"]["SAC (kg/kW-hr)"],
	df_dictionary["Calculated-2-Nozzle-Contant_P1"]["Actual Power (W)"], df_dictionary["Calculated-2-Nozzle-Contant_P1"]["SAC (kg/kW-hr)"],
	legend_names, "Specific Air Consumption Vs, Actual Power (at constant Pressure Ratio)", 
	"Actual Power (W)", "Specific Air Consumption (kg/kW-hr)", 5
	)

# Specific Air Consumption Vs. Actual Power (at constant RPM)
plot(
	df_dictionary["Calculated-4-Nozzle-Contant_N"]["Actual Power (W)"], df_dictionary["Calculated-4-Nozzle-Contant_N"]["SAC (kg/kW-hr)"],
	df_dictionary["Calculated-2-Nozzle-Contant_N"]["Actual Power (W)"], df_dictionary["Calculated-2-Nozzle-Contant_N"]["SAC (kg/kW-hr)"],
	legend_names, "Specific Air Consumption Vs, Actual Power (at constant RPM)", 
	"Actual Power (W)", "Specific Air Consumption (kg/kW-hr)", 6
	)

# Torque Vs. Pressure Ratio
plot(
	df_dictionary["Calculated-4-Nozzle-Contant_N"]["Pressure Ratio (P1/P2)"], df_dictionary["Calculated-4-Nozzle-Contant_N"]["Torque (Nm)"],
	df_dictionary["Calculated-2-Nozzle-Contant_N"]["Pressure Ratio (P1/P2)"], df_dictionary["Calculated-2-Nozzle-Contant_N"]["Torque (Nm)"],
	legend_names, "Torque Vs. Pressure Ratio", 
	"Pressure Ratio", "Torque (N-m)", 7
	)
# Torque Vs. RPM
plot(
	df_dictionary["Observed-4-Nozzle-Contant_P1"]["N"], df_dictionary["Calculated-4-Nozzle-Contant_P1"]["Torque (Nm)"],
	df_dictionary["Observed-2-Nozzle-Contant_P1"]["N"], df_dictionary["Calculated-2-Nozzle-Contant_P1"]["Torque (Nm)"],
	legend_names, "Torque Vs. RPM", 
	"RPM", "Torque (N-m)", 8
	)


