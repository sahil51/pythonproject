
import mysql.connector
from tkinter import *
from tkinter import ttk, messagebox

# Connect to MySQL
def connect_db():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="sahil7070",
            database="studentdb"
        )
        return conn
    except mysql.connector.Error as e:
        messagebox.showerror("Database Error", f"Error connecting to MySQL:\n{e}")
        return None

# Function to add student
def add_student():
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            query = """
                INSERT INTO students (student_id, first_name, sur_name, dob, age, gender, address, mobile)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            values = (
                student_id.get(), first_name.get(), sur_name.get(),
                dob.get(), age.get(), gender.get(), address.get(), mobile.get()
            )
            cursor.execute(query, values)
            conn.commit()
            messagebox.showinfo("Success", "Student added successfully!")
            display_students()
        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Failed to add student: {e}")
        finally:
            conn.close()

# Function to update student
def update_student():
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            query = """
                UPDATE students
                SET first_name=%s, sur_name=%s, dob=%s, age=%s, gender=%s, address=%s, mobile=%s
                WHERE student_id=%s
            """
            values = (
                first_name.get(), sur_name.get(), dob.get(), age.get(),
                gender.get(), address.get(), mobile.get(), student_id.get()
            )
            cursor.execute(query, values)
            conn.commit()
            messagebox.showinfo("Success", "Student updated successfully!")
            display_students()
        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Failed to update student: {e}")
        finally:
            conn.close()

# Function to delete student
def delete_student():
    delete_window = Toplevel(root)
    delete_window.title("Delete Student")
    delete_window.geometry("300x200")
    
    Label(delete_window, text="Enter Student ID to Delete:").pack(pady=5)
    delete_var = StringVar()
    Entry(delete_window, textvariable=delete_var).pack(pady=5)
    
    def confirm_delete():
        conn = connect_db()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM students WHERE student_id = %s", (delete_var.get(),))
                row = cursor.fetchone()
                
                if row:
                    confirm = messagebox.askyesno(
                        "Confirm Delete",
                        f"Are you sure you want to delete:\n\nID: {row[0]}\nName: {row[1]} {row[2]}?"
                    )
                    if confirm:
                        cursor.execute("DELETE FROM students WHERE student_id = %s", (delete_var.get(),))
                        conn.commit()
                        messagebox.showinfo("Deleted", "Student record deleted successfully")
                        delete_window.after(2000, delete_window.destroy)  # Auto close after 2 seconds
                else:
                    messagebox.showinfo("Not Found", "Student ID not found")
            except mysql.connector.Error as e:
                messagebox.showerror("Error", f"Failed to delete student: {e}")
            finally:
                conn.close()
    
    Button(delete_window, text="Delete", command=confirm_delete).pack(pady=5)

# Function to display students
def display_students():
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM students")
            rows = cursor.fetchall()
            student_table.delete(*student_table.get_children())  # Clear existing table data
            for row in rows:
                student_table.insert("", "end", values=row)
        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Failed to fetch students: {e}")
        finally:
            conn.close()

# Function to clear form
def clear_form():
    student_id.set("")
    first_name.set("")
    sur_name.set("")
    dob.set("")
    age.set("")
    gender.set("")
    address.set("")
    mobile.set("")

# Function to clear student information
def clear_student_info():
    student_info.config(text="Student Information", fg="black")  # Ensures the text resets properly
    student_info.update()  

# Function to fill form when clicking on table row
def on_row_select(event):
    selected = student_table.focus()
    values = student_table.item(selected, 'values')
    if values:
        student_id.set(values[0])
        first_name.set(values[1])
        sur_name.set(values[2])
        dob.set(values[3])
        age.set(values[4])
        gender.set(values[5])
        address.set(values[6])
        mobile.set(values[7])

# Function to search and display student
def search_student():
    search_window = Toplevel(root)
    search_window.title("Search Student")
    search_window.geometry("300x150")
    
    Label(search_window, text="Enter Student ID or Name:").pack(pady=5)
    search_var = StringVar()
    Entry(search_window, textvariable=search_var).pack(pady=5)
    
    def fetch_student():
        conn = connect_db()
        if conn:
            try:
                cursor = conn.cursor()
                query = "SELECT * FROM students WHERE student_id = %s OR first_name = %s"
                cursor.execute(query, (search_var.get(), search_var.get()))
                row = cursor.fetchone()
                
                if row:
                    student_info.config(
                        text=f"ID: {row[0]}\nName: {row[1]} {row[2]}\nDOB: {row[3]}\nAge: {row[4]}\nGender: {row[5]}\nAddress: {row[6]}\nMobile: {row[7]}"
                    )
                    search_window.after(10, search_window.destroy)  # Auto close after 2 seconds
                else:
                    messagebox.showinfo("Not Found", "User is not available")
            except mysql.connector.Error as e:
                messagebox.showerror("Error", f"Failed to fetch student: {e}")
            finally:
                conn.close()
    
    Button(search_window, text="Search", command=fetch_student).pack(pady=5)

# GUI Setup
root = Tk()
root.title("Student Database Management")
root.geometry("1260x560")
root.config(bg="#f2f2f2")
root.resizable(False, False)

# Frames

headframe = Label(root,bg="#ffffff",text="Student   Management   System",font=("Arial", 30, "bold"), padx=10, pady=10, relief=RIDGE, bd=3)
headframe.place(x=20, y=0, width=1220, height=60)

form_frame = Frame(root, bg="#ffffff", padx=10, pady=10, relief=RIDGE, bd=3)
form_frame.place(x=20, y=57, width=420, height=360)

button_frame = Frame(root, bg="#ffffff", padx=10, pady=10)
button_frame.place(x=22, y=417, width=418, height=88)

infoframe = Frame(root,bg="#ffffff", padx=10, pady=10, relief=RIDGE, bd=3)
infoframe.place(x=870, y=57, width=370, height=225)

info_frame = Frame(root, bg="#ffffff", padx=12, pady=2, bd=3)
info_frame.place(x=440, y=60, width=430, height=218)


# Student information data
table_frame = Frame(root)
table_frame.place(x=439, y=280, width=801, height=225)

# Label inside info_frame
student_info = Label(info_frame, text="Student Information", bg="#ffffff", justify=LEFT)
student_info.grid(row=0, column=0, columnspan=4, pady=5)


# Frame for buttons inside the table frame (Bottom-Right)
table_button_frame = Frame(table_frame, bg="#ffffff")
table_button_frame.pack(side=BOTTOM, fill=X, pady=0) 

# Update Button (Bottom-Right of Student Table)
update_button = Button(table_button_frame, text="Update", bg="blue", fg="white", font=("Arial", 12, "bold"), command=update_student, width=12)
update_button.pack(side=RIGHT, padx=10, pady=5) 


# Label inside infoframe
appinfo = Label(infoframe, text="App Information\n\n"
                                "Python: Core programming language.\n"
                                "Tkinter: GUI library for building the user interface.\n"
                                "MySQL: Relational database for storing student data.\n"
                                "mysql.connector: Python library for connecting MySQL\nwith Python.\n"
                                "Developed by: Sahil\n"
                                "Mail: sahilofficial0@gmail.com\n"
                                "Contact: 7404304607",
                bg="#ffffff", justify=LEFT)
appinfo.grid(row=0, column=0, columnspan=6, pady=5)



footframe = Label(root, text="© 2025 Student Management System | Developed by Sahil", bg="#f2f2f2", fg="gray", font=("Arial", 10, "italic"))
footframe.place(x=20, y=510, width=1220, height=35)

# Empty row to push buttons to the bottom
info_frame.grid_rowconfigure(1, weight=1)  

# Frame for buttons (inside info_frame) to place at the bottom
button_container = Frame(info_frame, bg="#ffffff")
button_container.grid(row=2, column=0, columnspan=4, pady=5, sticky="s")  

# Display and Clear Buttons (Placed inside button_container)
display_button = Button(button_container, text="Display", bg="#673AB7", fg="white", command=search_student, width=12, padx=50)
display_button.pack(side=LEFT, padx=2, pady=5)

clear_button = Button(button_container, text="Clear StudentInfo", bg="red", fg="white", command=clear_student_info, width=12, padx=50)
clear_button.pack(side=RIGHT, padx=2, pady=5)




# Variables
student_id = StringVar()
first_name = StringVar()
sur_name = StringVar()
dob = StringVar()
age = StringVar()
gender = StringVar()
address = StringVar()
mobile = StringVar()

# Labels & Entries
Label(form_frame, text="Student ID:", bg="#ffffff").grid(row=1, column=0, sticky=W, pady=5)
Entry(form_frame, textvariable=student_id,width=40,bd=2).grid(row=1, column=1, pady=5)



Label(form_frame, text="First Name:", bg="#ffffff").grid(row=2, column=0, sticky=W, pady=5)
Entry(form_frame, textvariable=first_name,width=40, bd=2).grid(row=2, column=1, pady=5)

Label(form_frame, text="Surname:", bg="#ffffff").grid(row=3, column=0, sticky=W, pady=5)
Entry(form_frame, textvariable=sur_name,width=40, bd=2).grid(row=3, column=1, pady=5)

Label(form_frame, text="DOB (YYYY-MM-DD):", bg="#ffffff").grid(row=4, column=0, sticky=W, pady=5)
Entry(form_frame, textvariable=dob,width=40, bd=2).grid(row=4, column=1, pady=5)

Label(form_frame, text="Age:", bg="#ffffff").grid(row=5, column=0, sticky=W, pady=5)
Entry(form_frame, textvariable=age,width=40, bd=2).grid(row=5, column=1, pady=5)

Label(form_frame, text="Gender:", bg="#ffffff").grid(row=6, column=0, sticky=W, pady=5)
ttk.Combobox(form_frame, textvariable=gender, values=("Male", "Female", "Other"),width=37).grid(row=6, column=1, pady=5)

Label(form_frame, text="Address:", bg="#ffffff").grid(row=7, column=0, sticky=W, pady=5)
Entry(form_frame, textvariable=address,width=40, bd=2).grid(row=7, column=1, pady=5)

Label(form_frame, text="Mobile:", bg="#ffffff").grid(row=8, column=0, sticky=W, pady=5)
Entry(form_frame, textvariable=mobile,width=40, bd=2).grid(row=8, column=1, pady=5)

# Buttons
Button(button_frame, text="Add", bg="#4CAF50", fg="white",font=("Arial", 12, "bold"), command=add_student, width=11).grid(row=0, column=0, padx=5, pady=5)
Button(button_frame, text="Delete", bg="#E53935", fg="white",font=("Arial", 12, "bold"), command=delete_student, width=11).grid(row=0, column=2, padx=5, pady=5)
Button(button_frame, text="Clear", bg="#FFC107", fg="black",font=("Arial", 12, "bold"), command=clear_form, width=11).grid(row=0, column=3, padx=5, pady=5)

# Student Table
columns = ("Student_ID", "First_Name", "Sur_Name", "Dob", "Age", "Gender", "Address", "Mobile")
student_table = ttk.Treeview(table_frame, columns=columns, show="headings")
for col in columns:
    student_table.heading(col, text=col)
    student_table.column(col, width=100)

student_table.bind("<ButtonRelease-1>", on_row_select)
student_table.pack()

# Fetch Initial Data
display_students()

mainloop()
