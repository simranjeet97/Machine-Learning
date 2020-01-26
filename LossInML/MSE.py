"""
Mean square error is measured as the average of squared 
difference between predictions and actual observations. 
It’s only concerned with the average magnitude of error 
irrespective of their direction.
"""
import numpy as np

#Values are -
y_hat = np.array([0.000, 0.166, 0.333])
y_true = np.array([0.000, 0.254, 0.998])

def rmse(predictions, targets):
	differences = predictions - targets
	differences_squared = differences ** 2
	mean_of_differences_squared = differences_squared.mean()
	rmse_val = np.sqrt(mean_of_differences_squared)
	return rmse_val

print("y_hat is :" +str(["%.8f"% elem for elem in y_hat]))
print("y_true is :" +str(["%.8f"% elem for elem in y_true]))

rmse_val = rmse(y_hat,y_true)

print("RMS Error is : "+str(rmse_val))