from tkinter import *
import tkinter as tk
import datetime
import sqlite3
from tkinter import messagebox


############################# Begin Second Window #####################################
def login():
    user=username.get()
    code=password.get()
    #Creating seccond window
    if user=='HelloWorld' and code=="1234":
        root=Toplevel(screen)
        root.title('Recipe Shmecipe')
        root.geometry('1024x768')
        root.configure(bg='#318AE4')
        root.resizable(False,False)

        #labeling cat pictures

        #Quitting second window button
        button_quit=Button(root,text='Close Window',width=11,height=2,borderwidth=2,command=root.quit)
        button_quit.pack()

        #Images of cat

    #Creating Error box for invalid username and password. Username = HelloWorld, Password = 1234
    elif user=='' and code== '':
        messagebox.showerror('Invalid','Please enter Username and Password')
    elif user=='':
        messagebox.showerror('Invalid','Username is required')
    elif code=='':
        messagebox.showerror('Invalid','Password field required')
    elif user!='HelloWorld' and code!='1234':
        messagebox.showerror('Invalid','Invalid username and Password')
    elif user!='HelloWorld':
        messagebox.showerror('Invalid','Please enter a valid username')
    elif code!='1234':
        messagebox.showerror('Invalid','Please enter Username and Password')

############################# End Second Window #####################################

def main_screen():
    #Creation of the login screen/window


    global screen
    global username
    global password

    screen=Tk()
    screen.geometry('1280x720+150+80')
    screen.configure(bg='grey')

    #icon
    screen.title('Login')

    #Label title
    lblTitle=Label(text='Login System',font=('arial',50,'bold'),fg='black',bg='grey')
    lblTitle.pack(pady=50)
    #Border for username and password
    bordercolor=Frame(screen,bg='black',width=800,height=400)
    bordercolor.pack()

    mainframe=Frame(bordercolor,bg='grey',width=800,height=400)
    mainframe.pack(padx=20,pady=20)

    Label(mainframe,text='Username',font=('arial',30,'bold'),bg='grey').place(x=100,y=50)
    Label(mainframe, text='Password', font=('arial', 30, 'bold'), bg='grey').place(x=101, y=150)

    username=StringVar()
    password=StringVar()
    #Entry boxes for username and password
    entry_username=Entry(mainframe,textvariable=username,width=12,bd=2,font=('arial',30))
    entry_username.place(x=400,y=50)
    entry_password=Entry(mainframe,textvariable=password,width=12,bd=2,font=('arial',30),show='*')
    entry_password.place(x=400,y=150)

    #Defining reset command
    def reset():
        entry_username.delete(0,END)
        entry_password.delete(0,END)

    #Login, Reset and Exit buttons
    Button(mainframe,text='Login',height='2',width=23,bg='#ed3833',fg='white',bd=0,command=login).place(x=100,y=250)
    Button(mainframe, text='Reset', height='2', width=23, bg='#1089ff', fg='white', bd=0,command=reset).place(x=300, y=250)
    Button(mainframe, text='Exit', height='2', width=23, bg='#00bd56', fg='white', bd=0,command=screen.destroy).place(x=500, y=250)



    screen.mainloop()

main_screen()
