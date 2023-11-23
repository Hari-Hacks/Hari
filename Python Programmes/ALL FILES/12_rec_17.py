def Insert():
    a=input('Enter Country Name : ')
    b=input("Enter Country Capital : ")
    st.append([a,b])
    top=len(st)-1

def Delete():
    if len(st)==0:
        print("UNDERFLOW")
    else:
        top=len(st)-1
        print('Popped Item :',st[top])
        st.pop(top)
        top=len(st)-1

def Peek():
    if len(st)==0:
        print('UNDERFLOW')
    else:
        top=len(st)-1
        print('topmost element is',st[top])

def Display():
    if len(st)==0:
        print("UNDERFLOW")
    else:
        top=len(st)-1
        for k in range(top,-1,-1):
            print(st[k][0],st[k][1],sep='  ')  
st=[]
top=None

print('''
==========MENU=========
1.Insert
2.Delete
3.Display Stack
4.Peek
5.Exit''')
while True:
    c=int(input("Enter Menu Code: "))
    if c==1:
        Insert()
    elif c==2:
        Delete()
    elif c==3:
        Display()
    elif c==4:
        Peek()
    elif c==5:
        print('The Program is Ended')
        break
    else:
        print("Invalid Menu Code")