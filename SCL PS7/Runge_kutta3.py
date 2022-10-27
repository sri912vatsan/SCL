# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 00:07:23 2022

@author: sriva
"""

import math
from sympy import *
x,y = symbols('x y')

y_diff = (x-y)/2
x0 = 0
y0 = 1
h = 0.1
X_ = 0.2
X = x0
Y = y0

while not math.isclose(X, X_):
    k1 = h*y_diff.subs(x,X).subs(y,Y)
    k2 = h*y_diff.subs(x,X+h/2).subs(y,Y+k1/2)
    k3 = h*y_diff.subs(x,X+h).subs(y,Y+2*k2-k1)
    Y = Y+(k1+4*k2+k3)/6
    X += h
    
print(Y)