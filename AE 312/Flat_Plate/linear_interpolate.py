import numpy as np 
import matplotlib.pyplot as plt

def linear_interpolate(eta):

	if eta >= 7.5:
		return 1

	eta_values = []

	for i in range(17):
		eta_values.append(i*0.5)


	Uratio_values = [
	0, 0.1659, 0.3298, 0.4868, 0.6298, 0.7513, 0.8460, 0.9130, 0.9555, 0.9795,
	0.9915, 0.9969, 0.9990, 0.9997, 0.9999, 1, 1]

	eta_values = np.array(eta_values)
	Uratio_values = np.array(Uratio_values)

	closest_eta_index = np.argmin(abs(eta_values - eta))
	closest_eta = eta_values[closest_eta_index]

	if eta>closest_eta:
		next_eta_index = closest_eta_index+1
		eta_1 = eta_values[next_eta_index]
		eta_2 = eta_values[closest_eta_index]
		U_1 = Uratio_values[next_eta_index]
		U_2 = Uratio_values[closest_eta_index]

	else:
		next_eta_index = closest_eta_index-1
		eta_1 = eta_values[closest_eta_index]
		eta_2 = eta_values[next_eta_index]
		U_1 = Uratio_values[closest_eta_index]
		U_2 = Uratio_values[next_eta_index]

	# else:
	# 	Uratio = Uratio_values[closest_eta_index]

	slope = (U_1 - U_2)/(eta_1 - eta_2)

	U = slope*(eta - eta_1) + U_1

	return U

	# plt.plot(eta_values, Uratio_values)
	# plt.show()

def k_value_linear_interpolate(k_values, eta_values, eta):

	if eta >= max(list(eta_values)) or np.isnan(eta) == True:
		return 1

	closest_eta_index = np.argmin(abs(eta_values - eta))
	# print("!!!!!!!!!!!!!!", closest_eta_index, eta)
	closest_eta = eta_values[closest_eta_index]

	if eta>=closest_eta or closest_eta_index == 0:
		next_eta_index = closest_eta_index + 1

	elif eta < closest_eta or closest_eta_index == (len(list(eta_values)) - 1):
		next_eta_index = closest_eta_index - 1

	eta_1 = closest_eta
	eta_2 = eta_values[next_eta_index]
	K_1 = k_values[closest_eta_index]
	K_2 = k_values[next_eta_index]

	slope = (K_2 - K_1)/(eta_2 - eta_1)

	K = slope*(eta - eta_1) + K_1

	return K




