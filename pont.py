import genieCivilOuvrage2D as des
from turtle import*

#tortue1 = Turtle()
#tortue2 = Turtle()
#tortue3 = Turtle()

des.figure.penup()
des.figure.setpos(-150, 0)
des.figure.pendown()
des.figure.begin_fill()
des.rectangle(75, 20, "blue", "blue")
des.figure.end_fill()

des.figure.penup()
des.figure.setpos(-137, 20)
des.figure.pendown()
des.figure.begin_fill()
des.rectangle(50, 20, "blue", "blue")
des.figure.end_fill()

des.figure.penup()
des.figure.setpos(-20, 0)
des.figure.pendown()
des.figure.begin_fill()
des.rectangle(75, 20, "blue", "blue")
des.figure.end_fill()

des.figure.penup()
des.figure.setpos(-7, 20)
des.figure.pendown()
des.figure.begin_fill()
des.rectangle(50, 20, "blue", "blue")
des.figure.end_fill()

des.figure.penup()
des.figure.setpos(-237, 40)
des.figure.pendown()
des.figure.width(2)
des.figure.goto(145, 40)

for i in range(3):
    des.demiCercle(64, "blue")
    des.figure.left(90)