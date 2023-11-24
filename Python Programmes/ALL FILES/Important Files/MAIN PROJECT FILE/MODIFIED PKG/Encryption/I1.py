from tkinter import *
def main(t,f):
    #gets executed when called in M1
    if t<4:
        #Only when no. of tries < 3
        flag=0
        def new1():
            #To create new username
            def get():
                #to get the textbox entry
                if e.get() and e1.get():
                    us=e.get()
                    pw=e1.get()
                    e.delete(0,END)
                    e1.delete(0,END)
                    global L
                    L=[us,pw,0]
                    win1.destroy()
            def destroy1():
                win1.destroy()
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
            
            fram3=Frame(master=win1,bg="#040720")
            
            fram4=Frame(master=win1,bg="#040720")
            
            l=Label(master=fram3,text='Enter new username',fg='white',bg='#040720')
            l.config(font=fonts3)
            
            l1=Label(master=fram3,text='Enter new password',fg='white',bg='#040720')
            l1.config(font=fonts3)
            
            l.grid(row=0,column=0,padx=10,pady=10)
            
            l1.grid(row=1,column=0,padx=10,pady=10)
            
            e=Entry(master=fram3,font=("Calibri",11))
            e.config(width=35,bg="#BCC6CC",bd=4)
            
            e1=Entry(master=fram3,font=("Calibri",11), show = '*')
            e1.config(width=35,bg="#BCC6CC",bd=4)
            
            b2=Button(master=fram4,text='Create',command=get,bg="#040720",fg="white",activebackground='cyan')
            b2.config(font=("Calibri",18,'bold'),bd=0)
            change_on_hover(b2,"#663399","white")

            b3=Button(text='X',command=destroy1,bg='red',activebackground='red')
            b3.place(x=590,y=10)

            e.grid(row=0,column=1,padx=10,pady=10)

            e1.grid(row=1,column=1,padx=10,pady=10)

            b2.grid(row=0,column=0)

            fram3.place(x=75,y=160)

            fram4.place(x=270,y=280)

            win1.mainloop()

        def login():
            #To login
            def get():
                if e.get() and e1.get():
                    #to get the textbox entry
                    us=e.get()
                    pw=e1.get()
                    e.delete(0,END)
                    e1.delete(0,END)
                    global L
                    L=[us,pw,1]
                    win1.destroy()
            def destroy1():
                win1.destroy()
                return 1
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

            fram3=Frame(master=win1,bg="#040720")

            fram4=Frame(master=win1,bg="#040720")

            l=Label(master=fram3,text='Enter username',fg='white',bg='#040720')
            l.config(font=fonts3)

            l1=Label(master=fram3,text='Enter password',fg='white',bg='#040720')
            l1.config(font=fonts3)

            l.grid(row=0,column=0,padx=10,pady=10)

            l1.grid(row=1,column=0,padx=10,pady=10)

            e=Entry(master=fram3,font=("Calibri",11))
            e.config(width=25,bg="#BCC6CC",bd=4)

            e1=Entry(master=fram3,font=("Calibri",11), show ='*')
            e1.config(width=25,bg="#BCC6CC",bd=4)

            b2=Button(master=fram4,text='Login',command=get,bg="#040720",fg="white",activebackground='cyan')
            b2.config(font=("Calibri",18,'bold'),bd=0)
            change_on_hover(b2,"#663399","white")

            b3=Button(text='X',command=destroy1,bg='red',activebackground='red')
            b3.place(x=590,y=10)

            e.grid(row=0,column=1,padx=10,pady=10)

            e1.grid(row=1,column=1,padx=10,pady=10)

            b2.grid(row=0,column=0)

            fram3.place(x=130,y=160)

            fram4.place(x=270,y=280)

            win1.mainloop()
            
        def destroy1():
            #For red button
            win.destroy()
            return 1

        def change_on_hover(button,bg,fg):
            button.bind("<Enter>",func=lambda e:button.config(background=bg, foreground=fg))
            button.bind("<Leave>",func=lambda e:button.config(background= '#040720', foreground= 'white'))
        
        fonts1=("Times New Roman",25,"bold")
        fonts2=("Times New Roman",15,"bold")
        fonts3=("Calibri",15,"bold")

        win=Tk()
        screen_width = win.winfo_screenwidth()
        screen_height = win.winfo_screenheight()
        x = (screen_width/2) - (626/2)
        y = (screen_height/2) - (417/2)
        win.geometry('%dx%d+%d+%d' % (626, 417, x, y))
        #For size of window
        win.resizable(width=0,height=0)
        #For ensuring resizing doesn't occur
        win.config(bg='black')
        #To configure colour of window
        win.grid_rowconfigure(0,weight=1)
        #For grid options weight=1 ensures grid can rescale with increas in row count
        win.grid_columnconfigure(0,weight=1)
        #For grid options weight=1 ensures grid can rescale with increas in row count

        img=PhotoImage(file="back.png")
        labelimg=Label(win,width=626,height=417,image=img)
        labelimg.grid()

        fram2=Frame(master=win,bg="#040720")
        #To esnure all items packed in fram2

        l=Label(master=fram2,text='MENU',fg='white',bg="#040720")
        l.config(font=fonts1)

        if f==-1:
            Lab=Label(master=fram2,text='User created succesfully',fg='white',bg='#040720')
            Lab.config(font=fonts2)
            Lab.grid(row=3,column=0,padx=10,pady=10)
        elif f==-2:
            Lab=Label(master=fram2,text='Username already taken',fg='white',bg='#040720')
            Lab.config(font=fonts2)
            Lab.grid(row=3,column=0,padx=10,pady=10)
        elif f==-3:
            Lab=Label(master=fram2,text='Invalid Username',fg='white',bg='#040720')
            Lab.config(font=fonts2)
            Lab.grid(row=3,column=0,padx=10,pady=10)
        elif f==-4:
            Lab=Label(master=fram2,text='Invalid Password',fg='white',bg='#040720')
            Lab.config(font=fonts2)
            Lab.grid(row=3,column=0,padx=10,pady=10)

        b1=Button(master=fram2,text='New User',command=new1,bg="#040720",fg="white",
                          activebackground='cyan',activeforeground='black')
        b1.config(font=fonts3,bd=0,width=10)
        
        b2=Button(master=fram2,text='Login',command=login,bg="#040720",fg="white",
                          activebackground='cyan',activeforeground='black')
        b2.config(font=fonts3,bd=0,width=10)

        l.grid(row=0,column=0,padx=10,pady=10)

        b1.grid(row=1,column=0,padx=10,pady=10)
        b2.grid(row=2,column=0,padx=10,pady=10)
        change_on_hover(b1,"#663399","white")
        change_on_hover(b2,"#663399","white")

        fram3=Frame(win,bg="#040720")
        fram3.config(height=5,width=5)
        fram3.place(x=590,y=5)

        b3=Button(fram3,text='X',font=("Calibri",15),command=destroy1,bg='#040720',fg="white",activebackground='red')
        change_on_hover(b3,"red","#040720")
        b3.grid()

        fram2.grid(row=0,column=0)

        win.mainloop()
            
    else:
        fonts1=("Times New Roman",25,"bold")
        fonts2=("Times New Roman",15,"bold")
        fonts3=("Calibri",15,"bold")
        #For the window after 3 tries are used up
        def destroy1():
            win.destroy()
            return 1
        def change_on_hover(button,bg,fg):
            button.bind("<Enter>",func=lambda e:button.config(background=bg, foreground=fg))
            button.bind("<Leave>",func=lambda e:button.config(background= '#040720', foreground= 'white'))
        win=Tk()
        win.geometry('626x417')
        win.resizable(width=0,height=0)
        win.config(bg='black')
        win.grid_rowconfigure(0,weight=1)
        win.grid_columnconfigure(0,weight=1)

        img=PhotoImage(file="back.png")
        labelimg=Label(win,width=626,height=417,image=img)
        labelimg.grid()

        fram=Frame(win,bg="#040720")
        fram.grid(row=0,column=0)

        l=Label(master=fram,text='Too many attempts',fg='white',bg='#040720')
        l.config(font=fonts1)

        l1=Label(fram,text="Try again next time",fg='white',bg="#040720")
        l1.config(font=fonts1)

        b3=Button(text='X',command=destroy1,bg='#040720',fg="white",activebackground='red')
        change_on_hover(b3,"red","white")

        l.grid(row=0,column=0,padx=10,pady=10)
        l1.grid(row=1,column=0)
        b3.place(x=590,y=10)
        fram.place()
        win.mainloop()

