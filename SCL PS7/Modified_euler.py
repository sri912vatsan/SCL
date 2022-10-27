# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 23:59:23 2022

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
X=x0
Y = y0

while not math.isclose(X,X_):
    Y = Y + h*y_diff.subs(x,X+0.5*h).subs(y,Y+0.5*h*y_diff.subs(x,X).subs(y,Y))
    X += h
print(Y)