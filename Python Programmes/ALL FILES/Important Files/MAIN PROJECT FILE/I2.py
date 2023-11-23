from tkinter import *
def main(dec=None):
    def encry():
        def get():
            if e.get('1.0'):
                #Checks if 1st line zeroth position 
                det=e.get('1.0','end')
                e.delete('1.0','end')
                global L
                L=[det,0]
                win1.destroy()
        def destroy1():
            global L
            win1.destroy()
            L=[None,4]
            
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
        l.config(font=("calibri",18),height=1,width=10)
        l.place(x=240,y=100)

        b2=Button(win1,text='Submit',command=get,bg='#040720',fg="white",activebackground='cyan',activeforeground="black")
        b2.config(font=("calibri",18),bd=0)
        b2.place(x=264,y=270)
        change_on_hover(b2,"#663399","white")
    
        e=Text(win1,relief="raised",font=fonts3)
        e.config(bg="#BCC6CC",bd=10)
        e.place(x=205, y=150, height=100, width=200)
        
        b3=Button(text='X',command=destroy1,bg='red',fg="black",activebackground='red')
        b3.place(x=590,y=10)

        win1.mainloop()
        
    def decryip():
        def get():
            if e.get('1.0'):
                us=e.get('1.0','end')
                e.delete('1.0','end')
                global L
                L=[us,1]
                win1.destroy()
        def destroy1():
            global L
            win1.destroy()
            L=[None,4]
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
        l.config(font=("calibri",18),height=1,width=10)
        l.place(x=240,y=100)

        e=Text(win1,relief="raised",font=fonts3)
        e.config(bg="#BCC6CC",bd=10)
        e.place(x=205, y=150, height=100, width=200)
        
        b2=Button(win1,text='Submit',command=get,bg='#040720',fg="white",activebackground='cyan',activeforeground="black")
        b2.config(font=("calibri",18),bd=0)
        b2.place(x=264,y=270)
        change_on_hover(b2,"#663399","white")

        b3=Button(text='X',command=destroy1,bg='red',fg="black",activebackground='red')
        b3.place(x=590,y=10)
        
        win1.mainloop()
    def decryop():
        def destroy1():
            global L
            win1.destroy()
            L=[None,4]
        def exit():
            global L
            win1.destroy()
            L=[None,-1]
        win.destroy()
        win1=Tk()
        win1.geometry('800x600')
        win1.resizable(width=0,height=0)
        win1.config(bg='black')
        win1.grid_rowconfigure(0,weight=1)
        win1.grid_columnconfigure(0,weight=1)
        fram3=Frame(master=win1)
        l=Label(master=fram3,text='Enter Text',fg='white',bg='black')
        l.grid(row=0,column=0,padx=10,pady=10)
        l1=Label(master=fram3,text=dec,fg='white',bg='black')
        b2=Button(master=fram3,text='Exit',command='exit',activebackground='cyan')
        b3=Button(text='X',command=destroy1,bg='red',activebackground='red')
        b3.place(x=750,y=10)
        l1.grid(row=0,column=1,padx=10,pady=10)
        b2.grid(row=3,column=0,padx=10,pady=10)
        fram3.grid(row=0,column=0)
        win1.mainloop()
    
    def auth():
        def get():
            if e.get('1.0'):
                us=e.get('1.0','end')
                e.delete('1.0','end')
                global L
                L=[us,2]
                win1.destroy()
        def destroy1():
            global L
            win1.destroy()
            L=[None,4]
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
        
        '''fram3=Frame(master=win1)
        l=Label(master=fram3,text='Enter Text',fg='white',bg='black')
        l.grid(row=0,column=0,padx=10,pady=10)
        e=Text(master=fram3)
        b2=Button(master=fram3,text='Submit',command=get,activebackground='cyan')
        b3=Button(text='X',command=destroy1,bg='red',activebackground='red')
        b3.place(x=750,y=10)
        e.grid(row=0,column=1,padx=10,pady=10)
        b2.grid(row=3,column=0,padx=10,pady=10)
        fram3.grid(row=0,column=0)'''
        
        img=PhotoImage(file="back.png")
        labelimg1=Label(win1,width=626,height=417,image=img)
        labelimg1.grid()

        l=Label(win1,text='Enter Text',fg='white',bg='#040720')
        l.config(font=("calibri",18),height=1,width=10)
        l.place(x=240,y=100)

        b2=Button(win1,text='Submit',command=get,bg='#040720',fg="white",activebackground='cyan',activeforeground="black")
        b2.config(font=("calibri",18),bd=0)
        b2.place(x=264,y=270)
        change_on_hover(b2,"#663399","white")
    
        e=Text(win1,relief="raised",font=fonts3)
        e.config(bg="#BCC6CC",bd=10)
        e.place(x=205, y=150, height=100, width=200)
        
        b3=Button(text='X',command=destroy1,bg='red',fg="black",activebackground='red')
        b3.place(x=590,y=10)
        
        win1.mainloop()
        
    def sgout():
        global L
        win.destroy()
        L=[None,3]
    def destroy():
        global L
        win.destroy()
        L=[None,4]
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
    
    b4=Button(master=fram2,text='Sign Out',command=sgout,bg='#040720',fg='white',activebackground='cyan')
    b4.config(font=fonts3,bd=0,width=15)
    change_on_hover(b4,"#663399","white")

    fram3=Frame(win,bg="#040720")
    fram3.config(height=5,width=5)
    fram3.place(x=590,y=5)
    
    b5=Button(fram3,text='X',command=destroy,bg='#040720',fg="white",activebackground='red')
    change_on_hover(b5,"red","#040720")
    b5.grid()
    
    l.grid(row=0,column=0,padx=10,pady=10)
    b1.grid(row=1,column=0,padx=10,pady=10)
    b2.grid(row=2,column=0,padx=10,pady=10)
    b3.grid(row=3,column=0,padx=10,pady=10)
    b4.grid(row=4,column=0,padx=10,pady=10)
    fram2.grid(row=0,column=0)

    win.mainloop()
main(dec=None)





