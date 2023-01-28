import turtle
t=turtle.Turtle('turtle')
t.penup()
t.setx(200)
t.write('동',font=('Arial',30))
t.setx(-200)
t.write('서',font=('Arial',30))
t.setx(0)
t.sety(200)
t.write('북',font=('Arial',30))
t.sety(-200)
t.write('남',font=('Arial',30))
t.goto(0,0)
t.pendown()
t.pencolor('#07f2b4')
a=turtle.textinput('','방향을 입력해주세요.')
t.speed(1)
if a=='동':
    t.setx(200)
elif a=='서':
    t.setx(-200)
elif a=='북':
    t.sety(200)
elif a=='남':
    t.sety(-200)
else:
    t.right(360)
turtle.done()