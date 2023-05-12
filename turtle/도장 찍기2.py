from tkinter import*

def draw_shape(event):
    x1,y1=event.x-25,event.y-25
    x2,y2=event.x+25,event.y+25
    canvas.create_oval(x1,y1,x2,y2,outline='black')

win=Tk()
canvas=Canvas(win,height=300,width=300)
canvas.pack()

canvas.bind('<Double-Button-1>',draw_shape)

win.mainloop()