# Wilson Toni
# 10-28-2024
# P4LAB1
# While Loop to Make a Square and For Loop to Make a Triangle Using Turtle

# Import turtle library to use in code
import turtle

# Set up the window and turtle object
window = turtle.Screen()
tiny_tim = turtle.Turtle()

tiny_tim.pensize(4)
tiny_tim.pencolor("purple")
tiny_tim.shape("turtle")

# While loop to draw 4sides of square
line = 0
while line < 4:
    tiny_tim.right(90)
    tiny_tim.forward(150)
    line += 1

# For loop to draw 3sides of triangle
for line1 in range(3):
    tiny_tim.left(120)
    tiny_tim.forward(150)
