import turtle
t=turtle.Turtle()
s='즐거운 씨큐브 코딩'
n=turtle.numinput(s, '앞으로 얼마나 이동할까요?')
t.forward(n)
ang=turtle.numinput(s, '오른쪽으로 얼마나 회전할까요? : ', default=0,minval=0,
maxval=360)
t.right(ang)
n=turtle.numinput(s, '앞으로 얼마나 이동할까요?')
t.forward(n)
turtle.done()