import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import os 

data_path = "2DJet/"
legends = []

# if not os.path.exists(corrected_data_path):
# 	os.mkdir(corrected_data_path)

station_distance_map = {
	1:0,
	2:4.5,
	3:8.5,
	4:11.5,
	5:16,
	6:19,
	7:22
}
x_values = [4.5, 8.5, 11.5, 16, 19, 22]
b_values = []

for data_file_name in sorted(os.listdir(data_path)):

	data = pd.read_csv(data_path + data_file_name)

	if data_file_name in ["Sheet 1-Station 1.csv"] :
		continue

	print(list(data))

	U_values = data["U (m/s)"]
	U_max = data.loc[data["U (m/s)"].idxmax()]["U (m/s)"]

	U_values = abs(U_values - U_max/2)

	b_index = np.argmin(U_values)
	b = abs(data["y (mm)"][b_index])
	normalized_y = data["y (mm)"]/b

	del data['y/b']
	data['y/y_0.5'] = pd.Series(normalized_y.astype(float).round(3), index=data.index)


	# plt.scatter(normalized_y, data["U/Um"], s = 8)

	data["U/Um"] = data["U/Um"].astype(float).round(3)
	# data.round({"U/Um": 3, "y/y_0.5": 3})
	# data.to_csv(corrected_data_path + data_file_name)

	b_values.append(b/18)

	for i in range(1,8):
		if "Station " + str(i) in data_file_name:
			legend = "x/d = " + str(station_distance_map[i])
			legends.append(legend)
			break

# print(legends)
plt.plot(x_values, b_values, 'ro')
m,c = np.polyfit(x_values, b_values, 1)
r = np.linspace(0,25,100)
plt.plot(r, m*r + c)
plt.legend(["Actual Data Points", "Approximate Linear fit function"])
plt.xlabel("x/D")
plt.ylabel("b/D")
plt.xticks([])
plt.yticks([])
plt.title("Variation of jet half width with distance from the nozzle")
plt.savefig("Y.png")
plt.show()
