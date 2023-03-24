from tkinter import*
win=Tk()

a=0
def message(event):
    global a
    a+=int(entry.get())
    lb1['text']=a
def click():
    global a
    a=0
    lb1['text']=a
entry=Entry(win)
entry.bind('<Return>',message)
entry.pack()
lb1=Label(win,text='',fg='black')
lb1.pack()
btn=Button(win,text='Clear',command=click)
btn.pack()
win.mainloop()