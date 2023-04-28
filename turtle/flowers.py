from tkinter import*
win=Tk()
def double_click(event):
    index=listbox.curselection()
    lb1['text']=flowers[index[0]]
flowers=['Rose','Lily','Pansy','Sunflower']
lb1=Label(win,text='',bg='lightpink')
listbox=Listbox(win)
for i in range(4):
    listbox.insert(i,flowers[i])
lb1.pack()
listbox.bind('<Double-Button-1>',double_click)
listbox.pack()
win.mainloop()