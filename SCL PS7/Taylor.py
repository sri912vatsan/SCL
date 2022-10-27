# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 23:38:24 2022

@author: sriva
"""

from sympy import *
x, y = symbols('x y')
f = Function('f')(x)
y = f

def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact *= i
    return fact

def taylor_series(y_diff,x0,y0,h):
    sum = 0
    for i in range(5):
        print(y_diff)
        sum += (h**i)*y_diff.subs(x,x0).subs(y,y0)/factorial(i)
        y_diff = diff(y_diff,x)
    return sum

y_diff = y**2+x
x0 = 0
y0 = 1
h = 0.1

print(taylor_series(y_diff, x0, y0, h))

    