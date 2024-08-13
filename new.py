from tkinter import *
from tkinter import ttk
import mysql.connector as lg
from tkinter import messagebox
from tkinter import simpledialog

s = Tk()
s.title("Student Database Management System")
s.geometry("1024x512")
s['bg'] = "#00d2d2"

# mysql connection
def conn():
    Student_ID = e.get()
    First_Name = e1.get()
    Sur_Name = e2.get()
    Dob = e3.get()
    Age = e4.get()
    Gender = gendermf.get()
    Address = e6.get()
    Mobile = e7.get()

    if Student_ID == "" or First_Name == "" or Sur_Name == "" or Dob == "" or Age == "" or Gender == "" or Address == "" or Mobile == "":
        messagebox.showerror("Error", "All fields are required")
    else:
        con = lg.connect(host="localhost", user="root", password="sahil7070", database="student")
        cur = con.cursor()
        sql = "insert into tb1(Student_ID, First_Name, Sur_Name, Dob, Age, Gender, Address, Mobile) Values(%s, %s, %s, %s, %s, %s, %s, %s)"
        val = (Student_ID, First_Name, Sur_Name, Dob, Age, Gender, Address, Mobile)
        cur.execute(sql, val)
        con.commit()
        cur.close()
        con.close()
        messagebox.showinfo("Success", "Record has been inserted")

        # Display submitted data in "Student Details" box
        details_box = Label(s, text=f"Student ID: {Student_ID}\nFirst Name: {First_Name}\nSurname: {Sur_Name}\nDate of Birth: {Dob}\nAge: {Age}\nGender: {Gender}\nAddress: {Address}\nMobile: {Mobile}", font="arial 12", bg="lightgrey")
        details_box.place(x=720, y=190)

        # Clear all input boxes and details box
        clearall()

# delete data
def deleterow():
    Student_ID = e.get()
    if Student_ID == "":
        messagebox.showerror("Error","Id is required")
    else:
        con=lg.connect(host="localhost", user="root", password="sahil7070", database="student")
        cur = con.cursor()
        sql = "DELETE FROM tb1 WHERE Student_ID=%s;"
        val=(Student_ID,)
        cur.execute(sql, val)
        con.commit()
        cur.close()
        con.close()
        messagebox.showinfo("Success", "Rows have been deleted")

# add new
def clearall():
    e.delete(0,END)
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e6.delete(0,END)
    e7.delete(0,END)
    details_box = Label(s, text="", font="arial 12", bg="lightgrey")
    details_box.place(x=720, y=190)

# display data
def dd():
    con = lg.connect(host="localhost", user="root", password="sahil7070", database="student")
    cur = con.cursor()
    cur.execute("SELECT * FROM tb1")
    rows = cur.fetchall()
    data = ""  
    for row in rows:
        data += f"Student ID: {row[0]}\n"
        data += f"First Name: {row[1]}\n"
        data += f"Surname: {row[2]}\n"
        data += f"Date of Birth: {row[3]}\n"
        data += f"Age: {row[4]}\n"
        data += f"Gender: {row[5]}\n"
        data += f"Address: {row[6]}\n"
        data += f"Mobile: {row[7]}\n\n"
    con.close()
    messagebox.showinfo("Display Data", data)

# Search button command
def ss():
    searchid = simpledialog.askstring("Find Student", "Enter Student ID")
    if searchid is not None:
        con = lg.connect(host="localhost", user="root", password="sahil7070", database="student")
        cur = con.cursor()
        cur.execute("SELECT * FROM tb1 WHERE Student_ID = %s", (searchid,))
        rows = cur.fetchall()
        if rows:
            for row in rows:
                e.delete(0, END)
                e.insert(0, row[0])
                e1.delete(0, END)
                e1.insert(0, row[1])
                e2.delete(0, END)
                e2.insert(0, row[2])
                e3.delete(0, END)





 #  update button command
def ud():
    searchid = simpledialog.askstring("Update Student", "Enter Student ID")
    if searchid is not None:
        con = lg.connect(host="localhost", user="root", password="sahil7070", database="student")
        cur = con.cursor()
        cur.execute("SELECT * FROM tb1 WHERE Student_ID = %s", (searchid,))
        rows = cur.fetchall()
        if rows:
            for row in rows:
                e.delete(0, END)
                e.insert(0, row[0])
                e1.delete(0, END)
                e1.insert(0, row[1])
                e2.delete(0, END)
                e2.insert(0, row[2])
                e3.delete(0, END)
                e3.insert(0, row[3])
                e4.delete(0, END)
                e4.insert(0, row[4])
                gendermf.set(row[5])
                e6.delete(0, END)
                e6.insert(0, row[6])
                e7.delete(0, END)
                e7.insert(0, row[7])
            update_details = simpledialog.askstring("Update Student", "Enter new details (comma separated: First Name, Surname, Date of Birth, Age, Gender, Address, Mobile)")
            if update_details is not None:
                update_details_list = update_details.split(',')
                sql = "UPDATE tb1 SET First_Name = %s, Sur_Name = %s, Dob = %s, Age = %s, Gender = %s, Address = %s, Mobile = %s WHERE Student_ID = %s"
                val = (update_details_list[0].strip(), update_details_list[1].strip(), update_details_list[2].strip(), update_details_list[3].strip(), update_details_list[4].strip(), update_details_list[5].strip(), update_details_list[6].strip(), searchid)
                cur.execute(sql, val)
                con.commit()
                conn.close()
               
    
              
                conn.close()
                messagebox.showinfo("Success", "Student details updated successfully")
        else:
            messagebox.showinfo("Record not Found", "No student found with the given ID")
    
# header
h = Label(s,text="Student Database Management System",font="arial 40 bold",borderwidth=4,bg="lightgrey",highlightbackground="black",highlightthickness=3)
h.place(x=15,y=5)

# infobox
frm=Frame(s,width=1000,height=300,bg="lightgrey",bd=30,highlightbackground="black",highlightthickness=3)
frm.place(x=15,y=90)

# student info box
c=Label(s,text="Student Info-:",font="san=serif 20 bold",bg="lightgrey")
c.place(x=20,y=100)

frm=Frame(s,width=580,height=250,bg="lightgrey",bd=30,highlightbackground="black",highlightthickness=3)
frm.place(x=20,y=135)

# student details box
# student details box
c=Label(s,text="Student Details-:",font="san=serif 20 bold",bg="lightgrey")
c.place(x=602,y=100)

frm=Frame(s,width=405,height=250,bg="lightgrey",bd=30,highlightbackground="black",highlightthickness=3)
frm.place(x=605,y=135)

details_box = Label(frm, text="", font="arial 12", bg="lightgrey", wraplength=380, justify=LEFT)
details_box.place(x=10, y=10)

std_id=Label(s,text="Student ID:",font="ariel 15 bold", bg="lightgrey")
std_id.place(x=29,y=140)

# entery box
e=Entry(s,width=60)
e.place(x=170,y=145)

# student fn
std_fn=Label(s,text="First Name:",font="ariel 15 bold", bg="lightgrey")
std_fn.place(x=29,y=169)
# entery box
e1=Entry(s,width=60)
e1.place(x=170,y=175)

# student sn
std_sn=Label(s,text="Surname:",font="ariel 15 bold", bg="lightgrey")
std_sn.place(x=29,y=198)
# entery box
e2=Entry(s,width=60)
e2.place(x=170,y=204)

# student db
std_db=Label(s,text="Date of Birth:",font="ariel 15 bold", bg="lightgrey")
std_db.place(x=29,y=227)
# entery box
e3=Entry(s,width=60)
e3.place(x=170,y=233)

# student ag
std_ag=Label(s,text="Age:",font="ariel 15 bold", bg="lightgrey")
std_ag.place(x=29,y=256)
# entery box
e4=Spinbox(s,width=55,from_=1,to=110)
e4.place(x=170,y=260)

# student gn
std_G=Label(s,text="Gender:",font="ariel 15 bold", bg="lightgrey")
std_G.place(x=29,y=286)
# radio button              
gendermf = StringVar()

r=Radiobutton(s,text="Male",variable=gendermf,value="Male",font="arial 13 bold")
r.place(x=210,y=287)

r=Radiobutton(s,text="Female",variable=gendermf,value="Female",font="arial 13 bold")
r.place(x=365,y=287)

# student adrs
std_Ads=Label(s,text="Address:",font="ariel 15 bold", bg="lightgrey")
std_Ads.place(x=29,y=315)
# entery box
e6=Entry(s,width=60)
e6.place(x=170,y=322)

# students mb
std_mn=Label(s,text="Mobile:",font="ariel 15 bold", bg="lightgrey")
std_mn.place(x=29,y=345)
# entery box
e7=Entry(s,width=60)
e7.place(x=170,y=350)






# Button
# add new button
b=Button(s,text="Add New",font="Ariel 20 bold",bd=6,command=clearall)
b.place(x=20,y=400)

# Display button
b2=Button(s,text="Display",font="Ariel 20 bold",bd=6,command=dd)
b2.place(x=184,y=400)

# Clear button
b3=Button(s,text="Clear",font="Ariel 20 bold",bd=6,padx=28,command=clearall)
b3.place(x=332,y=400)

# Delete button
b4=Button(s,text="Delete",font="ariel 18 bold",bd=9,padx=28,command=deleterow)
b4.place(x=500,y=400)

# Search button
b5=Button(s,text="Search",font="ariel 18 bold",bd=9,padx=28,command=ss)
b5.place(x=671,y=400)

# Update button
b6=Button(s,text="Update",font="ariel 18 bold",bd=9,padx=25,command=ud)
b6.place(x=851,y=400)

# Submit button
b7=Button(s,text="Submit",font="ariel 10 bold",bg="#27cc69",activebackground="#05f709",bd=9,padx=200,command=conn)
b7.place(x=20,y=468)

# Exit button
b7=Button(s,text="Exit",font="ariel 10 bold",bg="#c24a4a",activebackground="#f70505",bd=9,padx=235,command=s.destroy)
b7.place(x=500,y=468)


mainloop()