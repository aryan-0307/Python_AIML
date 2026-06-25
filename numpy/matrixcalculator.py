import numpy as np

x=np.array([[1,2],[3,4]])
y=np.array([[5,6],[7,8]])
print("Addition of matrices:",np.add(x,y))
print("Subtraction of matrices:",np.subtract(x,y))
print("Multiplication of matrices:",np.dot(x,y))
print("Transpose of matrix 1:",np.transpose(x))
print("Transpose of matrix 2:",np.transpose(y))
print("Inverse of Matrix 1:",np.linalg.inv(x))
print("Inverse of Matrix 2:",np.linalg.inv(y))
