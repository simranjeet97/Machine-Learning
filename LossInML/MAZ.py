#MEAN Absolute Zero
"""Itis measured as the average of sum of absolute differences 
between predictions and actual observations. MAZ
needs more complicated tools such as linear programming to 
compute the gradients. Plus MAE is more robust to outliers 
since it does not make use of square."""

import numpy as np 

#Values are -
y_hat = np.array([0.000, 0.166, 0.333])
y_true = np.array([0.000, 0.254, 0.998])

def maz(predictions, targets):
	differences = predictions - targets
	absolute_differences = np.absolute(differences)
	mean_of_differences = absolute_differences.mean()
	return mean_of_differences

print("y_hat is :" +str(["%.8f"% elem for elem in y_hat]))
print("y_true is :" +str(["%.8f"% elem for elem in y_true]))

maz_val = maz(y_hat,y_true)

print("MAZ Error is : "+str(maz_val))