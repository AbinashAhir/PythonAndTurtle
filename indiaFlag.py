#import turtle
import turtle
from turtle import *

# screen for output
title("Happy Independence Day from Abinash")
screen = turtle.Screen()
turtle.setup(width=600, height=700)
# Defining a turtle Instance
t = turtle.Turtle()
speed(1)

def draw_text1(text, x, y, size, color):
    penup()
    goto(x + 100, (y * -1) - 300)
    pendown()
    pencolor(color)
    write(text, align="center", font=("Arial", size, "bold"))


# initially penup()
t.penup()
t.goto(-200, 225)
t.pendown()
# Orange Rectangle
#white rectangle
t.color("orange")
t.begin_fill()
t.forward(400)
t.right(90)
t.forward(84)
t.right(90)
t.forward(400)
t.end_fill()
t.left(90)
t.forward(84)

# Green Rectangle
t.color("green")
t.begin_fill()
t.forward(84)
t.left(90)
t.forward(400)
t.left(90)
t.forward(84)
t.end_fill()

# Big Blue Circle
t.penup()
t.goto(35, 100)
t.pendown()
t.color("navy")
t.begin_fill()
t.circle(35)
t.end_fill()

# Big White Circle
t.penup()
t.goto(30, 100)
t.pendown()
t.color("white")
t.begin_fill()
t.circle(30)
t.end_fill()

#Mini Blue Circles of Flag
t.penup()
t.goto(-27, 96)
t.pendown()
t.color("navy")
for i in range(24):
    t.begin_fill()
    t.circle(2)
    t.end_fill()
    t.penup()
    t.forward(7)
    t.right(15)
    t.pendown()

# Small Blue Circle
t.color("navy")
t.penup()
t.goto(10, 100)
t.pendown()
t.begin_fill()
t.circle(10)
t.end_fill()

#The spokes of India Flag
t.penup()
t.goto(0, 100)
t.pendown()
t.pensize(1)
for i in range(24):
    t.forward(30)
    t.backward(30)
    t.left(15)



#for stick of the flag
t.color("Brown")
t.pensize(10)
t.penup()
t.goto(-200,225)
t.right(180)
t.pendown()
t.forward(800)

draw_text1("Happy Independence Day!", 0, -150, 16, "green")

#to hold the
#output window
turtle.done()
