import numpy as np
import time as time

start = time.time()

for i in range(1, 5001):
    sumk = 0
    for j in range(1, i+1):
        sumk = sumk + (1/j)

    gamma = sumk - np.log(i)

    if i % 100 == 0:
        print(gamma, 'for n = ', i)

end = time.time()

print("time taken for this code to run is: ", end-start, 'seconds')
