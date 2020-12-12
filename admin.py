from tkinter import *
import tkinter.messagebox
import psycopg2
from admin_detail import admin_Deshboard

class admin_panel:

    def admin_open(self):
        self.conn = psycopg2.connect(dbname="application", user="postgres", password="azhar", host="localhost",port="5432")
        self.cur = self.conn.cursor()
        if self.eeadminid.get() == "" or self.eeadmin_password.get() == "":
            tkinter.messagebox.showerror("Error", "Enter Username And Password ", parent=self.adminroot)
        else:
            self.cur.execute("select * from admin where admin_id=%s and admin_password=%s",(self.eeadminid.get(), self.eeadmin_password.get()))
            self.row = self.cur.fetchone()
            if self.row == None:
                tkinter.messagebox.showerror("Erroe", "Invalied Username and password", parent=self.adminroot)
            else:
                self.adminroot.destroy()
                admin_Deshboard()

        self.conn.commit()
        self.conn.close()

    def __init__(self):
        self.adminroot = Tk()
        self.adminroot.title("Welcome - Admin")
        self.adminroot.geometry("744x592")
        self.adminroot.configure(background="#bab7fb")

        self.Label1 = Label(self.adminroot, text="Admin Login ", font='Helvetica 18 bold')
        self.Label1.place(relx=0, rely=0.10)
        self.Label1.configure(background="#bab7fb")

        self.mainFrame = Frame(self.adminroot)
        self.mainFrame.place(relx=0.2, rely=0.156, relheight=0.744, relwidth=0.592)
        self.mainFrame.configure(relief='groove')
        self.mainFrame.configure(borderwidth="2")
        self.mainFrame.configure(background="#d9d9d9")


        self.label1 = Label(self.mainFrame, text="Login ID", pady=20,bg="#d9d9d9")

        self.label1.grid(row=4, column=1, padx=(100, 10))

        self.label2 = Label(self.mainFrame, text="password", pady=20,bg="#d9d9d9")

        self.label2.grid(row=6, column=1, padx=(100, 10))



        self.eeadminid = Entry(self.mainFrame)
        self.eeadminid.grid(row=5, column=1, padx=(100, 10))

        self.eeadmin_password = Entry(self.mainFrame)
        self.eeadmin_password.grid(row=7, column=1, padx=(100, 10))

        self.login = Button(self.mainFrame, text="Login",command=self.admin_open)
        self.login.place(relx=0.190, rely=0.400, height=54, width=147)

        self.adminroot.mainloop()
