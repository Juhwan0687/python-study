from tkinter import*

win = Tk()
win.title('씨큐브코딩')
win.geometry=('300x200+100+100')
win.resizable(True,False)
label1=Label(win,text='One')
label2=Label(win,text='Two')
label3=Label(win,text='Three')
label1.pack()
label2.pack()
label3.pack()
win.mainloop()