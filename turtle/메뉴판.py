from tkinter import*
win=Tk()
win.title('메뉴')
img=PhotoImage(file='피자.png')
lb1=Label(win,image=img)
lb2=Label(win,text='Pizza',bg='yellow')
lb1.pack()
lb2.pack()
win.mainloop()