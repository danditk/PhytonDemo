from turtle import *

# import turtle library
import turtle
my_window = turtle.Screen()
my_window.bgcolor("blue")       # creates a graphics window
my_pen = turtle.Turtle()
my_pen.forward(150)
my_pen.left(90)
my_pen.forward(75)
my_pen.color("white")
my_pen.pensize(12)

shape("turtle")
color("green")
speed(5)

forward(200)
right(270)
forward(200)
right(270)
forward(200)
right(270)
forward(200)
right(270)

circle(100)

speed(8)
# import turtle library
import turtle
colors = [ "red","purple","blue","green","orange","yellow"]
my_pen = turtle.Pen()
turtle.bgcolor("black")
for x in range(360):
   my_pen.pencolor(colors[x % 6])
   my_pen.width(x/100 + 1)
   my_pen.forward(x)
   my_pen.left(59)

done()