# -*- coding: utf-8 -*-

"""
Author: Ruben
"""


def main():
    """ Main method """
    import matplotlib.pyplot as plt
    import diceController
    import histController
    import operator
    import pprint

    # PROGRAM VARIABLES
    points_list = []
    min_points = 0
    max_points = 0
    points_freq = {}
    iterations = 10
    sumFreq = 0
    debugPrint = False
    pp = pprint.PrettyPrinter(indent = 4)

    rolls = 10000
    dice_list = {
        'D20'  : 20,
        'D20_2': 20
        }
    
    # USER VARIABLES
    for i in range(iterations):
        try:
            # HISTOGRAM RANGE
            min_points = histController.minPoints(dice_list)
            max_points = histController.maxPoints(dice_list)
            possible_points = range(min_points, max_points + 1)
    
            # GET DATA
            points_list = diceController.doRolls(dice_list, rolls)
            points_freq = diceController.storeFrequency(possible_points, points_list)
    
            # BUILD GRAPH
            fin = [possible_points.index(i) for i in points_list]
            plt.hist(fin, bins=range(max_points), align="left", color="blue", rwidth=0.8)
            plt.xticks(range(max_points-1), possible_points)
            plt.xlabel("Results")
            plt.ylabel("Frequency")
            highFreq = max(points_freq.items(), key=operator.itemgetter(1))[0]
            sumFreq += highFreq
            
        except (KeyboardInterrupt, SystemExit):
            raise
    
    if debugPrint:
        print("Frequencies:")
        pp.pprint(points_freq)
        print("")
        print("High freq:", highFreq)
        print("")
        
        
    plt.show()    
    averageFreq = (sumFreq/iterations)
    print("Average Freq:", averageFreq)

if __name__ == '__main__':
    main()
