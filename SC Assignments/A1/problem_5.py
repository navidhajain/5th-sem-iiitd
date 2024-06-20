import math
import numpy as np

pi = math.pi

for i in range(21):

    x = pi/4 + 2*pi*pow(10, i)
    tanx = np.tan(x)
    print('x:', x, 'and tan(x):', tanx, ' when j = ', i)
    fwd = abs(1-tanx)
    bwd = 1.1102230246251565e-16
    cond = fwd/bwd
    print('condition number for this input is:', cond)
    abserror = x*bwd
    print('difference between input argument from the exact one: ', abserror)
    print()
