import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import os 

data_path = "2DJet/"
corrected_data_path = "corrected_2DJet/"
legends = []

if not os.path.exists(corrected_data_path):
	os.mkdir(corrected_data_path)

station_distance_map = {
	1:0,
	2:4.5,
	3:8.5,
	4:11.5,
	5:16,
	6:19,
	7:22
}

for data_file_name in sorted(os.listdir(data_path)):

	data = pd.read_csv(data_path + data_file_name)

	if data_file_name == "Sheet 1-Station 1.csv":
		continue

	print(list(data))

	U_values = data["U (m/s)"]
	U_max = data.loc[data["U (m/s)"].idxmax()]["U (m/s)"]

	U_values = abs(U_values - U_max/2)
	# print(min(list(U_values)))
	b_index = np.argmin(U_values)
	b = abs(data["y (mm)"][b_index])
	normalized_y = data["y (mm)"]/b

	del data['y/b']
	data['y/y_0.5'] = pd.Series(normalized_y.astype(float).round(3), index=data.index)


	plt.scatter(normalized_y, data["U/Um"], s = 8)

	data["U/Um"] = data["U/Um"].astype(float).round(3)
	# data.round({"U/Um": 3, "y/y_0.5": 3})
	data.to_csv(corrected_data_path + data_file_name)

	for i in range(2,8):
		if "Station " + str(i) in data_file_name:
			legend = "x/d = " + str(station_distance_map[i])
			legends.append(legend)
			break

plt.legend(legends)
plt.xlabel("y/y_0.5")
plt.ylabel("U/Um")
plt.title("Nomalized Curve")
plt.savefig("normalized_plot.png")
plt.show()
