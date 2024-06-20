# -*- coding: utf-8 -*-
"""problem_3b.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VOdy_6PRemToj7DXgl-owkLBGbztVZ64
"""

import matplotlib.pyplot as plt
import numpy as np
import bisect


def f(t):
    return 1/(1 + 25 * (t**2))


x = np.linspace(-1, 1, 100)
y_original = [f(t_) for t_ in x]

# cubic spline interpolation


def change(x):
    x1 = []
    for i in range(len(x)-1):
        x1.append(x[i+1]-x[i])

    return x1


def make_mat(n, h):
    a, c = [], [0]
    b = [2]*n
    for i in range(n-2):
        a.append(h[i]/(h[i] + h[i+1]))
        c.append(h[i+1]/(h[i] + h[i+1]))
    a.append(0)

    return a, b, c


def term(n, h, y):
    t = [0]
    for i in range(1, n-1):
        t.append(6*((y[i+1] - y[i])/h[i] -
                 (y[i] - y[i-1])/h[i-1])/(h[i] + h[i-1]))
    t.append(0)

    return t


def solve(a, b, c, d):
    c1 = c+[0]
    d1 = [0]*len(b)
    x = [0]*len(b)
    c1[0] = c[0]/b[0]
    d1[0] = d[0]/b[0]

    for i in range(1, len(b)):
        denc1 = b[i]-c1[i-1]*a[i-1]
        c1[i] = c1[i]/denc1
        dend1 = b[i]-c1[i-1]*a[i-1]
        d1[i] = (d[i]-d1[i-1]*a[i-1])/dend1

    x[-1] = d1[-1]
    for i in range(len(b)-2, -1, -1):
        x[i] = d1[i]-c1[i]*x[i+1]

    return x


def spline(x, y):
    h = change(x)
    a, b, c = make_mat(len(x), y)
    d = term(len(x), h, y)
    m = solve(a, b, c, d)

    coeffs = []

    for i in range(len(x)-1):
        p = [((m[i+1]-m[i])*h[i]*h[i])/6, (m[i]*h[i]*h[i])/2,
             (y[i+1] - y[i] - (([i+1]+2*m[i])*h[i]*h[i])/6), y[i]]
        coeffs.append(p)

    n = len(x)

    def spline1(a):
        idx = min(bisect.bisect(x, a)-1, n-2)
        z = (a-x[idx])/h[idx]
        c = coeffs[idx]
        ans = (((c[0]*z) + c[1])*z + c[2])*z + c[3]

        return ans

    return spline1


s = spline(x, y_original)

x11 = np.linspace(-1, 1, 31)
y11 = [s(y) for y in x11]

plt.plot(x11, y11, 'ro')
plt.plot(x, y_original, 'b-')
plt.grid(True)
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)
plt.xlabel('x')
plt.ylabel('y')
plt.show()

x21 = np.linspace(-1, 1, 51)
y21 = [s(y) for y in x21]

plt.plot(x21, y21, 'ro')
plt.plot(x, y_original, 'b-')
plt.grid(True)
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)
plt.xlabel('x')
plt.ylabel('y')
plt.show()