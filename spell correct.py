from tkinter import *
from textblob import TextBlob

s = Tk()
s.title("Currency Converter")
s.geometry("550x320")
s['bg'] = "grey"

def clearall():
    e.delete(0,END)
    e1.delete(0,END)

def correction():
    input_word= e.get()
    blob_obj = TextBlob(input_word)
    corrected_word = str(blob_obj.correct())
    e1.insert(10,corrected_word)


a=Label(s,text="Welcome to spell corrector Application",bg="#CCFFE5",font="Digital-7 12")
a.grid(row=1,column=8,padx=185)

a1=Label(s,text="input word",bg="#99FFCC",font="Digital-7 12")
a1.place(x=15,y=90)

e=Entry(s,width="37")
e.place(x=195,y=90)

b=Button(s,text="correction",font="Digital-7 12",bg="grey",command=correction)
b.place(x=249,y=130)

a2=Label(s,text="Corrected word",bg="#99FFCC",font="Digital-7 12")
a2.place(x=15,y=190)


e1=Entry(s,width="37")
e1.place(x=195,y=190)

b2=Button(s,text="Clear",font="Digital-7 12",bg="grey",command=clearall)
b2.place(x=270,y=240)

mainloop()