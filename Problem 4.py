#Problem 4: Using Numpy create random vector of size 15 having only Integers in the range 0 -20.
# Write a program to find the most frequent item/value in the vector list.

import numpy as np
a = np.random.randint(0, 20, 15) #creating random array integer(Min, Max, Size)
print(a)
print("Most frequent item in the list is", np.bincount(a).argmax()) #counting Most frequent number