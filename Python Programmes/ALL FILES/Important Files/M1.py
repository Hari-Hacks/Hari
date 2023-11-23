import mysql.connector as mc
import I1,I2
#Importing the files containing the interface code
cn=mc.connect(host='sql.freedb.tech',user='freedb_iehwf',password='NdVBt%!EkGepQ@4',database='freedb_XII Project')
cr=cn.cursor()

def conn():
    #To check if the connection is intact(as there is possibility of timeout
    global cn
    global cr
    cn=mc.connect(host='sql.freedb.tech',user='freedb_iehwf',password='NdVBt%!EkGepQ@4',database='freedb_XII Project')
    cr=cn.cursor()
    cr.execute('Create table if not exists Credentials (Username varchar(30) Primary key, Password varchar(30) unique)')
conn()
flag=0
#To ensure 1st loop is running till correct credentials mentioned
t=1
#to ensure only 3 times the user is allowed to enter details

def Check(L):
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
        if res[0][1]==L[1]:
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
    check()
    cr.execute("Select * from Credentials where username='{}'".format(u))
    res=cr.fetchall()
    if res==[]:
        cr.execute("Insert into Credentials values('{}','{}')".format(u,p))
        f=-1
        #Username and password created successfully
    else:
        f=-2
        #Username exists already

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
            inpu=L[0]
            ####THIS IS THE INPUT FOR YOUR Encryption code
            opt=L[1]
            if opt==0:pass
                #Encrypt
            elif opt==1:pass
                #Decrypt
            elif opt==2:pass
                #Authenticate
            elif opt==3:
                #Signout
                break
            elif opt==4:
                break
            
