# -*- coding: utf-8 -*-
"""
Author: Ruben
"""


def main():
    """ Main method """
    from random import randint
    import matplotlib.pyplot as plt

    # PROGRAM VARIABLES
    points = 0
    points_list = []
    max_points = 0

    # USER VARIABLES
    rolls = 10000
    dice_list = {
        'D20': 20, 
        'D4': 4,
        'D6': 6,
        'D5': 5
        }    

    # HISTOGRAM RANGE
    min_points = len(dice_list)

    for faces in dice_list.values():
        max_points = max_points + faces

    possible_points = range(min_points,max_points+1)

    # GET DATA
    for i in range(rolls):
        points = 0
        for dice in dice_list.values():
            points = points +  randint(1, dice)
        points_list.append(points)    

    # BUILD GRAPH
    fin = [possible_points.index(i) for i in points_list]
    plt.hist(fin, bins=range(max_points), align="left", color="blue", rwidth=0.8)
    plt.xticks(range(max_points), possible_points)

    plt.xlabel("Results")
    plt.ylabel("Frequency")
    plt.show()
    
if __name__ == '__main__':
    main()