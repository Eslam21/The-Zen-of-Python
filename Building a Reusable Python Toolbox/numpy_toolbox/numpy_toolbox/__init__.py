"""
numpy_toolbox
=============

`numpy_toolbox` is a Python package designed to simplify numerical operations using NumPy. It provides a collection of utility functions that facilitate array manipulations, mathematical computations, and random matrix generation.

Key Features:
-------------
- **Array Operations**: Functions to compute statistical properties of arrays, such as mean, median, and standard deviation.
- **Matrix Operations**: Tools for matrix multiplication and other linear algebra operations.
- **Random Matrix Generation**: Methods to create matrices with random values for testing and simulations.

Installation:
-------------
To install `numpy_toolbox`, use the following pip command:

    pip install numpy_toolbox

Usage:
------
Import the package and use its functions as demonstrated below:

```python
from numpy_toolbox import operations as ops
import numpy as np

# Example: Compute statistics of an array
arr = np.array([1, 2, 3, 4, 5])
stats = ops.array_statistics(arr)
print(stats)

# Example: Perform matrix multiplication
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])
result = ops.matrix_multiplication(matrix1, matrix2)
print(result)

# Example: Create a random matrix
random_matrix = ops.create_random_matrix(2, 3)
print(random_matrix)
"""


from .operations import( 
    array_statistics,
    matrix_multiplication)
from .helper import help

__all__=['array_statistics','matrix_multiplication','help']