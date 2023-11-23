def Push():
    a=int(input("Enter the item to be pushed : "))
    st.append(a)
    top=len(st)-1
def Pop():
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
            print(st[k])
st=[]
top=None
print('''Menu
1.Push
2.Pop
3.Display Stack
4.Peek
5.Exit''')
while True:
    c=input("Choice : ")
    if c=='1':
        Push()
    elif c=='2':
        Pop()
    elif c=='3':
        Display()
    elif c=='4':
        Peek()
    elif c=='5':
        break
    else:
        print("Invalid Input")
        
