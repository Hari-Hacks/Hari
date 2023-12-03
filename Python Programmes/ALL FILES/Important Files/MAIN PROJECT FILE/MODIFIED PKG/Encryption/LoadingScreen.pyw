import tkinter as tk
from tkinter import *
from random import random as tim
import socket

def is_connected():
    #function check if internet is on
    try:
        #checks for connection with host
        socket.create_connection(("1.1.1.1",53))
        return True
    except OSError:
        pass
    return False
def progress_bar():
    def close_progress():
        root.destroy()
    root = tk.Tk()
    root.title("Progress Bar")
    screen_width=root.winfo_screenwidth()
    screen_height=root.winfo_screenheight()
    x=(screen_width/2)-(626/2)
    y=(screen_height/2)-(417/2)
    root.geometry('%dx%d+%d+%d'%(626,417,x,y))
    root.resizable(width=0,height=0)
    img=PhotoImage(file="load3.png")
    labelimg1=Label(root,width=626,height=417,image=img)
    labelimg1.place(x=0,y=0)
    loading_label=Label(root,text="Checking for libraries ...",font=("Arial", 8),foreground="white",background="#1c1c1c")
    loading_label.pack(pady=5)
    from tkinter import ttk
    style=ttk.Style()
    style.theme_use('default')
    style.configure("black.Horizontal.TProgressbar",foreground='black',background='white')
    progress_bar=ttk.Progressbar(root,style="black.Horizontal.TProgressbar",orient="horizontal",length=200,mode="determinate",maximum=100,value=0)
    progress_bar.pack(pady=10)
    root.after(2000, close_progress)
    def update_progress():
        progress_bar.step(1)
        percentage=progress_bar['value']
        progress_bar['value']+=1
        root.title(f"Progress Bar - {percentage}%")
        if progress_bar['value']<100:
            root.after(50,update_progress)
    root.after(50,update_progress)
    root.mainloop()
progress_bar()
#checking for libraries
v=[]
k=is_connected()
try:
    import tkinter
except:v.append('tkinter')
try:
    import mysql.connector
except:v.append('mysql.connector')
try:
    import pyperclip
except:v.append('pyperclip')
try:
    import pygame
except:v.append('pygame')
if v or not(k):
    # Create the window after loading
    #if library unavailble
    root=tk.Tk()
    root.title("Appropriate Libraries Unavailable")
    screen_width=root.winfo_screenwidth()
    screen_height=root.winfo_screenheight()
    x=(screen_width/2)-(626/2)
    y=(screen_height/2)-(417/2)
    root.geometry('%dx%d+%d+%d'%(626,417,x,y))
    root.resizable(width=0,height=0)
    img=PhotoImage(file="load.png")
    labelimg1=Label(root,width=626,height=417,image=img)
    labelimg1.place(x=0,y=0)
    text=''
    for i in v:
        text+=i+' library missing\n'
    if len(v)==1 and not(k):
        text+='Please download it to continue\n\n'
    elif len(v)==1:
        text+='Please download it to continue'
    elif len(v)>1 and not(k):
        text+='Please download them to continue\n\n'
    elif len(v)>1:
        text+='Please download them to continue'
    if not(k):
        text+='No Internet'
    label=tk.Label(root,text=text,bg="#1c1c1c",fg="white",font=("Arial",20))
    label.pack(side="top",pady=50)
    button=tk.Button(root,text="Exit",command=root.destroy)
    button.pack(side="bottom",pady=20)
    root.mainloop()
else:
    #if all libraries present
    def progress_bar():
        def close_progress():
            root.destroy()

        root=tk.Tk()
        root.title("Progress Bar")
        screen_width=root.winfo_screenwidth()
        screen_height=root.winfo_screenheight()
        x=(screen_width/2)-(626/2)
        y=(screen_height/2)-(417/2)
        root.geometry('%dx%d+%d+%d'%(626,417,x,y))
        root.resizable(width=0,height=0)
        img=PhotoImage(file="load2.png")
        labelimg1=Label(root,width=626,height=417,image=img)
        labelimg1.place(x=0,y=0)
        loading_label=Label(root,text="Loading... Please Wait",font=("Arial", 8),foreground="white",background="#1c1c1c")
        loading_label.pack(pady=5)
        from tkinter import ttk
        style=ttk.Style()
        style.theme_use('default')
        style.configure("black.Horizontal.TProgressbar",foreground='black',background='white')
        progress_bar=ttk.Progressbar(root,style="black.Horizontal.TProgressbar",orient="horizontal",length=200,mode="indeterminate",maximum=90,value=0)
        progress_bar.pack(pady=10)
        k=round(tim(),3)
        k=int(k*3000+500)
        root.after(k,close_progress)
        
        def update_progress():
            progress_bar.step(1)
            percentage=progress_bar['value']
            progress_bar['value']+=1
            if progress_bar['value']<100:
                root.after(50,update_progress)
        root.after(50,update_progress)
        root.mainloop()

    progress_bar()
