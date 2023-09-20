"""
Created by: Ernest
Created on: Sep 2023
This module is a Micro:bit MicroPython program
"""

from microbit import *

display.clear()
sleep(1)


display.scroll("A = " + str(3 * 5))


display.scroll("P = " + str(3 * 2 + 5 * 2))
