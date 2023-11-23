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
                return 1
            win.destroy()
            win1=Tk()
            win1.geometry('800x600')
            win1.resizable(width=0,height=0)
            win1.config(bg='black')
            win1.grid_rowconfigure(0,weight=1)
            win1.grid_columnconfigure(0,weight=1)
            fram3=Frame(master=win1)
            l=Label(master=fram3,text='Enter username',fg='white',bg='black')
            l1=Label(master=fram3,text='Enter password',fg='white',bg='black')
            l.grid(row=0,column=0,padx=10,pady=10)
            l1.grid(row=1,column=0,padx=10,pady=10)
            e=Entry(master=fram3)
            e1=Entry(master=fram3)
            b2=Button(master=fram3,text='Create',command=get,activebackground='cyan')
            b3=Button(text='X',command=destroy1,bg='red',activebackground='red')
            b3.place(x=750,y=10)
            e.grid(row=0,column=1,padx=10,pady=10)
            e1.grid(row=1,column=1,padx=10,pady=10)
            b2.grid(row=3,column=0,padx=10,pady=10)
            fram3.grid(row=0,column=0)
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
            win1.geometry('800x600')
            win1.resizable(width=0,height=0)
            win1.config(bg='black')
            win1.grid_rowconfigure(0,weight=1)
            win1.grid_columnconfigure(0,weight=1)
            fram3=Frame(master=win1)
            l=Label(master=fram3,text='Enter username',fg='white',bg='black')
            l1=Label(master=fram3,text='Enter password',fg='white',bg='black')
            l.grid(row=0,column=0,padx=10,pady=10)
            l1.grid(row=1,column=0,padx=10,pady=10)
            e=Entry(master=fram3)
            e1=Entry(master=fram3)
            b2=Button(master=fram3,text='Login',command=get,activebackground='cyan')
            b3=Button(text='X',command=destroy1,bg='red',activebackground='red')
            b3.place(x=750,y=10)
            e.grid(row=0,column=1,padx=10,pady=10)
            e1.grid(row=1,column=1,padx=10,pady=10)
            b2.grid(row=3,column=0,padx=10,pady=10)
            fram3.grid(row=0,column=0)
            win1.mainloop()
            
        def destroy1():
            #For red button
            win.destroy()
            return 1
        win=Tk()
        win.geometry('800x600')
        #For size of window
        win.resizable(width=0,height=0)
        #For ensuring resizing doesn't occur
        win.config(bg='black')
        #To configure colour of window
        win.grid_rowconfigure(0,weight=1)
        #For grid options weight=1 ensures grid can rescale with increas in row count
        win.grid_columnconfigure(0,weight=1)
        #For grid options weight=1 ensures grid can rescale with increas in row count
        fram2=Frame(master=win,bg='black')
        #To esnure all items packed in fram2
        l=Label(master=fram2,text='Choose option',fg='white',bg='black')
        if f==-1:
            Lab=Label(master=fram2,text='User created succesfully',fg='white',bg='black')
            Lab.grid(row=3,column=0,padx=10,pady=10)
        elif f==-2:
            Lab=Label(master=fram2,text='Username already taken',fg='white',bg='black')
            Lab.grid(row=3,column=0,padx=10,pady=10)
        elif f==-3:
            Lab=Label(master=fram2,text='Invalid Username',fg='white',bg='black')
            Lab.grid(row=3,column=0,padx=10,pady=10)
        elif f==-4:
            Lab=Label(master=fram2,text='Invalid Password',fg='white',bg='black')
            Lab.grid(row=3,column=0,padx=10,pady=10)

        b1=Button(master=fram2,text='New User',command=new1,activebackground='cyan')
        b2=Button(master=fram2,text='Login',command=login,activebackground='cyan')
        b3=Button(text='X',command=destroy1,bg='red',activebackground='red')
        b3.place(x=750,y=10)
        l.grid(row=0,column=0,padx=10,pady=10)
        b1.grid(row=1,column=0,padx=10,pady=10)
        b2.grid(row=2,column=0,padx=10,pady=10)
        fram2.grid(row=0,column=0)
        win.mainloop()
        
    else:
        #For the window after 3 tries are used up
        def destroy1():
            win.destroy()
            return 1
        win=Tk()
        win.geometry('800x600')
        win.resizable(width=0,height=0)
        win.config(bg='black')
        win.grid_rowconfigure(0,weight=1)
        win.grid_columnconfigure(0,weight=1)
        l=Label(text='You have been locked out. Click to exit',fg='white',bg='black')
        b3=Button(text='X',command=destroy1,bg='red',activebackground='red')
        l.grid(row=0,column=0,padx=10,pady=10)
        b3.grid(row=1,column=0,padx=10,pady=10)
        win.mainloop()
