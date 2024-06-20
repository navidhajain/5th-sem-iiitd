import math
import numpy as np


class NewtonSolution:
    def __init__(self,fx, derivative_fx,guess, tolerance):
        self.fx = fx
        self.derivative_fx = derivative_fx
        self.tolerance = tolerance
        self.guess = guess
        self.roots_list = []
        
    def f(self,x):
        return eval(self.fx)

    def f_dash(self,x):
        return eval(self.derivative_fx)

    def ret(self):
        roots = self.guess
        self.roots_list.append(self.guess)
        while self.f(roots)>self.tolerance:
            fx = self.f(roots)
            derivative_fx = self.f_dash(roots)
            roots = roots - (fx/derivative_fx)
            self.roots_list.append(roots)
        
        convergence_rate = self.get_c(self.roots_list,roots)
        return roots, convergence_rate
    
    def get_c(self,roots_list, roots):  
        e=[]
        for x in roots_list[:-1]:
            e.append(roots-x)
        i = len(roots_list)-3 ## length of e is 1 less than the length of roots_list, hence we the last index will be len(roots_list)-2.
        rate = np.log(abs(e[i]/e[i+1]))/np.log(abs(e[i-1]/e[i]))
        return rate
    
print()
obj = NewtonSolution("x**2-1","2*x",1e6,1e-12)
print("Root: "+ str(obj.ret()[0])+", Convergence Rate: "+ str(obj.ret()[1]))
print()
obj_2 = NewtonSolution("(x-1)**4","4*(x-1)**3",10,1e-12)
print("Root: "+ str(obj_2.ret()[0])+", Convergence Rate: "+ str(obj_2.ret()[1]))
print()
obj_3 = NewtonSolution("x-np.cos(x)","1+np.sin(x)",1,1e-12)
print("Root: "+ str(obj_3.ret()[0])+", Convergence Rate: "+ str(obj_3.ret()[1]))
print()
