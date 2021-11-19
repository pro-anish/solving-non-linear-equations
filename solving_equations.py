#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 11:34:17 2021

@author: davinci
"""
#%%
import sympy as sym
from sympy import lambdify
x= sym.Symbol('x')

def f(x):
    return x**3-3


def Bisection(a,b,tol):
    
    if f(a)*f(b) >= 0:
       return('wrong assumption')
    iterations = 0
    while (b-a) >= tol:
        
        #midpoint
        c=(a+b)/2
        
        
        #if c is the root of the equation
        if f(c) == 0:
            return c
        

        # Decide the side to repeat the steps        
        elif f(c)*f(b) < 0:
            a = c
        else:
            b = c
        iterations+=1
    return (c,'iterations:',iterations)
    

    
      
    
def Regulafalsi(a,b,tol):
    if f(a) * f(b) >= 0:
        return ("You have not assumed right a and b")
     
     
    c_before =0
    c_after=a
    iterations=0
    while abs(c_before-c_after)>=tol:
        c_before=c_after
        
         
        #the point that touches x axis
        c_after = (a * f(b) - b * f(a))/ (f(b) - f(a))
        
         
        #if c is the root of the equation
        if f(c_after) == 0:
            return c_after
         
        # Decide the side to repeat the steps
        elif f(c_after) * f(a) < 0:
            b = c_after
        else:
            a = c_after
        iterations+=1
        
    
    return (c_after,'iterations:',iterations)

def deriv_value(p,q):
    f_diff = p.diff(x)
    f_diff= lambdify(x,f_diff)
    return f_diff(q)
    

def NewtonRaphson(val,tol):
    h= f(val)/deriv_value(f(x),val)
    iterations=0
    while h>= tol:
        h= f(val)/deriv_value(f(x),val)
        val= val-h
        iterations+=1
    return (val,'iterations:',iterations)
 


    

def output(x):
    print(x.__name__,'method:')
    
    for i in range(3,6):
        
        print('Tolerance: ',10**(-i),', value: ',x(1.25,1.75,10**-i))  
    print('\n')
    

print('\nROOT OF THE EQUATION x**3 - 3 = 0 BY DIFFERENT METHODS\n')
        
output(Bisection) 

output(Regulafalsi)

print(NewtonRaphson.__name__,'method:')

for i in range(3,6):
    print('Tolerance: ',10**(-i),', value: ',NewtonRaphson(1.5,10**-i))  
    
    



   

    
    
    
    
    
    
    
    
    
    
    
    
