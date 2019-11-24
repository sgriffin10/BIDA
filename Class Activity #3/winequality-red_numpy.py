
# Import numpy
import numpy as np
wines = np.genfromtxt("Class Activity #3/winequality-red.csv", delimiter=";", skip_header=1)

# Average Quality - Quality is in Column index 11 (12th column)
# print(np.average(wines[:, 11]))

# print(wines)
# print(wines.shape) #prints # of rows and cols
# print(wines[2,3])
# print(wines.dtype)
#
# # SLICING: Selectively choosing values  within the matrix

# # Single element

# print(wines[2,3])
#
# # All values  in a particular COLUMN (4th column)

# print(wines[:, 3])

# # All values in a particular ROW (4th row)

# print(wines[3, :])


