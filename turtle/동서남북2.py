import turtle
t=turtle.Turtle('turtle')
t.penup()
t.setx(200)
t.write('동', font=('Arial',10))
t.setx(-200)
t.write('서', font=('Arial',10))
t.setx(0)
t.sety(-200)
t.write('남', font=('Arial',10))
t.sety(200)
t.write('북', font=('Arial',10))
t.goto(0,0)
t.pendown()
t.pencolor('blue')
a=turtle.textinput(' ', '방향을 입력해주세요:')
t.speed(1)
if a=='동':
    t.setx(200)
elif a=='서':
    t.setx(-200)
elif a=='남':
    t.sety(-200)
elif a=='북':
    t.sety(200)
turtle.done()