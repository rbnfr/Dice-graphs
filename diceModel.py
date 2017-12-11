# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 00:23:03 2017

@author: RBN
"""

from random import randint

class dice(object):
    faces = ""
    def __init__(self, faces):
        self.faces = faces

    def roll(self):
        return randint(1, self.faces)
    