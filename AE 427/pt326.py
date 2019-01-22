import numpy as np 
import pandas as pd 
import os
import matplotlib.pyplot as plt

data_path = "all/"

legend_names = []
plots = []

folder_type_dictionary = {
	"ALL0000" : "20% Throttle: Near The Fan",
	"ALL0001" : "20% Throttle: Middle",
	"ALL0002" : "20% Throttle: Near The Exit",
	"ALL0003" : "40% Throttle: Near The Fan",
	"ALL0004" : "40% Throttle: Middle",
	"ALL0005" : "40% Throttle: Near The Exit",
	"ALL0006" : "80% Throttle: Near The Fan",
	"ALL0007" : "80% Throttle: Middle",
	"ALL0008" : "80% Throttle: Near The Exit",
	"ALL0009" : "100% Throttle: Near The Fan",
	"ALL0010" : "100% Throttle: Middle",
	"ALL0011" : "100% Throttle: Near The Exit"
}
start_time_dictionary = {
	"ALL0000" : 2.812,
	"ALL0001" : 2.252,
	"ALL0002" : 2.02,
	"ALL0003" : 4.664,
	"ALL0004" : 4.84,
	"ALL0005" : 4.776,
	"ALL0006" : 0.876,
	"ALL0007" : 1.464,
	"ALL0008" : 2.692,
	"ALL0009" : 3.756,
	"ALL0010" : 2.564,
	"ALL0011" : 0.932
}
end_time_dictionary = {
	"ALL0000" : 6.984,
	"ALL0001" : 6.92,
	"ALL0002" : 7.06,
	"ALL0003" : 8.112,
	"ALL0004" : 8.9,
	"ALL0005" : 8.81,
	"ALL0006" : 3.95,
	"ALL0007" : 5.44,
	"ALL0008" : 6.32,
	"ALL0009" : 8.59,
	"ALL0010" : 6.62,
	"ALL0011" : 4.744 
}

for folder_name in os.listdir(data_path):

	print("-------------", folder_name, "-------------" )

	required_names = ["ALL0002", "ALL0005", "ALL0008", "ALL0011"]

	if folder_name not in required_names:
		continue



	data_folder = data_path + folder_name + "/"

	if data_folder == 'all/.DS_Store/':
		continue

	for file_name in os.listdir(data_folder):
		# print(file_name)
		if file_name.endswith("2.CSV"):
			input_channel_data_path = data_folder + file_name
		elif file_name.endswith("1.CSV"):
			output_channel_data_path = data_folder + file_name


	input_channel_data = pd.read_csv(input_channel_data_path)
	input_channel_time = input_channel_data.iloc[:, 3]
	input_channel_volt = input_channel_data.iloc[:, 4]

	output_channel_data = pd.read_csv(output_channel_data_path)
	output_channel_time = output_channel_data.iloc[:, 3]
	output_channel_volt = output_channel_data.iloc[:, 4]

	terminal_times = []
	# delta_input_volt = 0
	terminal_times.append(start_time_dictionary[folder_name])
	terminal_times.append(end_time_dictionary[folder_name])

	# for i in range(len(input_channel_data)-1):

	# 	if len(terminal_times) == 2:
	# 		break

	# 	if abs(input_channel_volt[i+1] - input_channel_volt[i]) >= 2:
	# 		terminal_times.append(input_channel_time[i+1])
	# 		# print(i," ", input_channel_volt[i], " ", input_channel_volt[i+1], " ", input_channel_time[i+1])
	# 		delta_input_volt = abs(input_channel_volt[i+1] - input_channel_volt[i])


	# initial_output = output_channel_volt[list(output_channel_time).index(terminal_times[0])]
	# steady_index_time =  (terminal_times[0] + terminal_times[1])*0.5
	# steady_state_output = output_channel_volt[np.argmin(abs(output_channel_time - steady_index_time))]

	print("Start Time: ", terminal_times[0])
	print("End Time:", terminal_times[1])

	output_time_start = np.argmin(abs(output_channel_time - terminal_times[0]))
	output_time_end = np.argmin(abs(output_channel_time - terminal_times[1]))

	volt_plot_values = output_channel_volt[output_time_start: output_time_end]
	# time_plot_values = output_channel_time[output_time_start:output_time_end]
	time_plot_values = np.arange(len(volt_plot_values))

	plt.plot(time_plot_values, volt_plot_values)
	legend_names.append(folder_type_dictionary[folder_name])
	plots.append(volt_plot_values)
	# plt.show()


	# print("Start Index:", list(output_channel_time).index(terminal_times[0]))
	# print("Steady Index: ", np.argmin(abs(output_channel_time - steady_index_time)))
	# print("Initial Output: ", initial_output)
	# print("Steady_state_output:", steady_state_output)
	# print("Delta Input Volt: ", delta_input_volt)

	# gain = abs(steady_state_output - initial_output)/delta_input_volt
	# print("Gain: ", gain)

# print("Flag", len(plots))
# for plot in plots:
# 	plt.plot(plot)
plt.title("Air Temperature (V) vs. Time (s)")
plt.xlabel("Time (s)")
plt.ylabel("Air Temperature (V)")
plt.legend(legend_names)
plt.savefig("exp3-graphs/near_to_exit.png")
plt.show()




