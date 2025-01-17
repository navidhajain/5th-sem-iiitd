# -*- coding: utf-8 -*-
"""problem_7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11dpbHFWFdETIfB4vQEzr7Y1SuPq2zCr-
"""

import numpy as np
from numpy.linalg import inv

a = [[6, 2, 1], [2, 3, 1], [1, 1, 1]]
error = 1.1102230246251565e-16
lamiden = [[2, 0, 0], [0, 2, 0], [0, 0, 2]]
anew = np.subtract(a, lamiden)
# print(anew)
x = [[0], [0], [1]]
yold = [[0], [0], [0]]
ainv = np.linalg.inv(anew)
flag = True

evalue, evect = np.linalg.eig(anew)
emax = max(evalue)
# print(emax)

while flag:
    y = np.matmul(ainv, x)
    ynorm = max(abs(y))
    x = y/(ynorm[0])
    # print(y)
    if max(abs(np.subtract(yold, y))) < error:
        flag = False
    for i in range(3):
        yold[i] = y[i]

print('Shifted inverse method: ')
print('eigenvalue: ', 1/(ynorm[0]) + 2)
print('eigenvector is', x)

print('According to the library')
evalue, evect = np.linalg.eig(a)
print('eigenvalues are', evalue)
print('eigenvectors are', evect)

# def get_xn(x):
#     norm = max(abs(x))
#     xn = x / max(x)
#     return norm, xn

# a_inv = inv(anew)
# print(anew)
# for i in range(100):
#     y=np.linalg.solve(anew, x)
#     ynorminv=max(abs(y))
#     x=y/ynorminv
#     # x = np.dot(a_inv, x)
#     # lam, x = get_xn(x)

# print('Eigenvalue:', ynorminv)
# print('Eigenvector:', x)

# while flag:
#   # c+=1
#   y=np.linalg.solve(anew, x)
#   ynorminv=max(abs(y))
#   x=y/ynorminv
#   # print(c)
#   # print(np.subtract(yold, y))
#   if max(abs(np.subtract(np.matmul(anew, yold), np.matmul(anew, y))))<error:
#     flag=False
#   for i in range(3):
#     yold[i]=y[i]

# print('approximation of the smallest value of eigenvalue is ', ynorminv)
# print('approximation of the smallest eigenvector is ', x)
