from tkinter import *
from tkinter import ttk
# from PIL import image,imageTk

class Login_window:

    def __init__(self,root):
        self.root = root
        self.root.title("login")
        self.root.geometry("1550x800+0+0")
 
        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)
        
        get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)

        #LABEL
        username=lbl=Label(frame,text="username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=75,y=155) 

        self.txtuser= ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)
        
        username=lbl=Label(frame,text="password",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=75,y=225) 
        self.txtpass= ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=250,width=270)
           #login
        loginbtn= Button(frame,text="login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="black")
        loginbtn.place(x=110,y=300,width=120,height=35)
           #Register
        registerbtn= Button(frame,text="register",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="black")
        registerbtn.place(x=110,y=350,width=120,height=35)


if __name__ == "__main__":
    root=Tk()
app=Login_window(root)
root.mainloop()

