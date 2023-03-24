from tkinter import*
win=Tk()

def click():
    if lb1['text']=='python':
        lb1['text']='Hello'
        lb1['bg']='orange'
    else:
        lb1['text']='python'
        lb1['bg']='green'
btn=Button(win,text='Button',command=click)
lb1=Label(win,text='Hello',bg='orange',fg='white')
lb1.pack()
btn.pack()
win.mainloop()