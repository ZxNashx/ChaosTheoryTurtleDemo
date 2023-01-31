import turtle
import random

colors = ["red", "white", "blue", "yellow", "green", "orange"]
sc = turtle.Screen()

sc.bgcolor("black")

class boi():
    def __init__(self, degrees, position):
        self.t = turtle.Turtle()
        self.t.hideturtle()
        self.t.color("white")
        self.t.penup()
        self.t.setposition(position)
        self.t.left(90)
        self.t.speed = 5
        self.t.shape("turtle")
        self.bounds = 200
        self.degrees = degrees

        self.t.write(str(degrees))
        self.t.forward(5)

    def setColor(self, c):
        self.t.color(c)

    def straightLine(self):
        self.t.showturtle()
        self.t.penup()
        self.t.forward(25)
        self.t.left(random.randint(-self.degrees, self.degrees))
        self.t.pendown()
        self.t.forward(2)


l = []

for i in range(1, 7):
    nt = boi(i ** 3 % 360, (100 * i - 350, -150))
    nt.setColor(colors[i - 1])
    l.append(nt)

while 1:
    for i in l:
        i.straightLine()
