from tkinter import *
from tkinter import ttk
import psycopg2
from datetime import datetime
import tkinter.messagebox
class admin_Deshboard:

 #all student
    def view_student(self):
        self.view_windwo_panal = Toplevel()

        self.view_windwo_panal.title("User Student Detail  - DeashBoard")
        self.view_windwo_panal.geometry("744x592")
        self.view_windwo_panal.configure(background="#bab7fb")

        self.conn = psycopg2.connect(dbname="application", user="postgres", password="azhar", host="localhost",port="5432")
        self.cur = self.conn.cursor()
        self.cur.execute("select student_name,student_id,student_contact from student ")
        self.row = self.cur.fetchall()



        self.frm = Frame(self.view_windwo_panal)
        self.frm.pack(side=LEFT,padx=20)
        tv = ttk.Treeview(self.frm,columns=(1,2,3),show="headings",height=5)
        tv.pack()
        tv.heading(1,text="student_name")
        tv.heading(2, text="student_id")
        tv.heading(3, text="student_contact")
        for i in self.row:
            tv.insert("","end",values=i)

     # View All attendance
    def attendance_student(self):
        self.view_windwo_panal = Toplevel()

        self.view_windwo_panal.title("User Attendance Detail  - DeashBoard")
        self.view_windwo_panal.geometry("744x592")
        self.view_windwo_panal.configure(background="#bab7fb")

        self.conn = psycopg2.connect(dbname="application", user="postgres", password="azhar", host="localhost",port="5432")
        self.cur = self.conn.cursor()
        self.cur.execute("select student_id,status,date from  attendance ")
        self.row = self.cur.fetchall()



        self.frm = Frame(self.view_windwo_panal)
        self.frm.pack(side=LEFT,padx=20)
        tv = ttk.Treeview(self.frm,columns=(1,2,3),show="headings",height=5)
        tv.pack()
        tv.heading(1,text="student_id")
        tv.heading(2, text="status")
        tv.heading(3, text="date")
        for i in self.row:
            tv.insert("","end",values=i)


        self.labe2 = Label(self.view_windwo_panal, text="Enter Student Id", bg="#bab7fb", font='Helvetica 10 bold')
        self.labe2.place(relx=0.100, rely=0.700)

        self.edmin_student_id = Entry(self.view_windwo_panal)
        self.edmin_student_id.place(relx=0.300, rely=0.700)

        self.approve_bt = Button(self.view_windwo_panal, text="Make Attendance",command=self.admin_addtendance_bt)
        self.approve_bt.place(relx=0.100, rely=0.800, height=54, width=147)

        self.cancle_bt = Button(self.view_windwo_panal, text="Remove Student Attendance",command=self.admin_detele_attendance_bt)
        self.cancle_bt.place(relx=0.400, rely=0.800, height=54, width=160)

   #admin can make the Attendance of Student :
    def admin_addtendance_bt(self):
        self.conn = psycopg2.connect(dbname="application", user="postgres", password="azhar", host="localhost",
                                     port="5432")
        self.cur = self.conn.cursor()
        postgres_insert_query = """ INSERT INTO attendance (student_id,status,date) VALUES (%s,%s,%s)"""
        record_to_insert = (self.edmin_student_id.get(), 'present', datetime.date(datetime.now()))
        self.cur.execute(postgres_insert_query, record_to_insert)
        tkinter.messagebox._show("Sucess", "Attendance is Done !", parent=self.view_windwo_panal)
        self.conn.commit()
        self.conn.close()

        # admin can make the Attendance of Student :
    def admin_detele_attendance_bt(self):
        self.conn = psycopg2.connect(dbname="application", user="postgres", password="azhar", host="localhost",port="5432")
        self.cur = self.conn.cursor()
        if self.edmin_student_id.get()=="":
            tkinter.messagebox.showerror("Error","Please Enter the Student ID ")
        else:
            postgres_delete_query = """ delete from attendance where student_id=%s"""
            record_to_detete = (self.edmin_student_id.get())
            self.cur.execute(postgres_delete_query, record_to_detete)
            print(self.edmin_student_id.get())
            tkinter.messagebox._show("Sucess", "Attendance is Remove !", parent=self.view_windwo_panal)
            self.conn.commit()
            self.conn.close()




 #Leave Approval Funcation
    def Leave_Approval_window(self):
        self.Leave_windwo_panal = Toplevel()

        self.Leave_windwo_panal.title("Leave Approval  Detail  - DeashBoard")
        self.Leave_windwo_panal.geometry("744x592")
        self.Leave_windwo_panal.configure(background="#bab7fb")

        self.conn = psycopg2.connect(dbname="application", user="postgres", password="azhar", host="localhost",port="5432")
        self.cur = self.conn.cursor()
        self.cur.execute("select student_id,leave_status,date from leave ")
        self.row = self.cur.fetchall()

        self.frm = Frame(self.Leave_windwo_panal)
        self.frm.pack(side=LEFT,padx=20)
        tv = ttk.Treeview(self.frm,columns=(1,2,3),show="headings",height=5)
        tv.pack()
        tv.heading(1,text="student_id")
        tv.heading(2, text="leave_status")
        tv.heading(3, text="date")
        for i in self.row:
            tv.insert("","end",values=i)

        self.labe2 = Label(self.Leave_windwo_panal,text="Enter Student Id",bg="#bab7fb",font='Helvetica 10 bold')
        self.labe2.place(relx=0.100, rely=0.700)

        self.student_id = Entry(self.Leave_windwo_panal)
        self.student_id.place(relx=0.300, rely=0.700)

        self.approve_bt = Button(self.Leave_windwo_panal, text="Approve Leave",command=self.leave_bt)
        self.approve_bt.place(relx=0.100, rely=0.800, height=54, width=147)

        self.cancle_bt = Button(self.Leave_windwo_panal, text="Cancle Leave",command=self.absent_bt)
        self.cancle_bt.place(relx=0.400, rely=0.800, height=54, width=147)
 #End

    def leave_bt(self):
        self.conn = psycopg2.connect(dbname="application", user="postgres", password="azhar", host="localhost", port="5432")
        self.cur = self.conn.cursor()
        self.cur.execute("select * from leave")

        self.row = self.cur.fetchone()
        self.get_date = self.row[2]

        if self.student_id.get()=="":
            tkinter.messagebox.showerror("Error", "Enter Student Id ....!", parent=self.Leave_windwo_panal)
        else:
            postgres_insert_query = """ INSERT INTO attendance (student_id,status,date) VALUES (%s,%s,%s)"""
            record_to_insert = (self.student_id.get(), 'Leave', self.get_date)
            self.cur.execute(postgres_insert_query, record_to_insert)


        #self.cur.execute("delete from attendance where student_id=%s",(self.student_id.get()))

            tkinter.messagebox._show("Sucess", "Leave Approve ....!", parent=self.Leave_windwo_panal)
            self.conn.commit()
            self.conn.close()

    # End :Work

    #Absent Button Coding
    def absent_bt(self):
        self.conn = psycopg2.connect(dbname="application", user="postgres", password="azhar", host="localhost", port="5432")
        self.cur = self.conn.cursor()
        self.cur.execute("select * from leave")

        self.row = self.cur.fetchone()
        self.get_date = self.row[2]

        if self.student_id.get() == "":
            tkinter.messagebox.showerror("Error", "Enter Student Id ....!", parent=self.Leave_windwo_panal)
        else:
            postgres_insert_query = """ INSERT INTO attendance (student_id,status,date) VALUES (%s,%s,%s)"""
            record_to_insert = (self.student_id.get(), 'Absent', self.get_date)
            self.cur.execute(postgres_insert_query, record_to_insert)

        # self.cur.execute("delete from attendance where student_id=%s",(self.student_id.get()))

            tkinter.messagebox._show("Sucess", " Teacher Dis approve you Leave  ....!", parent=self.Leave_windwo_panal)
            self.conn.commit()
            self.conn.close()

    # End :Work

    def __init__(self):
        self.admin_det = Tk()
        self.admin_det.title("Admin - DeashBoard")
        self.admin_det.geometry("744x592")
        self.admin_det.configure(background="#bab7fb")

        self.Label1 = Label(self.admin_det, text="Welcome Admin", font='Helvetica 18 bold')
        self.Label1.place(relx=0, rely=0.10)
        self.Label1.configure(background="#bab7fb")

        self.mainFrame = Frame(self.admin_det)
        self.mainFrame.place(relx=0.2, rely=0.156, relheight=0.744, relwidth=0.592)
        self.mainFrame.configure(relief='groove')
        self.mainFrame.configure(borderwidth="2")
        self.mainFrame.configure(background="#d9d9d9")

        self.user_bt = Button(self.mainFrame, text="All Student ",command=self.view_student)
        self.user_bt.place(relx=0.100, rely=0.100, height=54, width=147)

        self.user_bt = Button(self.mainFrame, text="View Attendance",command=self.attendance_student)
        self.user_bt.place(relx=0.600, rely=0.100, height=54, width=147)

        self.user_bt = Button(self.mainFrame, text="Leave Approval",command=self.Leave_Approval_window)
        self.user_bt.place(relx=0.100, rely=0.300, height=54, width=147)

        self.user_bt = Button(self.mainFrame, text=" Searching ")
        self.user_bt.place(relx=0.600, rely=0.300, height=54, width=147)


        self.admin_det.mainloop()
