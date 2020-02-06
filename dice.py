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

    # PROGRAM VARIABLES
    points_list = []
    min_points = 0
    max_points = 0
    points_freq = {}

    # USER VARIABLES
    rolls = 500
    dice_list = {
        'D6': 6,
        'D6_2': 6
    }

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
        plt.xticks(range(max_points), possible_points)
        plt.xlabel("Results")
        plt.ylabel("Frequency")
        print("Frequencies:", points_freq)
        print("High freq:", max(points_freq.items(), key=operator.itemgetter(1))[0])
        plt.show()
    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        print("I refuse to work in this conditions.")


if __name__ == '__main__':
    main()
