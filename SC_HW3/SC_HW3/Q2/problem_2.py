import math    
import numpy as np    

class NewtonMethod:
    def __init__(self,f_s, jacobian,tolerance,max_it):
        self.f_s = f_s
        self.jacobian = jacobian
        self.tolerance = tolerance
        self.max_it = max_it
    
    def f_v(self,arr):
        f_s_values = []
        
        for x in self.f_s:
            f_s_values.append(eval(x))
            
        return np.array(f_s_values)
    
    def Jacob(self,arr):
        # print(len(self.jacobian),len(self.jacobian[0]))
        j_values = np.zeros([len(self.jacobian),len(self.jacobian[0])], dtype=float)
        for i in range(j_values.shape[0]):
            for j in range(j_values.shape[1]):
                j_values[i][j] = eval(self.jacobian[i][j])

        return np.array(j_values)
    
    
    def ret(self, arr):
        for i in range(self.max_it):
            f = self.f_v(arr) #numpy array
            if np.linalg.norm(f,np.inf)<=self.tolerance:
                break
            J = self.Jacob(arr) #numpy 2-D array
            
            delta_x = np.linalg.solve(J, -1*f) 
            delta_x_t = np.transpose(delta_x)
            arr = np.add(delta_x_t, arr)
        
        for x in range(len(arr)):
            arr[x] = round(arr[x],3)
        return np.around(arr,3)
    
    

class ConversionClass:
    def form_equation(self,x,y,z):
        f_s = ['arr[0]*math.sin(arr[1])*math.cos(arr[2])-'+str(x), 'arr[0]*math.sin(arr[1])*math.sin(arr[2])-'+str(y),'arr[0]*math.cos(arr[1])-'+str(z)]
        
        jacobian =  [
            ['math.sin(arr[1])*math.cos(arr[2])' ,  'arr[0]*math.cos(arr[1])*math.cos(arr[2])' , '-arr[0]*math.sin(arr[1])*math.sin(arr[2])'],
            ['math.sin(arr[1])*math.sin(arr[2])',    'arr[0]*math.sin(arr[2])*math.cos(arr[1])', 'arr[0]*math.sin(arr[1])*math.cos(arr[2])' ] ,
            ['math.cos(arr[1])' , '-arr[0]*math.sin(arr[1])','0']
        ]
        
        obj_b = NewtonMethod(f_s, jacobian, math.pow(math.e,-12),500)
        li = obj_b.ret([1,1,1])
        return li
    
    def cartesian_to_spherical(self, x_):
        r = np.sqrt(x_[0]**2+x_[1]**2+x_[2]**2)
        theta = np.arccos(x_[2]/r)
        rho = np.arctan(x_[1]/x_[0])
        return np.array([r, theta, rho])

    def spherical_to_cartesian(self, spherical):
        x = spherical[0] * np.sin(spherical[1]) * np.cos(spherical[2])
        y = spherical[0] * np.sin(spherical[1]) * np.sin(spherical[2])
        z = spherical[0] * np.cos(spherical[1])
        return np.array([x, y, z])



class TestClass:
    def test_2a(self):
        ##2a
        print('-----------------2a------------------')
        f_s = ['arr[0]+2*arr[1]-2','arr[0]**2+4*(arr[1]**2)-4'] #list of functions
        jacobian = [['1','2'],['2*arr[0]','8*arr[1]']] # jacobian matrix, for each equation in f_s

        obj = NewtonMethod(f_s,jacobian,1e-12,500)
        li = obj.ret([1,2])
        print(li)

        print('------------------------------------') 
        
    
    def test_2b_givenTest(self,x,y,z):
        f_s = ['arr[0]*math.sin(arr[1])*math.cos(arr[2])-'+str(x), 'arr[0]*math.sin(arr[1])*math.sin(arr[2])-'+str(y),'arr[0]*math.cos(arr[1])-'+str(z)]
        jacobian =  [
        ['math.sin(arr[1])*math.cos(arr[2])' ,  'arr[0]*math.cos(arr[1])*math.cos(arr[2])' , '-arr[0]*math.sin(arr[1])*math.sin(arr[2])'],
        ['math.sin(arr[1])*math.sin(arr[2])',    'arr[0]*math.sin(arr[2])*math.cos(arr[1])', 'arr[0]*math.sin(arr[1])*math.cos(arr[2])' ] ,
        [ 'math.cos(arr[1])' , '-arr[0]*math.sin(arr[1])','0']
        ]
        print(x)
        obj = NewtonMethod(f_s,jacobian,1e-12,500)
        print(obj.ret([1,1,1]))
        
    def test_2b_random_values(self):
        print('----------------2b-------------------')
        conv = ConversionClass()
        np.random.seed(0)
        for i in range(10):
            x_ = np.random.randn(3,1)# random vector
            
            w_prime = conv.form_equation(x_[0][0], x_[1][0], x_[2][0]) #form given equations, taking x_ as coefficients.
            
            x = conv.spherical_to_cartesian(w_prime) #form cartesian equations using r, theta and rho.

            w = conv.cartesian_to_spherical(x_) 
            
            
            relative_residual = np.linalg.norm(np.subtract(x, x_), ord=2) / np.linalg.norm(x_, ord=2)
            relative_error = np.linalg.norm(np.subtract(w, w_prime), ord=2) / np.linalg.norm(w, ord=2)

            print('--------'+'Observation: '+str(i+1)+'--------')
            print("Points Generated : ", x_)
            print("Relative Residual : ", relative_residual)
            print("Relative Error : ", relative_error)
            print('----------------')
        print('-------------------------------------')
        
        
testing = TestClass()
# testing.test_2a()
# testing.test_2b_givenTest(1,1,1)
testing.test_2b_random_values()