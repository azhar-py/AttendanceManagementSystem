from tkinter import *
from user import user_panel
from admin import admin_panel

def open_user():
    user_panel()
def admin_user():
    admin_panel()


class main:

    def close(self):
        self.mmain.destroy()


    def __init__(self):
        self.mmain = Tk()
        self.mmain.title("Welcome")

#for full Window and Background Color
        self.mmain.attributes("-fullscreen", True)
        self.mmain.configure(background="#bab7fb")

       #Attendance Management System
        self.Label1 = Label(self.mmain,text="Attendance Management System",font='Helvetica 18 bold')
        self.Label1.place(relx=0, rely=0.10)
        self.Label1.configure(background="#bab7fb")
    #Add Frame on Window
        self.mainFrame = Frame(self.mmain)
        self.mainFrame.place(relx=0.2, rely=0.156, relheight=0.744, relwidth=0.592)
        self.mainFrame.configure(relief='groove')
        self.mainFrame.configure(borderwidth="2")
        self.mainFrame.configure(background="#d9d9d9")

       #Butto on Frame
        self.user_bt = Button(self.mainFrame,text="User",command=open_user)
        self.user_bt.place(relx=0.400, rely=0.179, height=54, width=147)

        self.admin_bt = Button(self.mainFrame,text="Admin",command=admin_user)
        self.admin_bt.place(relx=0.400, rely=0.374, height=54, width=147)

        self.close_bt = Button(self.mainFrame, text="Close", command=self.close)
        self.close_bt.place(relx=0.400, rely=0.574, height=54, width=147)


        self.mmain.mainloop()


if __name__ == '__main__':
    mrun = main()
