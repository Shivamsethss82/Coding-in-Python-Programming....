# Using the Numpy Library
import numpy as np

array = np.array([1,2,3,4,5])
print(array)
print(type(array))


# Using the Array Library
import array

int_array = array.array('i', [2,1,2,4,5,5])
float_array = array.array('f', [1.0, 2.5, 3.7, 4.2])
char_array = array.array('u', ['a', 'b', 'c', 'd', 'e'])

print(type(float_array))