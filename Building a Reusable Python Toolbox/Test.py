# example_usage.py
import numpy_toolbox
import numpy as np
# Create a random matrix
matrix1 = numpy_toolbox.operations.create_random_matrix(3, 2)
matrix2 = numpy_toolbox.operations.create_random_matrix(2, 4)

print("Matrix 1:")
print(matrix1)
print("\nMatrix 2:")
print(matrix2)

# Perform matrix multiplication
result_matrix = numpy_toolbox.matrix_multiplication(matrix1, matrix2)
print("\nResult of Matrix Multiplication:")
print(result_matrix)

# Calculate statistics of a NumPy array
array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
stats = numpy_toolbox.array_statistics(array)
print("\nArray Statistics:")
print(stats)

print(numpy_toolbox.help())

"""_Note_
Beacuse in __init__.py  array_statistics, matrix_multiplication, are imported 
so they can be used directly from numpy_toolbox. But create_random_matrix is not imported 
so it needs to be exracted from operations module
"""

