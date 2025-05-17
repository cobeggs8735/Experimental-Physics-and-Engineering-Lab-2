#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 08:25:50 2019

@author: colemanbeggs
"""

# Coleman Beggs
# PHYS216-502
# Homework 2

import numpy as np
import numpy.linalg as alg

"""
Problem 1.
Given A = np.array([1, -2, 3], [4, 5, -6]) and B = np.array([3, 0, 2], [-7, 1, 8]), perform the following operations (on paper). 
If an operation is not defined, explain why it cannot be performed. Verify your results using python.
"""

A1 = np.array([[1, -2, 3], [4, 5, -6]])
B1 = np.array([[3, 0, 2], [-7, 1, 8]])

a1 = A1 + B1
b1 = 2*A1 - B1
c1 = 3 * B1

print("Problem 1.\n", "a):\n", a1, "\n", "b):\n", b1, "\n", "c):\n", c1, "\n") 

"""
Problem 2
Given A = np.array([[1, 3], [2, -1]]) and B = np.array([[2, 0, -4], [3, -2, 6]]), perfrom the following operations (on paper). 
If an operation is not defined, expalin why it cannot be performed. Verify your results using python.
"""

A2 = np.array([[1, 3], [2, -1]])
B2 = np.array([[2, 0, -4], [3, -2, 6]])

a2 = np.matmul(A2, B2)
#b2 = np.matmul(B2, A2) #Error: Incorrect shape to multipy

print("Problem 2.\n", "a):\n", a1, "\n",  "b): Could not compute because of incorrect matrix dimensions\n")

"""
B2 multiplied A2 cannot be computed because the shapes of the matrices don't allow it.
"""

"""
Problem 3. 
Given A = np.array([[1, 0, 2], [2, -1, 3], [4, 1, 8]]) and B = np.array([[-11, 2, 2], [-4, 0, 1][6, -1, -1]]), perfrom the following 
operations (on paper). If an operation is not defined, explain why it cannot be performed. Verify your results using Python. Based
on your results, what can you say about the relationship of A to B?
"""

A3 = np.array([[1, 0, 2], [2, -1, 3], [4, 1, 8]])
B3 = np.array([[-11, 2, 2], [-4, 0, 1], [6, -1, -1]])

a3 = np.matmul(A3, B3)
b3 = np.matmul(B3, A3)

print("Problem 3.\n", "a):\n", a3, "\n", "b):\n", b3, "\nA multiplied by B and vice versa gives a unit matrix\n")

"""
A multiplied by B & B multiplied by A create a unit matrix
"""

"""
Problem 4.
Solve the following set of equation using numpy's linear algebra capabilities.

7x + 5y - 3z = 16
3x - 5y + 2z = -8
5x + 3y - 7z = 0

a) First, on paper, put the equation in the form Ax = b.

b) Next, create arrays in Python for the A and b matrices.

c) Use numpy’s solve() function to solve for the x matrix.  Record the results on paper.

d) Finally, verify the solution by printing the matrix product Ax to show that it is indeed b.

e) Just for fun, calculate A^(-1), the inverse of A.  Show that the product A^(-1) b gives the same result for x. 
Record the result on paper.
"""

A4 = np.array([[7, 5, -3], [3, -5, 2], [5, 3, -7]])
B4 = np.array([[16], [-8], [0]])

c4 = alg.solve(A4, B4)
# d)
print("Problem 4.\n", "Matrix product of Ax is:\n", np.matmul(A4, c4), "\n") # Product of Ax (is the same as b)

e4 = alg.inv(A4) # Inverse of A
print("Inverse of A is:\n", e4, "\n")
print("A^(-1) * b =\n", np.matmul(A4, B4), "\n")
print("x =\n", c4, "\n")

"""
Problem 5.
Solve the following set of equations using numpy's linear algebra capabilities.

5y + 2w + z - x = -3
3w + 2x + 2y - 6z = -32
3x + 3y - z + w = -47
3z + 5w -2x -3y = 49

a) First, on paper, put the equation in the form Ax=b.  Remember, each column of the coefficient matrix A represents coefficients 
of one of the variables.  You’ll need to rewrite the equations above in that format before creating the A matrix.

b) Next, create arrays in Python for the A and b matrices.

c) Use numpy’s solve() function to solve for the x matrix.  Record the results on paper.

d) Finally, verify the solution by printing the matrix product Ax to show that it is indeed b.

e) Just for fun, calculate A^(-1), the inverse of A.  Show that the product A^(-1) b gives the same result for x.  Record the result 
on paper.
"""

A = np.array([[2, -1, 5, 1], [3, 2, 2, -6], [1, 3, 3, -1], [5, -2, -3, 3]])
b = np.array([[-3], [-32], [-47], [49]])
x = alg.solve(A, b)

Ax = np.matmul(A, x) # Checking that Ax = b

Ainv = alg.inv(A)

print("x =\n", x)
print("Problem 5\n", "A^(-1) * b =\n", np.matmul(Ainv, b), "\n")
