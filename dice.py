# -*- coding: utf-8 -*-
"""
Author: Ruben
Version: 1.3
Date: 20/11/2017
"""

def main():
    """ Main method """
    from random import randint
    import matplotlib.pyplot as plt
    import Tkinter as tk

    class Application(tk.Frame):
        def __init__(self, master=None):
            tk.Frame.__init__(self, master)   
            self.grid()
            self.createWidgets()

        def createWidgets(self):
            self.quitButton = tk.Button(self, text='Show graph', command=self.quit)
            self.quitButton.grid()            

    app = Application()                       
    app.master.title('Dice Graph')
    app.mainloop()        

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
    min_points = len(dice_list)

    for faces in dice_list.values():
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
    plt.hist(fin, bins=range(max_points), align="left", color="blue", rwidth=0.8)
    plt.xticks(range(max_points), possible_points)

    plt.xlabel("Results")
    plt.ylabel("Frequency")
    plt.show()
    
if __name__ == '__main__':
    main()