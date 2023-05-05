from tkinter import*
win=Tk()
c=Canvas(win,bg='white',width=500,height=500)
c.create_line(250,0,250,300,fill='red',width=5)
c.pack()
win.mainloop()