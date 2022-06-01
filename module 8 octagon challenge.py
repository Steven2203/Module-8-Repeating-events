#-------------------------------------------------------------------------------
# Name:        module 8 - Understand repeating events.
# Purpose:     Using the turtle module, draw an octagon.
# Author:      Steven
# Created:     26-05-2022
# Copyright:   (c) Steven 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

##Importing the turtle module.
import turtle as tl

tl.title("Polygon / Object creater with turtle")
textInput = input("How manny sides does the object have?")
textInput = int(textInput)

for steps in range(textInput):
    tl.bgcolor("grey")
    tl.color("Blue")
    tl.forward(100)
    tl.right(360 / textInput)

##Using the turtle functions available to draw an octagon manually.

"""
tl.color('blue')
tl.right(45)
tl.forward(30)
tl.right(45)
tl.forward(30)
tl.right(45)
tl.forward(30)
tl.right(45)
tl.forward(30)
tl.right(45)
tl.forward(30)
tl.right(45)
tl.forward(30)
tl.right(45)
tl.forward(30)
tl.right(45)
tl.forward(30)
"""
##Using a loop to print a single blue octagon.

"""
for steps in range(8):
    tl.bgcolor('grey')
    tl.color('blue')
    tl.forward(30)
    tl.right(45)
"""



