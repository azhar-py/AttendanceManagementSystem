from tkinter import *
from Registration import registration_panel
from Login import login_panel


def reg_user():
    registration_panel()
def log_user():
    login_panel()

class user_panel:

    def close(self):
        self.userroot.destroy()

    def __init__(self):
        self.userroot = Tk()
        self.userroot.title("Welcome - User")
        self.userroot.geometry("744x592")
        self.userroot.configure(background="#bab7fb")

        self.Label1 = Label(self.userroot, text="Welcome User ! ", font='Helvetica 18 bold')
        self.Label1.place(relx=0, rely=0.10)
        self.Label1.configure(background="#bab7fb")


        self.mainFrame = Frame(self.userroot)
        self.mainFrame.place(relx=0.2, rely=0.156, relheight=0.744, relwidth=0.592)
        self.mainFrame.configure(relief='groove')
        self.mainFrame.configure(borderwidth="2")
        self.mainFrame.configure(background="#d9d9d9")


        self.reg_bt = Button(self.mainFrame, text="Registration",command=registration_panel)
        self.reg_bt.place(relx=0.400, rely=0.179, height=54, width=147)

        self.login_bt = Button(self.mainFrame, text="Login",command=login_panel)
        self.login_bt.place(relx=0.400, rely=0.374, height=54, width=147)

        self.close_bt = Button(self.mainFrame, text="Close",command=self.close)
        self.close_bt.place(relx=0.400, rely=0.574, height=54, width=147)



        self.userroot.mainloop()



