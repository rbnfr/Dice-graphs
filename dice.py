# -*- coding: utf-8 -*-
"""
Author: Ruben
"""


def main():
    """ Main method """
    from random import randint
    import matplotlib.pyplot as plt

    points = ""
    points_list = []
    faces1 = 20
    faces2 = 4
    rolls = 100000
    possible_points = range(2,(faces1+faces2)+1)



    for i in range(rolls):
        scramble1 = randint(1, faces1)
        scramble2 = randint(1, faces2)
        points = scramble1 + scramble2
        points_list.append(points)   
    #print (*points_list, sep="-")

    fin = [possible_points.index(i) for i in points_list]
    plt.hist(fin, bins=range(faces1+faces2), align="left", color="orange")
    plt.xticks(range(faces1+faces2), possible_points)

    plt.xlabel("Results")
    plt.ylabel("Frequency")
    plt.show()
    
if __name__ == '__main__':
    main()