import mysql.connector as mc
from tkinter import *
import I1,I2
import E
import pyperclip
import pickle
import os
#Importing the files containing the interface code and encryption code

cn=mc.connect(host='sql.freedb.tech',user='freedb_iehwf',password='NdVBt%!EkGepQ@4',database='freedb_XII Project')
cr=cn.cursor()

def conn():
    #To check if the connection is intact(as there is possibility of timeout
    global cn
    global cr
    cn=mc.connect(host='sql.freedb.tech',user='freedb_iehwf',password='NdVBt%!EkGepQ@4',database='freedb_XII Project')
    cr=cn.cursor()
    cr.execute('Create table if not exists Credentials (\
Username varchar(30) Primary key, \
Password1 varchar(30), \
Password2 varchar(30), \
Password3 varchar(30), \
Password4 varchar(30), \
Password5 varchar(30))')
conn()
flag=0
#To ensure 1st loop is running till correct credentials mentioned
t=1
#to ensure only 3 times the user is allowed to enter details

def Check(L):
    #To check if entered credentials are correct
    def check():
        if cn.is_connected:
            pass
        else:
            conn()
            
    global flag
    global t
    global f
    
    check()
    cr.execute("Select * from Credentials where username='{}'".format(L[0]))
    res=cr.fetchall()
    
    if res==[]:
        #'Invalid Username' as no matches
        f=-3
        t+=1
    else:
        
        #Entered password in ps
        #Correct password in L1
        L1=[]
        for i in range(1,6):
            L1+=[res[0][i]]

        ps=L[1]
        x=E.hs_passverify(L1,ps)
        #Returns True if password is corect
        
        if x:
            #print('Credentials Valid')
            flag=1
            #1st loop broken and proceed to 2nd stage(where encryption occurs)
        else:
            #print('Invalid Password')
            f=-4
            t+=1

f=None
#To print things like invalid username,password,etc

def Create(L):
    #To create the username and password and store in sql database
    def check():
        if cn.is_connected:
            pass
        else:
            conn()
    
    global t
    global f
    
    check()
    u=L[0]
    p=L[1]
    #p contains the user entered password
    sp=E.hs_hashpass(p)
    #sp has the hashed password
    
    check()
    cr.execute("Select * from Credentials where username='{}'".format(u))
    res=cr.fetchall()
    if res==[]:
            check()
            cr.execute('''Insert into Credentials values('{}','{}','{}','{}','{}','{}')'''.format(u,sp[0],sp[1],sp[2],sp[3],sp[4]))
            f=-1
            cn.commit()

            #Username and password created successfully
    else:
            f=-2
            #Username exists already
    

def Disp(o,s=''):
    l=['Encrypted message','Decrypted message','Correct encrypted message','Incorrect encrypted message','','File encrypted successfully and stored in the same folder','File decrypted successfully and stored in the same folder','File authenticated successfully','File not Found','File was not decryptable','Incorrect File Type']
    j=['Click to copy','Click to copy','Click to exit','Click to exit','','Click to exit','Click to exit','Click to exit','Click to exit','Click to exit','Click to exit']
    def des():
        n=o
        if n==0 or n==1:
            pyperclip.copy(s)
            win.destroy()
        else:
            win.destroy()
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
    labelimg1=Label(win,width=626,height=417,image=img)
    labelimg1.grid()

    fram2=Frame(master=win,bg='#040720')
    #To esnure all items packed in fram2
    l1=Label(master=fram2,text=l[o],fg='white',bg='#040720')
    l1.config(font=("calibri",18,'bold'))
    l1.grid(row=0,column=0,padx=10,pady=10)
    fram2.grid(row=0,column=0)
    bt=Button(master=fram2,text=j[o],command=des,bg='#040720',activebackground='cyan',fg='white')
    change_on_hover(bt,"#663399","white")
    bt.config(font=("calibri",18,'bold'),bd=0)
    bt.grid(row=1,column=0)
    
    win.mainloop()

fonts1=("Times New Roman",25,"bold")
fonts2=("Times New Roman",15,"bold")
fonts3=("Calibri",15,"bold")
def change_on_hover(button,bg,fg):
    button.bind("<Enter>",func=lambda e:button.config(background=bg, foreground=fg))
    button.bind("<Leave>",func=lambda e:button.config(background= '#040720', foreground= 'white'))

while flag==0:
    s=I1.main(t,f)
    #Run 1st screen
    
    f=0
    try:
        #Shows attribute error as some times L not defined
        #L has username and password in list
        
        if s==None:
            #s has some value when it is required that execution of window stops
            if I1.L[2]==0:
                Create(I1.L)
            if I1.L[2]==1:
                Check(I1.L)
        else:
            flag=-1
            
    except AttributeError:
        flag=-2
else:
    #Proceed to encrypt
    if flag==1:
        opt=-1
        
        #Used to input the correct option
        while opt!=3 and opt!=4:
            I2.main()
            L=I2.L
            opt=L[1]
            if opt in (5,6,7) and L[0]!=None:
                inpu=L[0]
            elif L[0]!=None:
                inpu=L[0][:-1]
            else:
                inpu=''
            ####THIS IS THE INPUT FOR YOUR Encryption code

            opt=L[1]
            if opt==0:
                #encrypt
                enc=E.se(inpu)
                if enc:
                    Disp(opt,enc)
                    
            elif opt==1:
                #Decrypt
                dec=E.sd(inpu)
                if dec:
                    Disp(opt,dec)
                else:
                    Disp(opt+2)
            elif opt==2:
                #Authenticate
                enc=E.HS_authenticateme(inpu)
                if enc:
                    Disp(opt)
                else:
                    Disp(opt+1)
                    
            elif opt==3:
                #Signout
                break
            
            elif opt==4:
                break
            elif opt==5:
            #File encryption
                try:
                    f=open(inpu,'r')
                except FileNotFoundError:
                    Disp(8)
                else:
                    r=f.read()
                    es=E.encrfile(r)
                    store=inpu.split('\\')[:-1]
                    store='\\'.join(store)+'\\encrypted.dat'
                    
                    with open(store,'wb') as f1:
                        pickle.dump([es],f1)
                    f.close()
                    Disp(5)
            elif opt==6:
            #File decrypt
                try:
                    f=open(inpu,'rb')
                except FileNotFoundError:
                    Disp(8)
                else:
                    try:
                        while True:
                            r=pickle.load(f)
                    except EOFError:
                            pass
                    else:
                        es=E.Filedecr(r[0])
                        if es:
                            pass
                        else:
                            Disp(9)
                        store=inpu.split('\\')[:-1]
                        store='\\'.join(store)+'\\decrypted.txt'
                    
                        with open(store,'w') as f1:
                            f1.write(es.strip("\'"))
                        f.close()
                        Disp(6)
            elif opt==7:
                try:
                    if inpu[-3:]=='dat':
                        f=open(inpu,'rb')
                    else:
                        Disp(10)
                        
                except FileNotFoundError:
                    Disp(8)
                else:
                    if inpu[-3:]=='dat':
                        try:
                            while True:
                                r=pickle.load(f)
                        except EOFError:
                                pass
                        
                        es=E.HS_authenticate(r[0])
                        if es:
                            Disp(7)
                        else:
                            Disp(9)
                        f.close()
               
                
