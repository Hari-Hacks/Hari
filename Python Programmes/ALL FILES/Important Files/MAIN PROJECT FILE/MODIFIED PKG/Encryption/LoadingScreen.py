import tkinter as tk
from tkinter import ttk
from random import random as tim
def progress_bar():
    def close_progress():
        root.destroy()
    root = tk.Tk()
    root.title("Progress Bar")
    root.geometry("600x400")
    root.resizable(False,False)
    root.configure(bg="#1c1c1c")
    loading_label=ttk.Label(root,text="Checking for libraries ...",font=("Arial", 8),foreground="white",background="#1c1c1c")
    loading_label.pack(pady=5)
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
try:
    import tkinter
except:v.append('tkinter')
try:
    import mysql.connector
except:v.append('mysql.connector')
try:
    import pyperclip
except:v.append('pyperclip')

if v:
    # Create the window after loading
    #if library unavailble
    window=tk.Tk()
    window.title("Appropriate Libraries Unavailable")
    window.configure(bg="#1c1c1c")
    window.geometry("450x300")
    text=''
    for i in v:
        text+=i+'  library missing\n'
    text+='Please download them to continue'
    label=tk.Label(window,text=text,bg="#1c1c1c",fg="white",font=("Arial",20))
    label.pack(side="top",pady=50)
    button=tk.Button(window,text="Exit",command=window.destroy)
    button.pack(side="bottom",pady=20)
    window.mainloop()
else:
    #if all libraries present
    def progress_bar():
        def close_progress():
            root.destroy()

        root=tk.Tk()
        root.title("Progress Bar")
        root.geometry("600x400")
        root.resizable(False,False)
        root.configure(bg="#1c1c1c")#black theme
        loading_label=ttk.Label(root,text="Loading... Please Wait",font=("Arial", 8),foreground="white",background="#1c1c1c")
        loading_label.pack(pady=5)
        style=ttk.Style()
        style.theme_use('default')
        style.configure("black.Horizontal.TProgressbar",foreground='black',background='white')
        progress_bar=ttk.Progressbar(root,style="black.Horizontal.TProgressbar",orient="horizontal",length=200,mode="indeterminate",maximum=90,value=0)
        progress_bar.pack(pady=10)
        k=round(tim(),3)
        k=int(k*3000+250)
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
