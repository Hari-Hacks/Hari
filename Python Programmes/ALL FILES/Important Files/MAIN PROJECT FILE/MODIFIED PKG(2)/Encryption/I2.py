from tkinter import *
def choose_file():
    from tkinter import filedialog
    file_name=filedialog.askopenfilename()
    #Function returns the file's name
    return file_name
def main(dec=None):
    def encry():
        def get1():
            return e1.get()
        def get():
            if e.get('1.0'):
                #Checks if 1st line zeroth position 
                det=e.get('1.0','end')
                e.delete('1.0','end')
                skey=get1()
                global L
                L=[det,0,skey]
                win1.destroy()
        def destroy1():
            global L
            win1.destroy()
            L=[None,4,'']
            
        win.destroy()
        win1=Tk()
        screen_width = win1.winfo_screenwidth()
        screen_height = win1.winfo_screenheight()
        x = (screen_width/2) - (626/2)
        y = (screen_height/2) - (417/2)
        win1.geometry('%dx%d+%d+%d' % (626, 417, x, y))
        win1.resizable(width=0,height=0)
        win1.config(bg='black')
        win1.grid_rowconfigure(0,weight=1)
        win1.grid_columnconfigure(0,weight=1)

        img=PhotoImage(file="back.png")
        labelimg1=Label(win1,width=626,height=417,image=img)
        labelimg1.grid()

        l=Label(win1,text='Enter Text',fg='white',bg='#040720')
        l.config(font=("calibri",18,'bold'),height=1,width=10)
        l.place(x=240,y=25)
        l1=Label(master=win1,text='Secret Key (Optional)',fg='white',bg='#040720')
        l1.place(x=210,y=275)
        e1=Entry(win1,textvariable=get1,font=fonts3)
        e1.place(x=210,y=300)
        e=Text(win1,relief="raised",font=fonts3)
        e.config(bg="#BCC6CC",bd=10)
        e.place(x=115, y=65, height=200, width=400)

        b2=Button(win1,text='Submit',command=get,bg='#040720',fg="white",activebackground='cyan',activeforeground="black")
        b2.config(font=("calibri",18,'bold'),bd=0)
        b2.place(x=264,y=340)
        change_on_hover(b2,"#663399","white")

        b3=Button(text='X',command=destroy1,bg='red',fg="black",activebackground='red')
        b3.place(x=590,y=10)

        win1.mainloop()
        
        
    def decryip():
        def get1():
            return e1.get()
        def get():
            if e.get('1.0'):
                us=e.get('1.0','end')
                e.delete('1.0','end')
                global L
                skey=get1()
                L=[us,1,skey]
                win1.destroy()
        def destroy1():
            global L
            win1.destroy()
            L=[None,4,'']
        win.destroy()
        win1=Tk()
        screen_width = win1.winfo_screenwidth()
        screen_height = win1.winfo_screenheight()
        x = (screen_width/2) - (626/2)
        y = (screen_height/2) - (417/2)
        win1.geometry('%dx%d+%d+%d' % (626, 417, x, y))
        win1.resizable(width=0,height=0)
        win1.config(bg='black')
        win1.grid_rowconfigure(0,weight=1)
        win1.grid_columnconfigure(0,weight=1)

        img=PhotoImage(file="back.png")
        labelimg1=Label(win1,width=626,height=417,image=img)
        labelimg1.grid()

        l=Label(win1,text='Enter Text',fg='white',bg='#040720')
        l.config(font=("calibri",18,'bold'),height=1,width=10)
        l.place(x=240,y=25)
        l1=Label(master=win1,text='Secret Key (If used for encryption)',fg='white',bg='#040720')
        l1.place(x=210,y=275)
        e1=Entry(win1,textvariable=get1,font=fonts3)
        e1.place(x=210,y=300)
        e=Text(win1,relief="raised",font=fonts3)
        e.config(bg="#BCC6CC",bd=10)
        e.place(x=115, y=65, height=200, width=400)

        b2=Button(win1,text='Submit',command=get,bg='#040720',fg="white",activebackground='cyan',activeforeground="black")
        b2.config(font=("calibri",18,'bold'),bd=0)
        b2.place(x=264,y=340)
        change_on_hover(b2,"#663399","white")

        b3=Button(text='X',command=destroy1,bg='red',fg="black",activebackground='red')
        b3.place(x=590,y=10)

        win1.mainloop()

    def file_encryption():
        def get():
            #To get text in entry box
            return e.get()
        def choose_file():
            from tkinter import filedialog
            file_name=filedialog.askopenfilename()
            #Function returns the file's name
            global L
            skey=get()
            L=[file_name,5,skey]
            win1.destroy()
        def destroy1():
            global L
            win1.destroy()
            L=[None,4,'']
        win.destroy()
        
        win1=Tk()
        screen_width = win1.winfo_screenwidth()
        screen_height = win1.winfo_screenheight()
        x = (screen_width/2) - (626/2)
        y = (screen_height/2) - (417/2)
        win1.geometry('%dx%d+%d+%d' % (626, 417, x, y))
        win1.resizable(width=0,height=0)
        win1.config(bg='black')
        win1.grid_rowconfigure(0,weight=1)
        win1.grid_columnconfigure(0,weight=1)

        img=PhotoImage(file="back.png")
        labelimg1=Label(win1,width=626,height=417,image=img)
        labelimg1.grid()
    
        l1=Label(master=win1,text='Secret Key (Optional)',fg='white',bg='#040720')
        l1.place(x=210,y=158)
        l1=Label(master=win1,text='Enter secret key before choosing',fg='white',bg='#040720')
        l1.place(x=230,y=274)
        e=Entry(win1,textvariable=get,font=fonts3)
        e.place(x=210,y=180)
        b4=Button(win1,text='Choose File',command=choose_file,activebackground='cyan',bg="#040720",fg="white")
        b4.config(font=("Calibri",18,'bold'),bd=0)
        b4.place(x=250,y=230)
        change_on_hover(b4,"#663399","white")

        b3=Button(text='X',command=destroy1,bg='red',activebackground='red')
        b3.place(x=590,y=10)
        win1.mainloop()

    def file_decryption():
        def get():
            return e.get()
        def choose_file():
            from tkinter import filedialog
            file_name=filedialog.askopenfilename()
            #Function returns the file's name
            global L
            skey=get()
            L=[file_name,6,skey]
            win1.destroy()
        def destroy1():
            global L
            win1.destroy()
            L=[None,4,'']
        win.destroy()
        win1=Tk()
        screen_width = win1.winfo_screenwidth()
        screen_height = win1.winfo_screenheight()
        x = (screen_width/2) - (626/2)
        y = (screen_height/2) - (417/2)
        win1.geometry('%dx%d+%d+%d' % (626, 417, x, y))
        win1.resizable(width=0,height=0)
        win1.config(bg='black')
        win1.grid_rowconfigure(0,weight=1)
        win1.grid_columnconfigure(0,weight=1)

        img=PhotoImage(file="back.png")
        labelimg1=Label(win1,width=626,height=417,image=img)
        labelimg1.grid()
        #write get function########
        l1=Label(master=win1,text='Secret Key (If used for encryption)',fg='white',bg='#040720')
        l1.place(x=210,y=158)
        l1=Label(master=win1,text='Enter secret key before choosing',fg='white',bg='#040720')
        l1.place(x=230,y=274)
        e=Entry(win1,textvariable=get,font=fonts3)
        e.place(x=210,y=180)
        b4=Button(win1,text='Choose File',command=choose_file,activebackground='cyan',bg="#040720",fg="white")
        b4.config(font=("Calibri",18,'bold'),bd=0)
        b4.place(x=250,y=230)
        change_on_hover(b4,"#663399","white")

        b3=Button(text='X',command=destroy1,bg='red',activebackground='red')
        b3.place(x=590,y=10)
        win1.mainloop()
    def file_authentication():
        def get():
            return e.get()
        def choose_file():
            from tkinter import filedialog
            file_name=filedialog.askopenfilename()
            #Function returns the file's name
            global L
            skey=get()
            L=[file_name,7,skey]
            win1.destroy()
        def destroy1():
            global L
            win1.destroy()
            L=[None,4,'']
        win.destroy()
        win1=Tk()
        screen_width = win1.winfo_screenwidth()
        screen_height = win1.winfo_screenheight()
        x = (screen_width/2) - (626/2)
        y = (screen_height/2) - (417/2)
        win1.geometry('%dx%d+%d+%d' % (626, 417, x, y))
        win1.resizable(width=0,height=0)
        win1.config(bg='black')
        win1.grid_rowconfigure(0,weight=1)
        win1.grid_columnconfigure(0,weight=1)

        img=PhotoImage(file="back.png")
        labelimg1=Label(win1,width=626,height=417,image=img)
        labelimg1.grid()

        skey=''
        l1=Label(master=win1,text='Secret Key (If used for encryption)',fg='white',bg='#040720')
        l1.place(x=210,y=158)
        l1=Label(master=win1,text='Enter secret key before choosing',fg='white',bg='#040720')
        l1.place(x=230,y=274)
        e=Entry(win1,textvariable=get,font=fonts3)
        e.place(x=210,y=180)
        b4=Button(win1,text='Choose File',command=choose_file,activebackground='cyan',bg="#040720",fg="white")
        b4.config(font=("Calibri",18,'bold'),bd=0)
        b4.place(x=250,y=230)
        change_on_hover(b4,"#663399","white")

        b3=Button(text='X',command=destroy1,bg='red',activebackground='red')
        b3.place(x=590,y=10)
        win1.mainloop()
    
    def auth():
        def get1():
            return e1.get()
        def get():
            if e.get('1.0'):
                us=e.get('1.0','end')
                e.delete('1.0','end')
                global L
                skey=get1()
                L=[us,2,skey]
                win1.destroy()
        def destroy1():
            global L
            win1.destroy()
            L=[None,4,'']
        win.destroy()
        
        win1=Tk()
        screen_width = win1.winfo_screenwidth()
        screen_height = win1.winfo_screenheight()
        x = (screen_width/2) - (626/2)
        y = (screen_height/2) - (417/2)
        win1.geometry('%dx%d+%d+%d' % (626, 417, x, y))
        win1.resizable(width=0,height=0)
        win1.config(bg='black')
        win1.grid_rowconfigure(0,weight=1)
        win1.grid_columnconfigure(0,weight=1)

        img=PhotoImage(file="back.png")
        labelimg1=Label(win1,width=626,height=417,image=img)
        labelimg1.grid()

        l=Label(win1,text='Enter Text',fg='white',bg='#040720')
        l.config(font=("calibri",18,'bold'),height=1,width=10)
        l.place(x=240,y=25)
        l1=Label(master=win1,text='Secret Key (If used for encryption)',fg='white',bg='#040720')
        l1.place(x=210,y=275)
        e1=Entry(win1,textvariable=get1,font=fonts3)
        e1.place(x=210,y=300)
        e=Text(win1,relief="raised",font=fonts3)
        e.config(bg="#BCC6CC",bd=10)
        e.place(x=115, y=65, height=200, width=400)

        b2=Button(win1,text='Submit',command=get,bg='#040720',fg="white",activebackground='cyan',activeforeground="black")
        b2.config(font=("calibri",18,'bold'),bd=0)
        b2.place(x=264,y=340)
        change_on_hover(b2,"#663399","white")

        b3=Button(text='X',command=destroy1,bg='red',fg="black",activebackground='red')
        b3.place(x=590,y=10)

        win1.mainloop()
        
    def sgout():
        global L
        win.destroy()
        L=[None,3,'']
    def destroy():
        global L
        win.destroy()
        L=[None,4,'']
    def change_on_hover(button,bg,fg):
            button.bind("<Enter>",func=lambda e:button.config(background=bg, foreground=fg))
            button.bind("<Leave>",func=lambda e:button.config(background= '#040720', foreground= 'white'))
    if dec==None:
        pass
    else:
        decryop(dec)
        return None

    fonts1=("Times New Roman",25,"bold")
    fonts2=("Times New Roman",15,"bold")
    fonts3=("Calibri",15,"bold")

    win=Tk()
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x = (screen_width/2) - (626/2)
    y = (screen_height/2) - (417/2)
    win.geometry('%dx%d+%d+%d' % (626, 417, x, y))
    win.resizable(width=0,height=0)
    win.config(bg='black')
    win.grid_rowconfigure(0,weight=1)
    win.grid_columnconfigure(0,weight=1)
    
    img=PhotoImage(file="back.png")
    labelimg1=Label(win,width=626,height=417,image=img)
    labelimg1.grid()
    
    fram2=Frame(master=win,bg='#040720')
    
    l=Label(master=fram2,text='MENU',fg='white',bg='#040720')
    l.config(font=fonts1)
    b1=Button(master=fram2,text='Encrypt',command=encry,bg='#040720',fg='white',activebackground='cyan')
    b1.config(font=fonts3,bd=0,width=15)
    change_on_hover(b1,"#663399","white")
        
    b2=Button(master=fram2,text='Decrypt',command=decryip,bg='#040720',fg='white',activebackground='cyan')
    b2.config(font=fonts3,bd=0,width=15)
    change_on_hover(b2,"#663399","white")
    
    b3=Button(master=fram2,text='Authenticate',command=auth,bg='#040720',fg='white',activebackground='cyan')
    b3.config(font=fonts3,bd=0,width=15)
    change_on_hover(b3,"#663399","white")

    b6=Button(master=fram2,text='Encrypt Text File',command=file_encryption,bg='#040720',fg='white',activebackground='cyan')
    b6.config(font=fonts3,bd=0,width=15)
    change_on_hover(b6,"#663399","white")

    b7=Button(master=fram2,text='Decrypt File',command=file_decryption,bg='#040720',fg='white',activebackground='cyan')
    b7.config(font=fonts3,bd=0,width=15)
    change_on_hover(b7,"#663399","white")

    b8=Button(master=fram2,text='Authenticate File',command=file_authentication,bg='#040720',fg='white',activebackground='cyan')
    b8.config(font=fonts3,bd=0,width=15)
    change_on_hover(b8,"#663399","white")
    
    b4=Button(master=fram2,text='Sign Out',command=sgout,bg='#040720',fg='white',activebackground='cyan')
    b4.config(font=fonts3,bd=0,width=15)
    change_on_hover(b4,"#663399","white")

    fram3=Frame(win,bg="#040720")
    fram3.config(height=5,width=5)
    
    b5=Button(fram3,text='X',command=destroy,bg='#040720',fg="white",activebackground='red')
    change_on_hover(b5,"red","#040720")
    b5.grid()
    
    l.grid(row=0,column=0,padx=10,pady=15)
    b1.grid(row=1,column=0,padx=10,pady=2)
    b2.grid(row=2,column=0,padx=10,pady=2)
    b3.grid(row=3,column=0,padx=10,pady=2)
    b4.grid(row=7,column=0,padx=10,pady=2)
    b6.grid(row=4,column=0,padx=10,pady=2)
    b7.grid(row=5,column=0,padx=10,pady=2)
    b8.grid(row=6,column=0,padx=10,pady=2)
    fram2.place(x=220,y=24,height=370,width=180)

    win.mainloop()
