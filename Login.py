from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import psycopg2
import psycopg2.extensions
from datetime import datetime

   #Login Class:
class login_panel:

    global profile_id

    def login_open(self):
        self.conn = psycopg2.connect(dbname="application", user="postgres", password="azhar", host="localhost",
                                     port="5432")
        self.cur = self.conn.cursor()

        if self.eestudent_id.get() == "" or self.eestudent_password.get() == "":
            tkinter.messagebox.showerror("Error", "Enter Student ID And Password ", parent=self.logroot)
        else:
            self.cur.execute("select * from student where student_id=%s and student_password=%s",
                             (self.eestudent_id.get(), self.eestudent_password.get()))

            self.row = self.cur.fetchone()
            self.show_id = self.row[2]
            self.profile_id = self.show_id
            if self.row == None:
                tkinter.messagebox.showerror("Error", "Invalied Username and password", parent=self.logroot)
            else:
                self.logroot.destroy()
                self.Login_Deashboard_window()

        self.conn.commit()
        self.conn.close()

    # Login Deashboard Window  Frame
    def Login_Deashboard_window(self):
        self.login_window_panel = Toplevel()
        self.login_window_panel.geometry("744x592")
        self.login_window_panel.title("Login - DeashBoard")

        self.login_window_panel.configure(background="#bab7fb")

        self.mainFrame = Frame(self.login_window_panel)
        self.mainFrame.place(relx=0.2, rely=0.156, relheight=0.744, relwidth=0.592)
        self.mainFrame.configure(relief='groove')
        self.mainFrame.configure(borderwidth="2")
        self.mainFrame.configure(background="#d9d9d9")



        self.Attendance_bt = Button(self.mainFrame, text="Attendance", command=self.Attendance_window)
        self.Attendance_bt.place(relx=0.400, rely=0.179, height=54, width=147)

        self.Leave_bt = Button(self.mainFrame, text="Leave",command=self.Leave_window)
        self.Leave_bt.place(relx=0.400, rely=0.374, height=54, width=147)

        self.Views_bt = Button(self.mainFrame, text="Views",command=self.view_window)
        self.Views_bt.place(relx=0.400, rely=0.574, height=54, width=147)

    # End : Work

    # Attendence Button  Window  Frame
    def Attendance_window(self):
        self.conn = psycopg2.connect(dbname="application", user="postgres", password="azhar", host="localhost", port="5432")
        self.cur = self.conn.cursor()
        postgres_insert_query = """ INSERT INTO attendance (student_id,status,date) VALUES (%s,%s,%s)"""
        record_to_insert = (self.profile_id, 'present', datetime.date(datetime.now()))
        self.cur.execute(postgres_insert_query, record_to_insert)
        tkinter.messagebox._show("Sucess", "Attendance is Done !", parent=self.login_window_panel)
        self.conn.commit()
        self.conn.close()

    # End : Work

    # Leave Button
    def Leave_window(self):
        self.conn = psycopg2.connect(dbname="application", user="postgres", password="azhar", host="localhost",port="5432")
        self.cur = self.conn.cursor()
        postgres_insert_query = """ INSERT INTO leave (student_id,leave_status,date) VALUES (%s,%s,%s)"""
        record_to_insert = (self.profile_id, 'Leave', datetime.date(datetime.now()))
        self.cur.execute(postgres_insert_query, record_to_insert)
        tkinter.messagebox._show("Sucess", "Leave Request is sending....!", parent=self.login_window_panel)
        self.conn.commit()
        self.conn.close()

        # End :Work

        # View  Button
    def view_window(self):
        self.view_windwo_panal = Toplevel()

        self.view_windwo_panal.title("User Attendance Detail  - DeashBoard")
        self.view_windwo_panal.geometry("744x592")
        self.view_windwo_panal.configure(background="#bab7fb")

        self.conn = psycopg2.connect(dbname="application", user="postgres", password="azhar", host="localhost",port="5432")
        self.cur = self.conn.cursor()
        self.cur.execute("select * from attendance where student_id=%s ", (self.profile_id,))
        self.row = self.cur.fetchall()



        self.frm = Frame(self.view_windwo_panal)
        self.frm.pack(side=LEFT,padx=20)
        tv = ttk.Treeview(self.frm,columns=(1,2,3),show="headings",height=5)
        tv.pack()
        tv.heading(1,text="student_id")
        tv.heading(2, text="status")
        tv.heading(3, text="data")
        for i in self.row:
            tv.insert("","end",values=i)


    # End :Work

    def __init__(self):
        self.logroot = Tk()
        self.logroot.title("Login")
        self.logroot.geometry("744x592")
        self.logroot.configure(background="#bab7fb")

        self.Label1 = Label(self.logroot, text="User Login !", font='Helvetica 18 bold')
        self.Label1.place(relx=0, rely=0.10)
        self.Label1.configure(background="#bab7fb")

        self.mainFrame = Frame(self.logroot)
        self.mainFrame.place(relx=0.2, rely=0.156, relheight=0.744, relwidth=0.592)
        self.mainFrame.configure(relief='groove')
        self.mainFrame.configure(borderwidth="2")
        self.mainFrame.configure(background="#d9d9d9")

        self.label1 = Label(self.mainFrame, text="Student ID", pady=20, bg="#d9d9d9")

        self.label1.grid(row=4, column=1, padx=(100, 10))

        self.label2 = Label(self.mainFrame, text="Password", pady=20, bg="#d9d9d9")

        self.label2.grid(row=6, column=1, padx=(100, 10))

        self.eestudent_id = Entry(self.mainFrame)
        self.eestudent_id.grid(row=5, column=1, padx=(100, 10))

        self.eestudent_password = Entry(self.mainFrame)
        self.eestudent_password.grid(row=7, column=1, padx=(100, 10))

        self.login = Button(self.mainFrame, text="Login", command=self.login_open)
        self.login.place(relx=0.190, rely=0.400, height=54, width=147)

        self.logroot.mainloop()
