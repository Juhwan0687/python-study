from tkinter import*
def click(shape):
    if shape=='circle':
        img=PhotoImage(file='circle.png')
    elif shape=='triangle':
        img=PhotoImage(file='triangle.png')
    else:
        img=PhotoImage(file='star.PNG')
    lb1['image']=img
    lb1.image=img
win=Tk()
img=PhotoImage(file='circle.png')
lb1=Label(win,image=img)
btn1=Button(win,text='Circle',command=lambda : click('circle'))
btn2=Button(win,text='Triangle',command=lambda : click('triangle'))
btn3=Button(win,text='Star',command=lambda : click('star'))
lb1.grid(row=0,column=0,columnspan=3)
btn1.grid(row=1,column=0)
btn2.grid(row=1,column=1)
btn3.grid(row=1,column=2)
win.mainloop()