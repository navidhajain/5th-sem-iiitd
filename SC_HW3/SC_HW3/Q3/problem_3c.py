import numpy as np
from matplotlib import pyplot as plt

class Vandermonde:
    def __init__(self):
        self.n_list = []
        self.cond_list = []
        
    def VandermondeMatrix_M(self, X,m):
        V = np.zeros([X.size,m], dtype=float)
        for i in range(X.size):
            for j in range(m):
                V[i][j] = self.monomial(j,X[i])
        return V
    
    def VandermondeMatrix_C(self, X,n):
        V = np.zeros([n,n], dtype=float)
        for i in range(n):
            for j in range(n):
                V[i][j] = self.chebyshev_polynomial(j,X[i])
        return V
    
    def chebyshev_polynomial(self,n,x):
        return np.cos(n * np.arccos(x))
    
    def monomial(self, n, x):
        return x**n
    
    def equispaced(self, n):
        return np.linspace(-1, 1, n)
    
    def chebyshev(self, n):
        M = np.zeros(n, dtype=float)
        for i in range(0, n):
            M[i] = np.cos((2*i + 1)/(2*n) * np.pi)
        return M
    
    def ret(self):
        li = [[self.monomial,self.equispaced],[self.monomial,self.chebyshev],[self.chebyshev_polynomial, self.equispaced],[self.chebyshev_polynomial, self.chebyshev]]
        for f in li:
            for n in range(5,101,5):
                X = f[1](n)
                if f[0].__name__=='monomial':
                    V = self.VandermondeMatrix_M(X,n)
                else:
                    V = self.VandermondeMatrix_C(X,n)
                self.n_list.append(n)
                self.cond_list.append(np.linalg.cond(V))
            name = 'function: '+f[0].__name__+' with nodes: '+f[1].__name__
            
            plt.semilogy(self.n_list, self.cond_list, '-o',label=name)
            self.n_list = []
            self.cond_list = []
            
        plt.xlabel("Interpolation Nodes")
        plt.ylabel('Condition number')
        plt.legend(loc='best')


        plt.show()
        
        
obj = Vandermonde()
# obj.VandermondeMatrix()
obj.ret()
