import numpy as np

#3*x+2*y=7
#5x-3y=-1

A = np.array([[3,2],[5,-3]], dtype='float')
B = np.array([[7],[-1]], dtype='float')

print(A)
print(B)

A_inv = np.linalg.inv(A) #A-1
print(A_inv)

print(A @ A_inv)