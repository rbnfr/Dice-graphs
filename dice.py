# -*- coding: utf-8 -*-

"""
Author: Ruben
"""
from typing import Text
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import PySimpleGUI as sg
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import diceController
import histController
import operator
import pprint
import PySimpleGUI as sg 

def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side="top", fill="both", expand=1)

    return figure_canvas_agg

def clearGraph(canvas):
    canvas.get_tk_widget().forget()
    # plt.close('all')
    # for graph in canvas.get_tk_widget().find_all():
    #     canvas.get_tk_widget().delete(graph)


def rollDices(diceList, rolls)-> None:
    # PROGRAM VARIABLES
    points_list = []
    min_points = 0
    max_points = 0
    points_freq = {}
    iterations = 10
    sumFreq = 0
    debugPrint = False
    pp = pprint.PrettyPrinter(indent = 4)

    dice_list = {
        'D3'  : 6,
        'D20_2': 6
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
    
    # plt.show()    
    averageFreq = (sumFreq/iterations)
    print("Average Freq:", averageFreq)

def main():
    """ Main method """

    dices = ['D3', 'D4', 'D6', 'D8', 'D10', 'D12', 'D20']
    
    layoutPlot = [
        [sg.Text("Frequency")],
        [sg.Canvas(key = "-CANVAS-", pad = (5,5))],
        [sg.Button("Ok")]
    ]
    
    layoutSettings = [
        [sg.Text("Settings")],
        [sg.HSeparator()],
        [
            sg.Text("D3"),  sg.Input(default_text = 0, key = "-D3 NUMBER-",  size = (2,2)),
            sg.Text("D4"),  sg.Input(default_text = 0, key = "-D4 NUMBER-",  size = (2,2)),
            sg.Text("D6"),  sg.Input(default_text = 0, key = "-D6 NUMBER-",  size = (2,2)),
            sg.Text("D8"),  sg.Input(default_text = 0, key = "-D8 NUMBER-",  size = (2,2)),
            sg.Text("D10"), sg.Input(default_text = 0, key = "-D10 NUMBER-", size = (2,2)),
            sg.Text("D12"), sg.Input(default_text = 0, key = "-D12 NUMBER-", size = (2,2)),
            sg.Text("D20"), sg.Input(default_text = 0, key = "-D20 NUMBER-", size = (2,2))
        ],
        [sg.Slider(range = (5,1000), default_value = 100, orientation = 'h', resolution = 5, key = "-SLIDER-")],
        [sg.Button("Roll")]
    ]

    layout = [
        [
            sg.Column(layoutSettings, expand_x = True, expand_y = True),
            sg.VSeparator(),
            sg.Column(layoutPlot)
        ]
    ]

    # Create the form and show without the plot
    window = sg.Window(
        "Frequency graph",
        layout = layout,
        location = (0, 0),
        finalize = True,
        element_justification = "center",
        font = "Helvetica 18",
        resizable = True
    )   

    # fig = plt.gcf()
    
    # Add the plot to the window
    # draw_figure(window["-CANVAS-"].TKCanvas, fig)
    while True:
        event, values = window.read()

        dice_list = {
            'D3'  : values['-D3 NUMBER-'],
            'D4'  : values['-D4 NUMBER-'],
            'D6'  : values['-D6 NUMBER-'],
            'D8'  : values['-D8 NUMBER-'],
            'D10' : values['-D10 NUMBER-'],
            'D12' : values['-D12 NUMBER-'],
            'D20' : values['-D20 NUMBER-']
        }

        rolls = int(values['-SLIDER-'])

        if event == 'Roll':
            fig = plt.gcf()
            # clearGraph(FigureCanvasTkAgg(fig,window["-CANVAS-"].TKCanvas))
            draw_figure(window["-CANVAS-"].TKCanvas, fig)
            rollDices(dice_list, rolls)

        if event == 'Ok' or event == sg.WIN_CLOSED:
            break


if __name__ == '__main__':
    main()
