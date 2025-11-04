# Turtle Artist
# Author: Thierry Narcisse
# 28 October


import turtle


# A one-of-a-kind drawing


wn = turtle.Screen()
t = turtle.Turtle()
t.shape("turtle")


t.pensize(3)
t.speed(5)
t.pencolor("orange")

# outer crust
t.pu()
t.goto(0, -260)
t.pd()
t.fillcolor("#CC5803")
t.begin_fill()
t.circle(210)
t.end_fill()
# outer outline
t.pu()
t.goto(0, -250)
t.pd()
t.fillcolor("orange")
t.begin_fill()
t.circle(200)
t.end_fill()
# inner crust
t.pu()
t.goto(0, -200)
t.pd()
t.fillcolor("#FFDA85")
t.begin_fill()
t.circle(150)
t.end_fill()

# peps
t.pu()
t.goto(5, -175)
t.pd()
t.fillcolor("#BB4430")
t.begin_fill()
t.circle(25)
t.end_fill()

t.pu()
t.goto(-85, -80)
t.pd()
t.fillcolor("#BB4430")
t.begin_fill()
t.circle(25)
t.end_fill()

t.pu()
t.goto(15, 0)
t.pd()
t.fillcolor("#BB4430")
t.begin_fill()
t.circle(25)
t.end_fill()

t.pu()
t.goto(90, -75)
t.pd()
t.fillcolor("#BB4430")
t.begin_fill()
t.circle(25)
t.end_fill()

t.pu()
t.goto(0, -75)
t.pd()
t.fillcolor("#BB4430")
t.begin_fill()
t.circle(25)
t.end_fill()

t.pu()
t.goto(-75, 10)
t.pd()
t.fillcolor("#BB4430")
t.begin_fill()
t.circle(25)
t.end_fill()

t.pu()
t.goto(-75, -150)
t.pd()
t.fillcolor("#BB4430")
t.begin_fill()
t.circle(25)
t.end_fill()

t.pu()
t.goto(75, -150)
t.pd()
t.fillcolor("#BB4430")
t.begin_fill()
t.circle(25)
t.end_fill()

t.pu()
t.goto(75, 0)
t.pd()
t.fillcolor("#BB4430")
t.begin_fill()
t.circle(25)
t.end_fill()


# slices
t.pencolor("#CC5803")
t.pensize(4)
t.penup()
t.goto(0, 0)
t.pendown()

slices = 8
slice_angle = 360 / slices

for pizza_slice in range(slices):
    t.penup()
    t.goto(0, -50)
    t.setheading(90 - pizza_slice * slice_angle)
    t.pendown()
    t.forward(200)


t.hideturtle()
wn.bgcolor("white")
wn.exitonclick()
