# -*- coding: utf-8 -*-
"""problem_5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qCY8PrcJW6_LCZpYsFiHM3kFHdrVr0E9
"""

import numpy as np
import math
import matplotlib.pyplot as plt


def f(x):
    return math.exp(-(math.sin(x**3))/4)


def fda(x, h):
    return (f(x+h)-f(x))/h


error = [0]*15
h = [0]*15
x = 1
xtrue = -3/4*(math.cos(1))*(math.exp(-(math.sin(1))/4))

for i in range(15):
    h[i] = 10**(-(i+1))
    fd_comp = fda(x, h[i])
    error[i] = abs(fd_comp-xtrue)
    print('for h =', h[i], 'error is', error[i])

plt.loglog(h, error)
plt.xlabel('log(h)')
plt.ylabel('log(absolute error)')
plt.show()
