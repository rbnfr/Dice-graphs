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
    rolls = 1000
    dice_list = {
        'D6'  : 20, 
        'D6_2': 20
        }    

    # HISTOGRAM RANGE
    min_points = len(dice_list)
    index = 0

    for faces in dice_list.values():
        if faces < 4:
            print("Invalid faces at dice " + str(index) + ", are you a fucking retard?")
            index+=1

        max_points += faces

    possible_points = range(min_points,max_points+1)

    # GET DATA
    for i in range(rolls):
        points = 0
        for dice in dice_list.values():
            points += randint(1, dice)
        points_list.append(points)    

    # BUILD GRAPH
    fin = [possible_points.index(i) for i in points_list]
    hist = plt.hist(fin, bins=range(max_points), align="left", color="blue", rwidth=0.8)
    for i in range(max_points-1):
        plt.text(
            x = hist[1][i], 
            y = hist[0][i], 
            s = int(hist[0][i]),
            fontweight = 'bold',
            backgroundcolor = 'grey',
            horizontalalignment = 'center'

            )


    
    plt.xticks(range(max_points), possible_points)

    plt.xlabel("Results")
    plt.ylabel("Frequency")
    plt.show()
    
if __name__ == '__main__':
    main()