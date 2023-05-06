"""
# Counters.py
# A collection of different kinds of counters that might be used for
# various projects
# Author: Arijit Sengupta
"""

from Displays import *
from Button import *
import time

class Counter:
    """
    Counter base class - provides an internal count, an initiailzer and a reset method
    everything else should be defined at subclass level
    """
    
    def __init__(self):
        print("Counter: constructor")
        self._number = 0
        self._display= LCDDisplay (sda=20, scl = 21, i2cid=0)
        self._greenButton = Button(17, "increase", buttonhandler=self, lowActive=True)
        self._redButton = Button(16, "reset", buttonhandler=self, lowActive=True)

    def increment(self):
            print("Counter: incrementing")
            self._number = self._number + 1

    def reset(self):
        print("Counter: resetting")
        self._number = 0

    def buttonPressed(self, name):
        if name == "increase":
            self.increment()
            elif name == "reset":
                self.reset()

    def buttonReleased(self, name):
        pass

    def show(self)
        while True:
            self.display.showNumber(self._number)
            time.sleep(0.1)
    

