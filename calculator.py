from tkinter import *
s=Tk()
s.title("screen")
s.geometry("450x430")
s['bg']="black"
e=Entry(s,width=74)
e.grid(row=1,column=1,columnspan=4)


# functioning
def click(num):
    value=e.get()
    e.delete(0,END)
    e.insert(0,str(value)+str(num))
def clear():
    e.delete(0,END)
def add():
    num=e.get()
    e.delete(0,END)
    global math
    math ="add"
    global a 
    a=int(num)

def minus():
    num1=e.get()
    e.delete(0,END)
    global math
    math="minus"
    global b 
    b=int(num1)

def multiply():
    num2=e.get()
    e.delete(0,END)
    global math
    math="mul"
    global c 
    c=int(num2)

def divide():
    num3=e.get()
    e.delete(0,END)
    global math
    math="divide"
    global d 
    d=int(num3)


def modulus():
    num4=e.get()
    e.delete(0,END)
    global math
    math="mod"
    global h 
    h=int(num4)

def equal():
    num5=e.get()
    e.delete(0,END)
    if math=="add":
        e.insert(0,a+int(num5))
    elif math=="minus":
        e.insert(0,b-int(num5))
    elif math=="mul":
        e.insert(0,c*int(num5))
    elif math=="divide":
        e.insert(0,d/int(num5))
    elif math =="mod":
        e.insert(0,h%int(num5))






# row 2
btn1=Button(s,text="1",padx=25, pady=5,bd=7,fg="black",font="airal 20 bold",command=lambda:click(1))
btn1.grid(row=3,column=1, pady=5)

btn2=Button(s,text="2",padx=25, pady=5,bd=7,fg="black",font="airal 20 bold",command=lambda:click(2))
btn2.grid(row=3,column=2, pady=5)

btn3=Button(s,text="3",padx=25, pady=5,bd=7,fg="black",font="airal 20 bold", command=lambda:click(3))
btn3.grid(row=3,column=3, pady=5)

btn4=Button(s,text="+",padx=21, pady=5,bd=7,fg="black",font="airal 20 bold",command=add)
btn4.grid(row=3,column=4, pady=5)


# row 3
btn5=Button(s,text="4",padx=25, pady=5,bd=7,fg="black",font="airal 20 bold",command=lambda:click(4))
btn5.grid(row=4,column=1, pady=5)

btn6=Button(s,text="5",padx=25, pady=5,bd=7,fg="black",font="airal 20 bold",command=lambda:click(5))
btn6.grid(row=4,column=2, pady=5)

btn7=Button(s,text="6",padx=25, pady=5,bd=7,fg="black",font="airal 20 bold",command=lambda:click(6))
btn7.grid(row=4,column=3, pady=5)

btn8=Button(s,text="-",padx=25, pady=5,bd=7,fg="black",font="airal 20 bold",command=minus)
btn8.grid(row=4,column=4, pady=5)

# row 4
btn9=Button(s,text="7",padx=25, pady=5,bd=7,fg="black",font="airal 20 bold",command=lambda:click(7))
btn9.grid(row=5,column=1, pady=5)

btn11=Button(s,text="8",padx=25, pady=5,bd=7,fg="black",font="airal 20 bold",command=lambda:click(8))
btn11.grid(row=5,column=2, pady=5)

btn12=Button(s,text="9",padx=25, pady=5,bd=7,fg="black",font="airal 20 bold",command=lambda:click(9))
btn12.grid(row=5,column=3, pady=5)

btn13=Button(s,text="x",padx=21, pady=5,bd=7,fg="black",font="airal 20 bold",command=multiply)
btn13.grid(row=5,column=4, pady=5)

# row 5
btn14=Button(s,text="%",padx=21, pady=5,bd=7,fg="black",font="airal 20 bold",command=modulus)
btn14.grid(row=6,column=1, pady=5)

btn15=Button(s,text="0",padx=25, pady=5,bd=7,fg="black",font="airal 20 bold",command=lambda:click(0))
btn15.grid(row=6,column=2, pady=5)

btn16=Button(s,text=".",padx=28, pady=5,bd=7,fg="black",font="airal 20 bold",command=lambda:click())
btn16.grid(row=6,column=3, pady=5)

btn17=Button(s,text="/",padx=25, pady=5,bd=7,fg="black",font="airal 20 bold",command=divide)
btn17.grid(row=6,column=4)

# row 6
btn18=Button(s,text="AC",padx=69, pady=5,bd=7,fg="black",font="airal 20 bold",command=lambda:click(clear))
btn18.grid(row=7,column=1,columnspan=2,)

btn20=Button(s,text="=",padx=79, pady=5,bd=7,fg="white",bg="blue",font="airal 20 bold",command=equal)
btn20.grid(row=7,column=3,columnspan=2,)

mainloop()