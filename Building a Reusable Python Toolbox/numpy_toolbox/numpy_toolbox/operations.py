# numpy_toolbox/numpy_toolbox/operations.py

"""
operations
==========

This module provides various numerical operations using NumPy, including array statistics, matrix multiplication, and random matrix generation.

Functions:
----------
- array_statistics(arr): Calculate statistics (mean, median, std_dev) of a NumPy array.
- matrix_multiplication(matrix1, matrix2): Perform matrix multiplication using NumPy.
- create_random_matrix(rows, cols): Create a random matrix with specified dimensions.
"""


import numpy as np

def array_statistics(arr):
    """
    Calculate statistics of a NumPy array.

    Args:
        arr (np.ndarray): Input array.

    Returns:
        dict: A dictionary with mean, median, and standard deviation of the array.
    """
    return {
        'mean': np.mean(arr),
        'median': np.median(arr),
        'std_dev': np.std(arr)
    }

def matrix_multiplication(matrix1, matrix2):
    """
    Perform matrix multiplication using NumPy.

    Args:
        matrix1 (np.ndarray): First matrix.
        matrix2 (np.ndarray): Second matrix.

    Returns:
        np.ndarray: Result of the matrix multiplication.
    """
    return np.dot(matrix1, matrix2)

def create_random_matrix(rows, cols):
    """
    Create a random matrix with specified dimensions.

    Args:
        rows (int): Number of rows.
        cols (int): Number of columns.

    Returns:
        np.ndarray: Random matrix with values between 0 and 1.
    """
    return np.random.rand(rows, cols)
