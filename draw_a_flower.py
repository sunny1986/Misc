#############################################################################
#
# Description:
# This program lets you explore Python's turtle graphics module
# and draw a 2-color flower using some functions from turtle
#
# Steps:
# #1 Background window/canvas definition
# #2 Define an instance of class Turtle
# #3 Set color based on changing heading 0-360 deg. Alternate color flower petals
# #4 Draw a petal
# #5 Set heading for the instance and move to a new spot for the next petal
#
############################################################################

import turtle

def draw_flower():

    #1
    # Define properties of the window on which flower will be drawn
    window = turtle.Screen()
    window.bgcolor("black")

    #2
    # Define an instance of class turtle
    brad = turtle.Turtle()    
    
    for heading in range (0,360,5):

        #3
        if heading%2 == 0:
            brad.color("red")
        else:
            brad.color("yellow")

        #4 
        for x in range(0,2):
          brad.forward(10)
          brad.right(90)
          brad.forward(100)
          brad.right(90)

        #5
        brad.setheading(heading)
        brad.forward(2)
        brad.speed(10)

    # Exit the window on click after drawing the flower
    window.exitonclick()

draw_flower()
