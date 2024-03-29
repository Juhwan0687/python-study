from tkinter import*
from random import*

win=Tk()

win.title('Rock Scissors Paper Game')

basic_img=PhotoImage(file='ready.png')

def game(com,user):

    if user==0:
        if com==0:lb1_res['text']='Draw'
        elif com==1:lb1_res['text']='Computer wins!'
        else:lb1_res['text']='User wins!'

    elif user==1:
        if com==0:lb1_res['text']='User wins!'
        elif com==1:lb1_res['text']='Draw'
        else:lb1_res['text']='Computer wins!'

    else:
        if com==0:lb1_res['text']='Computer wins!'
        elif com==1:lb1_res['text']='User wins!'
        else:lb1_res['text']='Draw'

def change_img(user):

    list=['scissors.png','rock.png','paper.png']

    com=randint(0,2)

    com_img=PhotoImage(file=list[com])
    user_img=PhotoImage(file=list[user])

    lb1_com['image']=com_img
    lb1_com.image=com_img
    lb1_user['image']=user_img
    lb1_user.image=user_img

    game(com,user)
lb1_com=Label(win,image=basic_img,relief='solid')
lb1_user=Label(win,image=basic_img,relief='solid')

lb1_res=Label(win,text='',width=15,font=('consolas',20,'bold'),fg='brown',bg='lightyellow')

lb1_name1=Label(win,text='Computer',font=('consolas',20))
lb1_name2=Label(win,text='User',font=('consolas',20))

btn_scissors=Button(win,text='Scissors',width=15,font=('consolas',15),bg='skyblue',command=lambda : change_img(0))
btn_rock=Button(win,text='Rock',width=15,font=('consolas',15),bg='pink',command=lambda : change_img(1))
btn_paper=Button(win,text='Paper',width=15,font=('consolas',15),bg='light green',command=lambda : change_img(2))

lb1_com.grid(row=0,column=0)
lb1_res.grid(row=0,column=1)
lb1_user.grid(row=0,column=2)
lb1_name1.grid(row=1,column=0)
lb1_name2.grid(row=1,column=2)
btn_scissors.grid(row=2,column=0)
btn_rock.grid(row=2,column=1)
btn_paper.grid(row=2,column=2)

win.mainloop()