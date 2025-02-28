from tkinter import *
from tkinter import messagebox
import os

def login():
    user=username.get()
    code=password.get()

    if user=="Prajesh" and code=="manish1niraj":

        root=Toplevel(screen)
        root.title("Farm logistics")
        root.geometry("1280x750+150+80")
        root.configure(bg="#d7dae2")
        root.resizable(False,False)

        #copy and paste your code here 
        




        #end of code 
        

    elif user=="" or code=="":
        messagebox.showerror("invalid","please enter username and password")
    else:
        messagebox.showerror("invalid","invalid username or password")





       


def main_screen():
    global screen
    global username
    global password

    screen=Tk()
    screen.geometry("988x655+150+80")
    screen.configure(bg="#d7dae2")

    #icon
    # image_icon=PhotoImage(file="")
    # screen.iconphoto(False,image_icon)
    screen.title("login")

    lblTitle=Label(text="Login for using farm logistic",font=("arial",50,'bold'),fg="black",bg="#d7dae2")
    lblTitle.pack(pady=50)

    bordercolor=Frame(screen,bg="black",width=800,height=400)
    bordercolor.pack()

    mainframe=Frame(bordercolor,bg="#d7dae2",width=800,height=400)
    mainframe.pack(padx=20,pady=20)

    Label(mainframe,text="username",font=("arial",30,"bold"),bg="#d7dae2").place(x=100,y=50)
    
    Label(mainframe,text="password",font=("arial",30,"bold"),bg="#d7dae2").place(x=100,y=150)
    

    username=StringVar()
    password=StringVar()

    entry_username=Entry(mainframe,textvariable=username,width=12,bd=2,font=("arial",30))
    entry_username.place(x=400,y=50)
    entry_password= Entry(mainframe,textvariable=password,width=12,bd=2,font=("arial",30),show="*")
    entry_password.place(x=400,y=150)

    def reset():
        entry_username.delete(0,END)
        entry_password.delete(0,END)

    Button(mainframe,text="login",height="2",width=23,bg="#ed3833",fg="white",bd=0,command=login).place(x=100,y=250)
    Button(mainframe,text="Reset",height="2",width=23,bg="#1089ff",fg="white",bd=0,command=reset).place(x=300,y=250)
    Button(mainframe,text="Exit",height="2",width=23,bg="#00bd56",fg="white",bd=0,command=screen.destroy).place(x=500,y=250)


    screen.mainloop()


main_screen()

