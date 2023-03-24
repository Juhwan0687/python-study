from tkinter import*

win = Tk()
win.title('씨큐브코딩')
win.geometry=('300x200+100+100')
win.resizable(True,False)
list=['info','warning','error','question','questhead','hourglass','gray12','gray25','gray50','gray75']
for i in range(10):
    lb1=Label(win,bitmap=list[i])
    lb1.pack(side='left')
win.mainloop()