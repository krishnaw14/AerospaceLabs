import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 

def linear_interpolate(base_y_values, base_x_values, x):

	if x >= max(list(base_x_values)) or np.isnan(x) == True:
		return 1

	closest_x_index = np.argmin(abs(base_x_values - x))
	# print("!!!!!!!!!!!!!!", closest_x_index, x)
	closest_x = base_x_values[closest_x_index]

	if x>=closest_x or closest_x_index == 0:
		next_x_index = closest_x_index + 1

	elif x < closest_x or closest_x_index == (len(list(base_x_values)) - 1):
		next_x_index = closest_x_index - 1

	x_1 = closest_x
	x_2 = base_x_values[next_x_index]
	K_1 = base_y_values[closest_x_index]
	K_2 = base_y_values[next_x_index]

	slope = (K_2 - K_1)/(x_2 - x_1)

	K = slope*(x - x_1) + K_1

	return K

data = pd.read_csv("airfoil_data.csv")

lower_base_x_values = data["lower_x"]
lower_base_y_values = data["lower_y"]

upper_base_x_values = data["upper_x"]
upper_base_y_values = data["upper_y"]

lower_x_values = data["x_lower"]
lower_y_values = []

upper_x_values = data["x_upper"]
upper_y_values = []

for i in range(len(upper_x_values)):

	lower_x = lower_x_values[i]

	if np.isnan(lower_x):
		lower_y_values.append(-1)
		upper_y_values.append(-1)
		continue


	lower_y = linear_interpolate(lower_base_y_values, lower_base_x_values, lower_x)
	lower_y_values.append(lower_y)

	upper_x = upper_x_values[i]
	upper_y = linear_interpolate(upper_base_y_values, upper_base_x_values, upper_x)
	upper_y_values.append(upper_y)

	print(lower_x, upper_x)


# plt.plot(lower_x_values[0:len(lower_y_values)], lower_y_values)
# plt.plot(upper_x_values[0:len(upper_y_values)], upper_y_values)
# plt.show()
lower_y_values = np.array(lower_y_values)
upper_y_values = np.array(upper_y_values)

data["y_lower"] = pd.Series(lower_y_values.astype(float).round(6), index=data.index)
data["y_upper"] = pd.Series(upper_y_values.astype(float).round(6), index=data.index)
data.to_csv("with_y_values.csv")

plt.scatter(lower_base_x_values, lower_base_y_values, s = 10)
plt.scatter(upper_base_x_values, upper_base_y_values, s = 10)

plt.plot(lower_base_x_values, lower_base_y_values)
plt.plot(upper_base_x_values, upper_base_y_values)
plt.axis([0,1, -0.2, 0.3])
plt.title("Eppler E423 airfoil")
plt.xlabel("x/c")
plt.ylabel("y/c")
plt.show()


