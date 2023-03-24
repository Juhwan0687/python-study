from tkinter import*
win=Tk()

def message(event):
    lb1['text']=entry.get()
entry=Entry(win)
entry.bind('<Return>',message)
entry.pack()
lb1=Label(win,text='',fg='black')
lb1.pack()
win.mainloop()