# -*- coding: utf-8 -*-
"""
Author: Ruben
"""
from random import randint
import matplotlib.pyplot as plt

points = ""
possible_points = range(2,13)
points_list = []

for i in range(10000):
    scramble1 = randint(1,6)
    scramble2 = randint(1,6)
    points = scramble1 + scramble2
    points_list.append(points)
    
#print (*points_list, sep="-")

fin = [ possible_points.index(i) for i in points_list]
plt.hist(fin, bins=range(12), align="left", color="orange")
plt.xticks(range(12), possible_points)

plt.xlabel("Results")
plt.ylabel("Frequency")
plt.show()


