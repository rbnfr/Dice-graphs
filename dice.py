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
    faces = 20
    possible_points = range(2,(faces*2)+1)



    for i in range(1000):
        scramble1 = randint(1, faces)
        scramble2 = randint(1, faces)
        points = scramble1 + scramble2
        points_list.append(points)   
    #print (*points_list, sep="-")

    fin = [possible_points.index(i) for i in points_list]
    plt.hist(fin, bins=range(faces*2), align="left", color="orange")
    plt.xticks(range(faces*2), possible_points)

    plt.xlabel("Results")
    plt.ylabel("Frequency")
    plt.show()
    
if __name__ == '__main__':
    main()