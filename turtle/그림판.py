from tkinter import*

pen_color='black'
width=2

def paint(event):
    global pen_color
    x1,y1=event.x,event.y
    x2,y2=x1+5,y1+5
    c.create_line(x1,y1,x2,y2,width=width,fill=pen_color)

def change_color(color):
    global pen_color
    pen_color=color
    
def change_width(event):
    global width
    if event=='+':
        width+=1
    else:
        width-=1

    if width<1:
        width=1

win=Tk()
c=Canvas(win,bg='white',width=500,height=500)

white_btn=Button(win,text='White',bg='white',command=lambda:change_color('white'))
black_btn=Button(win,text='Black',bg='black',fg='white',command=lambda:change_color('black'))
blue_btn=Button(win,text='Blue',bg='blue',fg='white',command=lambda:change_color('blue'))
green_btn=Button(win,text='Green',bg='Green',fg='white',command=lambda:change_color('green'))
yellow_btn=Button(win,text='Yellow',bg='yellow',command=lambda:change_color('yellow'))
red_btn=Button(win,text='Red',bg='red',command=lambda:change_color('red'))
plus_btn=Button(win,text='+',command=lambda:change_width('+'))
minus_btn=Button(win,text='-',command=lambda:change_width('-'))
clear_btn=Button(win,text='Clear',command=lambda:c.delete('all'))

c.grid(row=0,column=0,columnspan=9)

white_btn.grid(row=1,column=0)
black_btn.grid(row=1,column=1)
blue_btn.grid(row=1,column=2)
green_btn.grid(row=1,column=3)
yellow_btn.grid(row=1,column=4)
red_btn.grid(row=1,column=5)
plus_btn.grid(row=1,column=6)
minus_btn.grid(row=1,column=7)
clear_btn.grid(row=1,column=8)

win.bind('<B1-Motion>',paint)

win.mainloop()