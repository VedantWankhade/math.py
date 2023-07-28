from turtle import *


def square(sidelength=100):
    for i in range(4):
        forward(sidelength)
        right(90)


def triangle(sidelength=100):
    for i in range(3):
        forward(sidelength)
        right(120)

def polygon(sidelength=100, sides=5):
    for i in range(sides):
        forward(sidelength)
        right(180 - ((sides - 2) * 180) / sides)


def star(sidelength=100):
    for i in range(5):
        forward(sidelength)
        right(180 - 180/5)

#star()

shape('turtle')
speed(0)

#length = 50
#for i in range(4):
#    polygon(length, 7)
#    length += 50

length = 5
inc = 5
rot = 5

#for i in range(60):
#    polygon(length, 4)
#    length += inc
#    right(5)


for i in range(60):
    star(length)
    length += inc
    right(rot)
