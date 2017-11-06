
import turtle
from random import randint
from turtleprojectfunctions import *
turtle.colormode (255)
turtle.bgcolor (255,255,255)
turtle.tracer (0)
bob=turtle.Turtle ()

for times in range (500):
    a= randint (-800,800)
    s= randint (-800,800)
    n = randint (1,7)
    b= randint (100,255)
    r=randint (100,255)
    e=randint (100,255)

    bob.color (b,r,e)
    rainbowsnow (bob,n,a,s)

bob.width (6)

for times in range (10):
    rainbowsnowflake (bob)
    bob.left (35)
