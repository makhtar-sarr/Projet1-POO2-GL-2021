import genieCivilOuvrage2D as des
from turtle import*

#tortue1 = Turtle()
#tortue2 = Turtle()
#tortue3 = Turtle()

#des.figure.penup()
#des.figure.setpos(-150, 0)
#des.figure.pendown()
#des.figure.begin_fill()
#des.rectangle(75, 20, "blue", "blue")
#des.figure.end_fill()

#des.figure.penup()
#des.figure.setpos(-137, 20)
#des.figure.pendown()
#des.figure.begin_fill()
#des.rectangle(50, 20, "blue", "blue")
#des.figure.end_fill()

#des.figure.penup()
#des.figure.setpos(-20, 0)
#des.figure.pendown()
#des.figure.begin_fill()
#des.rectangle(75, 20, "blue", "blue")
#des.figure.end_fill()

#des.figure.penup()
#des.figure.setpos(-7, 20)
#des.figure.pendown()
#des.figure.begin_fill()
#des.rectangle(50, 20, "blue", "blue")
#des.figure.end_fill()

#des.figure.penup()
#des.figure.setpos(-237, 40)
#des.figure.pendown()
#des.figure.width(2)
#des.figure.goto(145, 40)

for i in range(1):
 #   des.demiCercle(64, "blue")
  #  des.figure.left(90)

#Pour la fin du pont, j'ai essayé cela

    speed(5)
    pensize(3)
    color("dodgerblue3")

    long = 217
    larg = 32
    ht()
    begin_fill()
    for i in range(2):
        forward(long)
        left(90)
        forward(larg)
        left(90)
    up()
    goto(38,larg)
    pd()
    long -= 76
    larg -=3
    for i in range(2):
        forward(long) 
        left(90)
        forward(larg)
        left(90)
    end_fill
