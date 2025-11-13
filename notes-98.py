# thierry N

import random

import turtle

window = turtle.Screen()  # Set up the window and its attributes
window.bgcolor("lightgreen")

# TMNT - turtles
mikey = turtle.Turtle()

mikey.turtlesize(0.5)
mikey.color("yellow")
mikey.shape("circle")
mikey.setheading(0)
mikey.color("yellow")
mikey.pu()
mikey.goto(-5, -30)
mikey.pd()
mikey.circle(30)
mikey.pu()
mikey.goto(-10, 10)
mikey.stamp()
mikey.goto(10, -10)
mikey.stamp()
mikey.goto(-2, 4)

for _ in range(1000):
    x = random.randrange(-700, 701)
    y = random.randrange(700, 700)
window.exitonclick()
