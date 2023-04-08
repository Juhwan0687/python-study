from tkinter import*
from tkinter import messagebox

def save(x):
    file_name=entry.get()
    if x==0:
        data=txt.get(1.0,END)
        f=open('%s.txt'%file_name,'w')
        f.write(data)

        messagebox.showinfo('Save','Save Complete')
    else:
        f=open('%s.txt'%file_name,'r+')
        txt.insert(1.0,data)
        entry['text']=file_name

        messagebox.showinfo('Open','Open Complete')
def clear():

    txt.delete(1.0,END)

    entry.delete(0,END)

    ans=messagebox.showinfo('Clear','Delete Complete')

win=Tk()
win.title('My Notepad')
win.geometry('300x320')

lb1=Label(win,text='File name : ')
entry=Entry(win,width=70)
txt=Text(win)
btn_save=Button(win,text='Save',command=lambda:save(0))
btn_clear=Button(win,text='Clear',command=lambda:clear())
btn_open=Button(win,text='Open',command=lambda:save(1))

txt.grid(row=0,column=0,columnspan=3)
lb1.grid(row=1,column=0)
entry.grid(row=1,column=1)
btn_save.grid(row=2,column=0)
btn_clear.grid(row=2,column=2)
btn_open.grid(row=2,column=1)

win.mainloop()