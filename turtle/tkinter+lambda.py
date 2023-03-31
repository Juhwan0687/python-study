from tkinter import*
def click(n):
    if n==1:
        lb1['text']='First button clicked.'
    elif n==2:
        lb1['text']='Second button clicked.'
    else:
        lb1['text']='Third button clicked.'
win=Tk()
lb1=Label(win,text='이름')

btn1=Button(win,text='First',command=lambda:click(1))
btn2=Button(win,text='Second',command=lambda:click(2))
btn3=Button(win,text='Third',command=lambda:click(3))

lb1.grid(row=0,column=0,columnspan=3)
btn1.grid(row=1,column=0)
btn2.grid(row=1,column=1)
btn3.grid(row=1,column=2)
win.mainloop()