from tkinter import *
root = Tk()
root.geometry("300x360")
root.title("Calculator")

root.config(background="#EAEAEA")
textin=StringVar()
operator=""
def clrbtn():
    global operator
    operator=""
    textin.set(" ")
def clickbut(number):
    global operator
    operator=operator+str(number)
    textin.set(operator)
def equlbut():
    global operator
    add = str(eval(operator))
    textin.set(add)
    operator = ''
def equlbut():
    global operator
    sub =str(eval(operator))
    textin.set(sub)
    operator= ''
def equlbut():
    global operator
    mul =str(eval(operator))
    textin.set(mul)
    operator=''
def equlbut():
    global operator
    div =str(eval(operator))
    textin.set(div)

roottext=Entry(root, font=("Courier New", 11, 'bold'), textvar=textin, width=30,  bd=10, bg='powder blue')
roottext.place(x=3,y=25)
# roottext.pack()
but7 = Button(root,  bd=2, bg='#FFFFFF',width=4,height=1, command=lambda: clickbut(7), text="7",
              font=("Courier New", 16, 'bold'))
but7.place(x=10, y=100)
but8 = Button(root, bd=2, bg='white',height=1,width=4,command=lambda: clickbut(8),text="8",
              font=("Courier New",16,'bold'))
but8.place(x=80,y=100)
but9 = Button(root,bd=2,bg='white',height=1,width=4,command=lambda: clickbut(9),text="9",font=("Courier New",16,'bold'))
but9.place(x=150,y=100)
but4 =Button(root,bd=2,bg='white',height=1,width=4,command=lambda:clickbut(4),text="4",font=("Courier New",16,'bold'))
but4.place(x=10,y=150)
but5 =Button(root,bd=2,bg='white',height=1,width=4,command=lambda:clickbut(5),text="5",font=("Courier New",16,'bold'))
but5.place(x=80,y=150)
but6 =Button(root,bd=2,bg='white',height=1,width=4,command=lambda:clickbut(6),text="6",font=("Courier New",16,'bold'))
but6.place(x=150,y=150)
but1 =Button(root,bd=2,bg='white',height=1,width=4,command=lambda:clickbut(1),text="1",font=("Courier New",16,'bold'))
but1.place(x=10,y=200)
but2 =Button(root,bd=2,bg='white',height=1,width=4,command=lambda:clickbut(2),text="2",font=("Courier New",16,'bold'))
but2.place(x=80,y=200)
but3 =Button(root,bd=2,bg='white',height=1,width=4,command=lambda:clickbut(3),text="3",font=("Courier New",16,'bold'))
but3.place(x=150,y=200)
but0 =Button(root,bd=2,bg='white',height=1,width=4,command=lambda:clickbut(0),text="0",font=("Courier New",16,'bold'))
but0.place(x=80,y=250)
butd =Button(root,bd=2,bg='white',height=1,width=4,command=lambda:clickbut("."),text=".",font=("Courier New",16,'bold'))
butd.place(x=10,y=250)
butc =Button(root,bd=2,bg='white',height=1,width=4,command=clrbtn,text="C",font=("Courier New",16,'bold'))
butc.place(x=150,y=250)
butpl=Button(root,bg='#A2A39D',bd=2,height=1,width=4,command=lambda:clickbut("+"),text="+",font=("Courier New",16,'bold'))
butpl.place(x=225,y=100)
butsb=Button(root,bg='#A2A39D',bd=2,height=1,width=4,command=lambda:clickbut("-"),text="-",font=("Courier New",16,'bold'))
butsb.place(x=225,y=150)
butml=Button(root,bg='#A2A39D',bd=2,height=1,width=4,command=lambda:clickbut("*"),text="*",font=("Courier New",16,'bold'))
butml.place(x=225,y=200)
butdv=Button(root,bg='#A2A39D',bd=2,height=1,width=4,command=lambda:clickbut("/"),text="/",font=("Courier New",16,'bold'))
butdv.place(x=225,y=250)
butequal = Button(root,  bd=2, bg='#A2A39D', command=equlbut,height=1,width=15, text="=", font=("Courier New", 16, 'bold'))
butequal.place(x=10, y=300)
root.mainloop()