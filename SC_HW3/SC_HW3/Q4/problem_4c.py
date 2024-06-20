import numpy as np
import matplotlib.pyplot as plt
import math


class Interpolate1D:
    def __init__(self):
        self.x_init = 0
        self.x = 0
        self.y = 0
        
    def cubic_interpolate(self):
        
        if np.any(np.diff(self.x)<0):
            indices = np.argsort(self.x)
            self.x = self.x[indices]
            self.y = self.y[indices]
            
        
        self.L1 = np.array([0. for i in range(len(self.x))])
        self.L2 = np.array([0. for i in range(len(self.x)-1)])
        self.z =  np.array([0. for i in range(len(self.x))])

        self.L1[0] = math.sqrt(2*np.diff(self.x)[0])
        self.__allocate_matrix_and_vector()
        
        return self.__solve()
        
    def __solve(self):
        i = len(self.x)-1
       
        self.z[i]/=self.L1[i]
        
        for i in range(len(self.x)-2,-1,-1):
            self.z[i] = (self.z[i]-self.L2[i-1]*self.z[i+1])/self.L1[i]
        
        index = self.x.searchsorted(self.x_init)
        np.clip(index, 1, len(self.x)-1, index)
        
        x1 = [self.x[index-1], self.x[index]]
        y1 = [self.y[index-1], self.y[index]]
        z1 = [self.z[index-1], self.z[index]]
        h1 = x1[1]-x1[0]
        h2 = y1[1]-y1[0]
        h3 = z1[1]-z1[0]
        
        f1 = z1[0]/(6*h1)*(x1[1]-self.x_init)**3
        f2 = z1[1]/(6*h1)*(self.x_init-x1[0])**3
        f3 = (y1[1]/h1- z1[1]*h1/6)*(self.x_init-x1[0]) + (y1[0]/h1 - z1[0]*h1/6) * (x1[1]-self.x_init)
        
        return f1+f2+f3
    
    def __allocate_matrix_and_vector(self):
        difference_x = np.diff(self.x)
        difference_y = np.diff(self.y)
        
        for i in range(1, len(self.x)-1,1):
            self.L2[i] = difference_x[i-1]/self.L1[i-1]
            self.L1[i] = math.sqrt(2*(difference_x[i-1]+difference_x[i]) - (self.L2[i-1]**2))
            self.B_i = 6*((difference_y[i]/difference_x[i]) - (difference_y[i-1]/difference_x[i-1]))
            self.z[i] = (self.B_i-self.L2[i-1]*self.z[i-1])/self.L1[i]
            
        
        k = len(self.x)-1
        
        self.L2[k-1] = difference_x[len(difference_x)-1]/self.L1[k-1]
        self.L1[k] = math.sqrt(2*(difference_x[len(difference_x)-1]) - (self.L2[k-1]**2))
        self.B_i = 0.
        self.z[k] = (self.B_i-self.L2[k-1]*self.z[k-1])/self.L1[k]
            
        
    def generate_vectors(self):
        np.random.seed(0)
        self.x = np.random.rand(6).astype(float)
        print(self.x)
        self.y = np.random.rand(6).astype(float)
        print(self.y)
        self.x_init = self.x
        f = self.cubic_interpolate()
        self.plot(f)
    
    def plot(self,f):
        plt.scatter(self.x,self.y)
        plt.plot(self.x_init, f)
        plt.xlabel("X")
        plt.ylabel("Y(Computed from cubic interpolation)")
        plt.show()        
        
obj = Interpolate1D()
obj.generate_vectors()
        
        