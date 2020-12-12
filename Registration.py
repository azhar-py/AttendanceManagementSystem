from tkinter import *
import tkinter.messagebox
import psycopg2
class registration_panel:

    def close(self):
        self.root.destroy()

    def reg_connection(self):

        self.conn = psycopg2.connect(dbname="application", user="postgres",password="azhar",host="localhost",port="5432")
        self.cur = self.conn.cursor()
        if self.eestudentid.get()=="" or self.eename.get()=="" or self.eepassword.get()=="" or self.eecontact.get()=="":
            tkinter.messagebox.showerror("Error","Fill the Form",parent=self.root)
        else:
            postgres_insert_query = """ INSERT INTO student (student_password,Student_name,Student_id,student_contact) VALUES (%s,%s,%s,%s)"""
            record_to_insert = (self.eepassword.get(),self.eename.get(),self.eestudentid.get(),self.eecontact.get())
            self.cur.execute(postgres_insert_query,record_to_insert)
            tkinter.messagebox._show("Sucess", "Registration is Done !",parent=self.root)
            self.conn.commit()
            self.conn.close()
            self.root.destroy()


    def __init__(self):
        self.root = Tk()
        self.root.title("Registration")
        self.root.geometry("744x592")
        self.root.configure(background="#bab7fb")

        self.Label1 = Label(self.root, text="Registration For Account", font='Helvetica 18 bold')
        self.Label1.place(relx=0, rely=0.10)
        self.Label1.configure(background="#bab7fb")


        self.mainFrame = Frame(self.root)
        self.mainFrame.place(relx=0.2, rely=0.156, relheight=0.800, relwidth=0.592)
        self.mainFrame.configure(relief='groove')
        self.mainFrame.configure(borderwidth="2")
        self.mainFrame.configure(background="#d9d9d9")

       #Label set on Frame

        self.label1 = Label(self.mainFrame, text="Student ID ", pady=20, bg="#d9d9d9")

        self.label1.grid(row=1, column=1, padx=(100, 10))

        self.label2 = Label(self.mainFrame,text="Name",pady=20,bg="#d9d9d9")

        self.label2.grid(row=3,column=1,padx=(100, 10))

        self.label3 = Label(self.mainFrame, text="Password",pady=20,bg="#d9d9d9")

        self.label3.grid(row=5, column=1,padx=(100, 10))

        self.label4 = Label(self.mainFrame, text="Contact Number",pady=20,bg="#d9d9d9")

        self.label4.grid(row=7, column=1,padx=(100, 10))




     #Text Field Creat and Add On frame
        self.eestudentid = Entry(self.mainFrame)
        self.eestudentid.grid(row=2, column=1, padx=(100, 10))
        
        self.labelresult = Label(self.mainFrame,text="Enter Only 4 Number ",bg="#d9d9d9",fg="red")
        self.labelresult.grid(row=2, column=4,)


        self.eename = Entry(self.mainFrame)
        self.eename.grid(row=4,column=1,padx=(100, 10))

        self.eepassword = Entry(self.mainFrame)
        self.eepassword.grid(row=6, column=1,padx=(100, 10))

        self.eecontact = Entry(self.mainFrame)
        self.eecontact.grid(row=8, column=1,padx=(100, 10))

        self.success = Button(self.mainFrame, text="Registration",command=self.reg_connection)
        self.success.place(relx=0.190, rely=0.700, height=54, width=147)

        self.close_bt = Button(self.mainFrame, text="Close",command=self.close)
        self.close_bt.place(relx=0.190, rely=0.850, height=54, width=147)



        self.root.mainloop()

