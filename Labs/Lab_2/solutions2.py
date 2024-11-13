# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 13:01:57 2024

@author: domin
"""

import functions2 as f2
import cmath
from numpy import tan,pi,cos,sin

class solutions:
    
       
   def print_list(self,lis):
       print("Najdene ničle so")
       print("-"*18)
       for r in lis:
           print(f"{r:.4f}")
       
   def task_one(self):
       def function(x):
           return x*x+x+1
       def d_function(x):
           return 2*x+1
       f2.plot(function, [-10,10])
       x_guess=1+1j
       x_n=f2.tangent(function, d_function,x_guess)
       print("Kompleksni ničli sta: ")
       print(f"{x_n.real:.4f} + i{x_n.imag:.4f}")
       print(f"{x_n.real:.4f} - i{x_n.imag:.4f}")
      
   def task_two(self):
        def function(x):
            return x*x+x-1 - tan(x)
        def d_function(x,_,__):
            return 2*x - tan(x)*tan(x)
        f2.plot(function, [0,6*pi])
        roots=f2.bisection_root_scan(function, 0, 6*pi, 0.001)
        self.print_list(roots)
        print(f"Najdenih je {len(roots)} ničel")
        
        """
        roots2=f2.tangent_root_scan(function, 0, 6*pi, step=0.01,df=d_function)#d_function)
        roots2=sorted([root for root in roots2 if 0<root<6*pi])
        print("\n")
        self.print_list(roots2)
        """
        
   def task_three(self):
        def function(x):
            return x-cos(x)
        def d_function(x):
            return 1+sin(x)
        f2.plot(function, [-2,2])
        x0=0
        root=f2.tangent(function,d_function,x0)        
        print(f"Ničla je pri x = {root:.4f}")
        
   def four_a(self):
        def function(x):
            return 0.1*x*x*x*x - 2*x*x*x - 1.5*x*x + 3*x - 4.5
        def d_function(x):
            return 0.4*x*x*x - 6*x*x - 3*x + 3
        roots = f2.tangent_complex_root_scan(function, d_function, [-10, 10], [-10, 10], [1, 1])  
        self.print_list(roots)

   def four_b(self):
        def function(x):
            return 0.1*x**5 - 3*x**3 + 5
        def d_function(x):
            return 0.5*x**4 - 9*x**2 +5
        roots = f2.tangent_complex_root_scan(function, d_function, [-10, 10], [-10, 10], [1, 1])  
        self.print_list(roots)

   def four_c(self):
        def function(x):
            return 1j*x**4 - 2*x**3 + x**2 + 5
        def d_function(x):
            return 4j*x**3 - 4*x + 2 + 2*x
        roots = f2.tangent_complex_root_scan(function, d_function, [-10, 10], [-10, 10], [1, 1])  
        self.print_list(roots)
         
   def task_five(self):
          def function(V, a,b,n,p,T):
              R=0.0821
              return p*V - p*n*b + a*n*n/V - a*n*n*n*b/(V*V) - n*R*T
          a=1.408
          b=0.03913
          n=2.05
          p=0.986923
          T=302.15

          volumen=f2.secant(function, 0.1, 100, 1e-9,a,b,n,p,T)       
          print(f"Ničla je pri V = {volumen:.4f} L")
          
          import matplotlib.pyplot as plt
          import numpy as np
          x=np.linspace(0.1,100)
          T_list=np.array([T*50 for T in range(0,10)])
          for Tm in T_list:
              plt.plot(x,function(x,a,b,n,p,Tm), label=f"{Tm:.0f} K")
          plt.legend()
          plt.show()
          
   def task_six_a(self):
        def function(x):
            return x*x*x-1
        def d_function(x):
            return 3*x*x
        def root_index(sez):
            for i in range(len(sez)):
                if (sez[i]==True):
                    return i
            return -1
            
        
        # we scan -2 to 2 in both directions
        roots=[]
        roots1=[]
        roots2=[]
        roots3=[]
        import numpy as np
        import matplotlib.pyplot as plt
        x=np.linspace(-2,2,100)
        y=np.linspace(-2,2,100)
        X,Y=np.meshgrid(x,y)
        for dim1 in range(X.shape[0]):
            for dim2 in range(X.shape[1]):
                a=complex(X[dim1,dim2],Y[dim1,dim2])
                complex_root=f2.tangent(function, d_function, a)
                
                is_simi = [(abs(x.real - complex_root.real) < 1e-6 and abs(x.imag - complex_root.imag) < 1e-6) for x in roots]
                if not any(is_simi):
                    roots.append(complex_root)

                ind=root_index(is_simi)
                match ind:
                    case 0:
                        roots1.append(a)
                    case 1:
                        roots2.append(a)
                    case 2:
                        roots3.append(a)
        roots1=np.array(roots1)
        roots2=np.array(roots2)
        roots3=np.array(roots3)
        plt.plot(roots1.real,roots1.imag,"o")
        plt.plot(roots2.real,roots2.imag,"o")
        plt.plot(roots3.real,roots3.imag,"o")
        plt.show()
        plt.clf()

   def task_six_b(self):
          def function(x):
              return x**4 - 1
          def d_function(x):
             return 4 * x**3 
          def root_index(sez):
              for i in range(len(sez)):
                  if (sez[i]==True):
                      return i
              return -1
              
          
          # we scan -2 to 2 in both directions
          roots=[]
          roots1=[]
          roots2=[]
          roots3=[]
          roots4=[]
          import numpy as np
          import matplotlib.pyplot as plt
          x=np.linspace(-2,2,20)
          y=np.linspace(-1.9,1.9,20) #it gets stuck if it does not converge, i have made a seperate script just for task_six
          X,Y=np.meshgrid(x,y)
          for dim1 in range(X.shape[0]):
              for dim2 in range(X.shape[1]):
                  a=complex(X[dim1,dim2],Y[dim1,dim2])
                  complex_root=f2.tangent(function, d_function, a)
                  is_simi = [(abs(x.real - complex_root.real) < 1e-4 and abs(x.imag - complex_root.imag) < 1e-4) for x in roots]
                  if not any(is_simi):
                      roots.append(complex_root)

                  ind=root_index(is_simi)
                  match ind:
                      case 0:
                          roots1.append(a)
                      case 1:
                          roots2.append(a)
                      case 2:
                          roots3.append(a)
                      case 3:
                          roots4.append(a)
                          
          roots1=np.array(roots1)
          roots2=np.array(roots2)
          roots3=np.array(roots3)
          roots4=np.array(roots4)
          plt.plot(roots1.real,roots1.imag,"o")
          plt.plot(roots2.real,roots2.imag,"o")
          plt.plot(roots3.real,roots3.imag,"o")      
          plt.plot(roots4.real,roots4.imag,"o")                   
          plt.show()
          plt.clf()
                
        
       
       
       
       
res=solutions()
res.task_one()
res.task_two()
res.task_three()
res.four_a()
res.four_b()
res.four_c()
res.task_five()
res.task_six_a()
res.task_six_b()
