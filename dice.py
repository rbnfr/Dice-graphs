# -*- coding: utf-8 -*-
"""
Author: Ruben
"""

def main():
    """ Main method """
    from random import randint
    import matplotlib.pyplot as plt
    import diceController
    import histController

    # PROGRAM VARIABLES
    points = 0
    points_list = []
    max_points = 0
 
    # USER VARIABLES
    rolls = 1000
    dice_list = {
        'D6'  : 6, 
        'D6_2': 6
        }
 
    # HISTOGRAM RANGE
    min_points = histController.minPoints(dice_list)
    max_points = histController.maxPoints(dice_list) 
    possible_points = range(min_points,max_points+1)
 
    # GET DATA
    points_list = diceController.doRolls(dice_list, rolls)
 
    # BUILD GRAPH
    fin = [possible_points.index(i) for i in points_list]
    plt.hist(fin, bins=range(max_points), align="left", color="blue", rwidth=0.8)
    plt.xticks(range(max_points), possible_points)
 
    plt.xlabel("Results")
    plt.ylabel("Frequency")
    plt.show()
    
if __name__ == '__main__':
    main()
