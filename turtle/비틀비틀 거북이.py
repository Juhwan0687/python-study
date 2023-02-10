import turtle
from random import*

i=1
t=turtle.Turtle('turtle')
while i<=30:
    dist=randint(1,100)
    ang=randint(-180,180)
    t.forward(dist)
    t.right(ang)
    i+=1
turtle.done()