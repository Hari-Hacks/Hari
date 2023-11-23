def add():
    nam=input('Enter the subscribers name:')
    phno=int(input('Enter the phone numer:'))
    d[phno]=nam
def view():
    print(d)
def mod():
    ph=int(input('Enter the phone number of the subscriber:'))
    name=input('Enter the correct name:')
    d[ph]=name
    print('Name modified successfully')
    print(d)
def delete():
    ph=int(input('Enter the subscribers phone number:'))
    del d[ph]
    print('Deleted successfully')
    print(d)
n=int(input('Enter the number of subscribers:'))
d={}
for i in range(n):
    add()
print('''
===============MENU===============
1. ADD
2. VIEW
3. MODIFY NAME
4. DELETE
5. EXIT''')
while True:
    ch=int(input('Enter the menu code:'))
    if ch==1:
        add()
    elif ch==2:
        view()
    elif ch==3:
        mod()
    elif ch==4:
        delete()
    elif ch==5:
        print('The Program is ended')
        break
    elif ch <= 0 or ch > 5:
        print('Incorrect menu code')
        
