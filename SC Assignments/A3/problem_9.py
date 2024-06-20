# -*- coding: utf-8 -*-
"""problem_9.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18_HxGmj6stNHkUe6VVa90r7NO0ZtwNIB
"""

import numpy as np

a6 = [[2, 3, 2], [10, 3, 4], [3, 6, 1]]
a7 = [[6, 2, 1], [2, 3, 1], [1, 1, 1]]


def qr_iter(a):
    for i in range(1500):
        shift = a[2][2]
        lam_iden = [[shift, 0, 0], [0, shift, 0], [0, 0, shift]]
        a_minus = np.subtract(a, lam_iden)
        q, r = np.linalg.qr(a_minus)
        rq = np.matmul(r, q)
        a = np.add(rq, lam_iden)

    return a


print('qr iteration matrix for matrix in problem 6 is ')
print(qr_iter(a6))
print()
print('qr iteration matrix for matrix in problem 7 is ')
print(qr_iter(a7))
