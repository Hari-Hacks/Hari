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
        win1.geometry('800x600')
        win1.resizable(width=0,height=0)
        win1.config(bg='black')
        win1.grid_rowconfigure(0,weight=1)
        win1.grid_columnconfigure(0,weight=1)
        fram3=Frame(master=win1)
        l=Label(master=fram3,text='Enter Text',fg='white',bg='black')
        l.grid(row=0,column=0,padx=10,pady=10)
        e=Text(master=fram3)
        b2=Button(master=fram3,text='Submit',command=get,activebackground='cyan')
        b3=Button(text='X',command=destroy1,bg='red',activebackground='red')
        b3.place(x=750,y=10)
        e.grid(row=0,column=1,padx=10,pady=10)
        b2.grid(row=3,column=0,padx=10,pady=10)
        fram3.grid(row=0,column=0)
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
        win1.geometry('800x600')
        win1.resizable(width=0,height=0)
        win1.config(bg='black')
        win1.grid_rowconfigure(0,weight=1)
        win1.grid_columnconfigure(0,weight=1)
        fram3=Frame(master=win1)
        l=Label(master=fram3,text='Enter Text',fg='white',bg='black')
        l.grid(row=0,column=0,padx=10,pady=10)
        e=Text(master=fram3)
        b2=Button(master=fram3,text='Submit',command=get,activebackground='cyan')
        b3=Button(text='X',command=destroy1,bg='red',activebackground='red')
        b3.place(x=750,y=10)
        e.grid(row=0,column=1,padx=10,pady=10)
        b2.grid(row=3,column=0,padx=10,pady=10)
        fram3.grid(row=0,column=0)
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
        win1.geometry('800x600')
        win1.resizable(width=0,height=0)
        win1.config(bg='black')
        win1.grid_rowconfigure(0,weight=1)
        win1.grid_columnconfigure(0,weight=1)
        fram3=Frame(master=win1)
        l=Label(master=fram3,text='Enter Text',fg='white',bg='black')
        l.grid(row=0,column=0,padx=10,pady=10)
        e=Text(master=fram3)
        b2=Button(master=fram3,text='Submit',command=get,activebackground='cyan')
        b3=Button(text='X',command=destroy1,bg='red',activebackground='red')
        b3.place(x=750,y=10)
        e.grid(row=0,column=1,padx=10,pady=10)
        b2.grid(row=3,column=0,padx=10,pady=10)
        fram3.grid(row=0,column=0)
        win1.mainloop()
    def sgout():
        global L
        win.destroy()
        L=[None,3]
    def destroy():
        global L
        win.destroy()
        L=[None,4]
    if dec==None:
        pass
    else:
        decryop(dec)
        return None
    win=Tk()
    win.geometry('800x600')
    win.resizable(width=0,height=0)
    win.config(bg='black')
    win.grid_rowconfigure(0,weight=1)
    win.grid_columnconfigure(0,weight=1)
    fram2=Frame(master=win,bg='black')
    l=Label(master=fram2,text='Choose option',fg='white',bg='black')
    b1=Button(master=fram2,text='Encrypt',command=encry,activebackground='cyan')
    b2=Button(master=fram2,text='Decrypt',command=decryip,activebackground='cyan')
    b3=Button(master=fram2,text='Authenticate',command=auth,activebackground='cyan')
    b4=Button(master=fram2,text='Sign Out',command=sgout,activebackground='cyan')

    b5=Button(text='X',command=destroy,bg='red',activebackground='red')
    b5.place(x=750,y=10)
    l.grid(row=0,column=0,padx=10,pady=10)
    b1.grid(row=1,column=0,padx=10,pady=10)
    b2.grid(row=2,column=0,padx=10,pady=10)
    b3.grid(row=3,column=0,padx=10,pady=10)
    b4.grid(row=4,column=0,padx=10,pady=10)

    fram2.grid(row=0,column=0)
    win.mainloop()





