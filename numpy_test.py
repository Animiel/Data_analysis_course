# to install NumPy
##################
# py -m pip install numpy
##################

import numpy as np

# creates an array with only numbers that can be written with 8 bits (sparing memory, not necessary for beginners, but when manipulating huge amount of data)
test_list = np.array([1, 2, 3], dtype=np.int8)
print(test_list)

# getting the type
print(test_list.dtype)

# default type is 64 bits
other_list = np.array([1, 2, 3, 4])
print(other_list.dtype)