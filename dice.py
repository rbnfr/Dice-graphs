# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""
from random import randint
import matplotlib as plt

points = ""
possible_points = [1,2,3,4,5,6]
points_list = []

for i in range(100):
    scramble1 = randint(1,6)
    scramble2 = randint(1,6)
    points = scramble1 + scramble2
    points_list[i] = points
    

plt.hist(points_list, bins=range(11), align="left")

plt.title("Dice results distribution")
plt.xlabel("Points obtained")
plt.ylabel("Repetitions")
plt.show()