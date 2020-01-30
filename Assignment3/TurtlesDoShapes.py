# Kathryn Webb
# 1/29/2020
# This program creates two turtles.
# One turtle makes an equilateral triangle.
# The other turtle makes a hexagon.

import turtle

window = turtle.Screen()
window.bgcolor("LightBlue")
window.title("Turtles!")

alex = turtle.Turtle()
alex.pencolor("White")

bob = turtle.Turtle()

for _ in range(3):
    alex.forward(50)
    alex.left(120)

for _ in range(6):
    bob.forward(50)
    bob.left(60)

window.mainloop()
