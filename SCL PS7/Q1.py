# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 06:17:59 2022

@author: sriva
"""
#Predictor Corrector method
from sympy import *
x, y = symbols('x y')

y_diff = (x + y) / 2
X = [0, 0.5, 1, 1.5]
Y = [2, 2.636, 3.595, 4.968]

n = len(X) - 1
h = X[1] - X[0]

# Predicting
value = Y[n - 3] + (4 * h / 3) * (2 * y_diff.subs(x, X[n - 2]).subs(y, Y[n - 2]) - y_diff.subs(x, X[n - 1]).subs(y, Y[n - 1]) + 2 * y_diff.subs(x, X[n]).subs(y, Y[n]))

# Correcting
value = Y[n - 1] + (h / 3) * (y_diff.subs(x, X[n - 1]).subs(y, Y[n - 1]) + 4 * y_diff.subs(x, X[n]).subs(y, Y[n]) + y_diff.subs(x, X[n] + h).subs(y, value))
print(value)

'''
#Adam Bashford
from sympy import *
x, y = symbols('x y')

y_diff = (x + y) / 2
X = [0, 0.5, 1, 1.5]
Y = [2, 2.636, 3.595, 4.968]

n = len(X) - 1
h = X[1] - X[0]

# Predicting
value = Y[n] + (h / 24) * (55 * y_diff.subs(x, X[n]).subs(y, Y[n]) - 59 * y_diff.subs(x, X[n - 1]).subs(y, Y[n - 1]) + 37 * y_diff.subs(x, X[n - 2]).subs(y, Y[n - 2]) - 9 * y_diff.subs(x, X[n - 3]).subs(y, Y[n - 3]))

# Correcting
value = Y[n] + (h / 24) * (9 * y_diff.subs(x, X[n] + h).subs(y, value) + 19 * y_diff.subs(x, X[n]).subs(y, Y[n]) - 5 * y_diff.subs(x, X[n - 1]).subs(y, Y[n - 1]) + y_diff.subs(x, X[n - 2]).subs(y, Y[n - 2]))
print(value)
'''