# -*- coding: utf-8 -*-
from dataclasses import dataclass
import unittest
import diceController
import histController

@dataclass(init=False)
class TestDice(unittest.TestCase):

    def setUp(self):
        self.dice_list = {'D6':6, 'D6_2':6}
        self.rolls = 100
        self.points_list = [1, 2, 3, 4, 5]

    def test_roll(self):
        result = diceController.roll(6)
        self.assertIsInstance(result, int)

    def test_dorolls(self):
        result = diceController.doRolls(self.dice_list, self.rolls)
        self.assertIsInstance(result, list)

    def test_storeFrequency(self):
        result = diceController.storeFrequency(range(20), self.points_list)
        self.assertIsInstance(result, dict)
    
@dataclass(init = False)
class TestHistogram(unittest.TestCase):

    def setUp(self):
        self.dice_list = {'D6':6, 'D6_2':6}

    def test_maxpoints(self):
        result = histController.maxPoints(self.dice_list)
        self.assertIsInstance(result, int)
    
    def test_minPoints(self):
        result = histController.minPoints(self.dice_list)
        self.assertIsInstance(result, int)

if __name__ == "__main__":
    unittest.main()


