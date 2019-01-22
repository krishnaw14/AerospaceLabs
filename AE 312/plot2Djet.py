import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import os 

data_path = "2DJet/"
legends = []

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


	plt.scatter(data["y/b"], data["U/Um"], s = 8)

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
