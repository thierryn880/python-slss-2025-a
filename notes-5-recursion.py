# Thierry Narcisse
# Oct 20, 2025
# Recursive tree drawing using turtle

import turtle

# Create a turtle named mike
mike = turtle.Turtle()


# dictionary to hold colors
LEAF_COLORS = {
    "melon": "#F7A9A8",
    "summer": "#C1CC99",
    "winter": "#E2E7F4",
    "fall": "#BB4D00",
}


def draw_tree(level: int, branch_length: float):
    """A recursive function to draw trees.
    level  the levels of branches
    branch_length  length of branch to draw"""

    # : if level is 0, stamp a leaf and return
    if level == 0:
        mike.color(LEAF_COLORS["melon"])
        mike.stamp()
        mike.color("brown")
        return

    # Recursive case
    mike.forward(branch_length)
    mike.left(37)
    draw_tree(level - 1, branch_length * 0.8)
    mike.right(74)
    draw_tree(level - 1, branch_length * 0.8)
    mike.left(37)
    mike.backward(branch_length)


def factorial(num: int) -> int:
    """Returns the factorial of a given num
    calculated recusrively"""
    if num > 1:
        return num * factorial(num - 1)
    else:
        return 1


def fibonacci(num: int) -> int:
    """Returns the nth fibonacci number
    and calculates recursively"""
    # if the number is greater than 2
    # return fibonacci(num - 1) + fibonacci(num - 2)
    # else
    # return 1


# Set up the turtle
mike.left(90)
mike.color("brown")
mike.pensize(5)
mike.shape("turtle")
mike.penup()
mike.goto(0, -180)
mike.pendown()

# draw_complicated_tree(5, 128)
print(factorial(3))  # 6
print(factorial(4))  # 24
print(factorial(100))  #

print(fibonacci(5))
print(fibonacci(1000))


# Setup screen
wn = turtle.Screen()
wn.bgcolor("lightblue")

# Start drawing
draw_tree(5, 180)

# Wait for click to close
wn.exitonclick()
