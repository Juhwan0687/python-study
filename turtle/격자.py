from tkinter import*
win=Tk()
c=Canvas(win,bg='white',width=500,height=500)
x=10
y1,y2=(10,460)
for i in range(10):
    c.create_line(x,y1,x,y2,fill='red',width=5)
    x+=50
x1,x2=(10,460)
y=10
for j in range(10):
    c.create_line(x1,y,x2,y,fill='blue',width=5)
    y+=50
c.pack()
win.mainloop()