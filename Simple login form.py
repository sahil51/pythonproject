from tkinter import *
import mysql.connector as ms
from tkinter import messagebox
from tkinter.colorchooser import *

s = Tk()
s.title("Data Store")
s.geometry("550x320")
s['bg'] = "#0e2222"

def conn():
    Id=e3.get()
    Name=e.get()
    Age=e1.get()

    if Name=="" or Age=="":
        messagebox.showerror("Error","All fields are required")
    else:
        con=ms.connect(host="localhost",user="root",password="sahil7070",database="d1")
        cur=con.cursor()
        sql="insert into tnl1(Id,name,age) Values(%s,%s,%s)"
        val=(Id,Name,Age)
        cur.execute(sql,val)
        con.commit()
        cur.close()
        con.close()
        messagebox.showinfo("Success","Record has been inserted")

def deleterow():
    Id=e3.get()
    if Id == "":
        messagebox.showerror("Error","Id is required")
    else:
        con=ms.connect(host="localhost", user="root", password="sahil7070", database="d1")
        sql = "DELETE FROM tnl1 WHERE Id=%s;"
    # sql = "DELETE FROM tnl1 WHERE Id=%s;
        cur = con.cursor()  
        val=(Id,)
        cur.execute(sql, val) 
        con.commit()
        cur.close()
        con.close()
        messagebox.showinfo("Success", "Rows have been deleted")




def clearall():
    e.delete(0,END)
    e1.delete(0,END)
    e3.delete(0,END)
 
def show():
   nm= askcolor()
   print(nm)

a11=Label(s,text="Welcome to Login",bg="#0e2222",fg="white",font="cursive")
a11.place(x=220)


a3=Label(s,text="ID",bg="#0e2222",fg="white",font="Digital-7 12")
a3.place(x=105,y=60)

e3=Entry(s,width="37")
e3.place(x=195,y=60)

a1=Label(s,text="Name",bg="#0e2222",fg="white",font="Digital-7 12")
a1.place(x=105,y=90)

e=Entry(s,width="37")
e.place(x=195,y=90)

a2=Label(s,text="Age",bg="#0e2222",fg="white",font="Digital-7 12")
a2.place(x=105,y=120)


e1=Entry(s,width="37")
e1.place(x=195,y=120)


b2=Button(s,text="Submit",font="Digital-7 12",bg="grey",padx=23,background="#30abaa",activebackground="#0c2b2b",foreground="black",activeforeground="white",bd=7,command=conn)
b2.place(x=196,y=155)

b2=Button(s,text="Clear",font="Digital-7 12",bg="grey",background="#30abaa",activebackground="#0c2b2b",foreground="black",activeforeground="white",bd=2,command=clearall)
b2.place(x=496,y=294)

b= Button(s,text='click here', command=show)
b.place(x=0, y=294)

b4=Button(s,text="Delete Data",font="Digital-7 12",bg="grey",padx=0,background="#30abaa",activebackground="#0c2b2b",foreground="black",activeforeground="white",bd=7,command=deleterow)
b4.place(x=318,y=155)

mainloop()  