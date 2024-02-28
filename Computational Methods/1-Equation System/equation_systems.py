"""
Name: Mariam Alabi
Assignment 1
Submitted on 05/11/2023
"""

import numpy as np
import matplotlib.pyplot as plt

a = np.array([[0,6,-2,0,0,0],
             [0,4,1,2,2,0],
             [0,0,0,0,2,4],
             [1,-1,0,1,0,0],
             [0,0,1,0,-1,1],
             [0,0,0,1,-1,1]])

y = np.array([10,17,14,0,0,0])

#Gausian Elimination method
x = np.linalg.solve(a,y)
print(x)
#Inverse Method
ai = np.linalg.inv(a)
d = ai@y
print(d)

#Create Graph
plt.bar(np.arange(1,7), x)
plt.xlabel('Nodes')
plt.ylabel('Current')
plt.savefig('a1_graph.pdf')
