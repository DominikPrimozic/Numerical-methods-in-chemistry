# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 08:03:30 2024

@author: domin
"""

import functions3 as f3

class solutions():
    
    def task_one_a(self):
        y="y"
        while y=="y":
            N=int(input("How many point? "))
            a=0
            b=1
            analytical=1/30
            trapez=f3.trapez_integration(lambda x:x*x*(1-x)*(1-x), a, b, N)
            error=abs((analytical-trapez)/analytical)
            print(f"Relative error with {N} points is {error:.4f}")
            if error<0.001: break
            print("Try again")
            # seven points are needed for trapez
        print(f"Trapez method was good with {N} points")
        
        print("Now try simpson")
        y="y"
        while y=="y":
            N=int(input("How many point? "))
            a=0
            b=1
            analytical=1/30
            simpson=f3.simpson_integration(lambda x:x*x*(1-x)*(1-x), a, b, N)
            error=abs((analytical-simpson)/analytical)
            print(f"Relative error with {N} points is {error:.4f}")
            if error<0.001: break
            print("Try again")
            # nine points are needed 
        print(f"Simpson method was good with {N} points")
        
        print("Now try montecarlo")
        y="y"
        while y=="y":
            N=int(input("How many point? "))
            a=0
            b=1
            analytical=1/30
            mc=f3.monte_carlo_integration(lambda x:x*x*(1-x)*(1-x), [a,0], [b,1], N)
            error=abs((analytical-mc)/analytical)
            print(f"Relative error with {N} points is {error:.4f}")
            if error<0.001: break
            print("Try again")
            # lot points are needed 
        print(f"MC method was good with {N} points")
        
    def task_one_a_1(self):
        N=2
        a=0
        b=1
        analytical=1/30
        error=1
        while error>0.001:
            trapez=f3.trapez_integration(lambda x:x*x*(x-1)*(x-1), a, b, N)
            error=abs((analytical-trapez)/analytical)
            N+=1
            print(f"Relative error for trapez with {N} points is {error:.4f}")
            # seven points are needed for trapez
        print(f"Trapez method was good with {N} points")
        
        print()
        N=3
        error=1
        while error>0.001:
            simpson=f3.simpson_integration(lambda x:x*x*(x-1)*(x-1), a, b, N)
            error=abs((analytical-simpson)/analytical)
            print(f"Relative error for simpson with {N} points is {error:.4f}")
            N+=2
        print(f"Simpson method was good with {N} points")
        
        print()
        N=10
        error=1
        while error>0.001:
            mc=f3.monte_carlo_integration_visual(lambda x:x*x*(x-1)*(x-1), [a,0], [b,0.2], N)
            error=abs((analytical-mc)/analytical)
            print(f"Relative error monte carlo with {N} points is {error:.4f}")
            N*=10
        print(f"MC method was good with {N} points")  
        
    def task_one_b(self):
        from numpy import exp
        N=2
        a=0
        b=1
        analytical=1/2 - 1/exp(1)
        error=1
        while error>0.001:
            trapez=f3.trapez_integration(lambda x:exp(-x)+x-1, a, b, N)
            error=abs((analytical-trapez)/analytical)
            N+=1
            print(f"Relative error for trapez with {N} points is {error:.4f}")
            # seven points are needed for trapez
        print(f"Trapez method was good with {N} points")
        
        print()
        N=3
        error=1
        while error>0.001:
            simpson=f3.simpson_integration(lambda x:exp(-x)+x-1, a, b, N)
            error=abs((analytical-simpson)/analytical)
            print(f"Relative error for simpson with {N} points is {error:.4f}")
            N+=2
        print(f"Simpson method was good with {N} points")
        
        print()
        N=10
        error=1
        while error>0.001:
            mc=f3.monte_carlo_integration(lambda x:exp(-x)+x-1, [a,0], [b,2], N)
            error=abs((analytical-mc)/analytical)
            print(f"Relative error monte carlo with {N} points is {error:.4f}")
            N*=10
        print(f"MC method was good with {N} points")
        
    def task_one_c(self):
        from numpy import sin,pi
        N=2
        a=0
        b=pi
        analytical=pi*pi/4
        error=1
        while error>0.001:
            trapez=f3.trapez_integration(lambda x:x*sin(x)*sin(x), a, b, N)
            error=abs((analytical-trapez)/analytical)
            N+=1
            print(f"Relative error for trapez with {N} points is {error:.4f}")
            
        print(f"Trapez method was good with {N} points")
        
        print()
        N=3
        error=1
        while error>0.001:
            simpson=f3.simpson_integration(lambda x:x*sin(x)*sin(x), a, b, N)
            error=abs((analytical-simpson)/analytical)
            print(f"Relative error for simpson with {N} points is {error:.4f}")
            N+=2
        print(f"Simpson method was good with {N} points")
        
        print()
        N=10
        error=1
        while error>0.001:
            mc=f3.monte_carlo_integration(lambda x:x*sin(x)*sin(x), [a,0], [b,2], N)
            error=abs((analytical-mc)/analytical)
            print(f"Relative error monte carlo with {N} points is {error:.4f}")
            N*=10
        print(f"MC method was good with {N} points")
        
        
    def task_two(self):
        a=1;
        b=4;
        
        print("Simpson")
        print("#"*10)
        N=[7,13,19]
        for n in N:
            simpson=f3.simpson_integration(lambda x: (1+x*x)**0.5, a, b, n)
            print(f"{(n-1)/2}", ""*5, f"{simpson:.5f}")
        print("\nTrapez")
        print("#"*10)
        for n in N:
            simpson=f3.trapez_integration(lambda x: (1+x*x)**0.5, a, b, n)
            print(f"{(n-1)}", ""*5, f"{simpson:.5f}")
        print("\nLeft Riemann")
        print("#"*10)
        for n in N:
            simpson=f3.riemann_integration(lambda x: (1+x*x)**0.5, a, b, n,ty=-1)
            print(f"{(n-1)}", ""*5, f"{simpson:.5f}")
        print("\nMid Riemann")
        print("#"*10)
        for n in N:
            simpson=f3.riemann_integration(lambda x: (1+x*x)**0.5, a, b, n,ty=0)
            print(f"{(n-1)}", ""*5, f"{simpson:.5f}")
        print("\nRight Riemann")
        print("#"*10)
        for n in N:
            simpson=f3.riemann_integration(lambda x: (1+x*x)**0.5, a, b, n,ty=1)
            print(f"{(n-1)}", ""*5, f"{simpson:.5f}")
      
    def task_three_a(self):
        a=-0.5
        b=0.5
        N=4
        from numpy import cos
        integral=f3.trapez_integration(lambda x: cos(x)*cos(x), a, b, N)
        print(f"Integral is {integral:.5f}")
    def task_three_b(self):
        a=-0.5
        b=0.5
        N=6
        from numpy import log
        integral=f3.trapez_integration(lambda x: x*log(x+1), a, b, N)
        print(f"Integral is {integral:.5f}")
    def task_three_c(self):
        a=0.75
        b=1.75
        N=8
        from numpy import sin
        integral=f3.trapez_integration(lambda x: sin(x)*sin(x) - 2*x*sin(x) +1, a, b, N)
        print(f"Integral is {integral:.5f}")
    def task_three_d(self):
        from numpy import exp,log
        a=exp(1)
        b=exp(1)+2
        N=8
        
        integral=f3.trapez_integration(lambda x: 1/(x*log(x)), a, b, N)
        print(f"Integral is {integral:.5f}")
        
    def task_four(self):
        """
        Half sphere with radius 4 
        x^2+y^2+z^2=4, a=[-4,-4,0], b=[4,4,4]
        """
        def half_sphere(x,y,z,R):
            r2=x**2 + y**2 + z**2
            if R>=r2**0.5:
                return True;
            else:
                return False;
                
        a=[-4,-4,0]
        b=[4,4,4]
        integral=f3.monte_carlo_sphere(half_sphere, a, b, 1000, 4)
        print(f"Volume is {integral:.5f}")
        
#res=solutions()
#res.task_one_a()
#res.task_one_a_1()
#res.task_one_b()
#res.task_one_c()
#res.task_two()
#res.task_three_a()
#res.task_three_b()
#res.task_three_c()
#res.task_three_d()
#res.task_four()

