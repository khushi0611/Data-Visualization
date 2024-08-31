# 1.Convert the below list into numpy array then display the array
# input: my_list = [1,2,3,4,5]
# Output: Numpy array: [1 2 3 4 5]

import numpy as np
my_list=[1,2,3,4,5]
print('my_list = ',my_list)
numpy_array=np.array(my_list)
print('Numpy array: ',numpy_array)


# 2.Convert the below list into a numpy array then display the array then display the first and last index and
# then multiply each element by 2 and display the result

# input: my_list = [1,2,3,4,5]
# Output: 
# First element: 1
# Last element: 5
# Array after doubling each element:
# [2 4 6 8 10] 

import numpy as np
my_list=[1,2,3,4,5]
print('my_list = ',my_list)

numpy_array=np.array(my_list)
print('First element: ',numpy_array[0])
print('last element: ',numpy_array[len(numpy_array)-1])
print('Array after doubling each element: ',numpy_array*2)


# Working with Numpy using Jupyter 

# 1.Write a NumPy program to create an array of 10 zeros, 10 ones, and 10 fives
# Sample Output
# An array of 10 zeros
#     [0 0 0 0 0 0 0 0 0 0]
# An array of 10 ones 
#     [1 1 1 1 1 1 1 1 1 1] 
# An array of 10 fives
#     [5 5 5 5 5 5 5 5 5 5]
import numpy as np
arr=np.zeros((10),dtype=np.int_)
print('An array of 10 zeros\n',arr)
arr=np.ones((10),dtype=np.int_)
print('An array of 10 ones\n',arr)
arr=np.ones((10),dtype=np.int_)*5
print('An array of 10 fives\n',arr)



# 2.Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10. 
import numpy as np
matrix = np.arange(2, 11).reshape(3, 3)

print("3x3 matrix with values ranging from 2 to 10:")
print(matrix)