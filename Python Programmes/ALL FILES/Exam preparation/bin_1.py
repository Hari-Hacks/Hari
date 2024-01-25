import pickle
with open('EMPLOYEE.dat','wb') as f:
    l=[]
    while True:
        n=input('Enter your name:')
        a=int(input('Enter your age:'))
        dept=input('Enter your department:')
        desig=input('Enter your Designation:')
        sal=int(input('Enter your salary:'))
        l.append([n,a,dept,desig,sal])
        pickle.dump([n,a,dept,desig,sal],f)
        ch=input('y/n:')
        if ch.lower()=='n':
            break
print('input vanguna records')
print(l)
print('''1. details of manager sal > 50000 in finance and admin
2.delete details of retired employees(58 and above)
3.exit''')
while True:
    q=int(input('Enter the menu code:'))
    if q==1:
        try:
            while True:
                with open('EMPLOYEE.dat','rb') as f:
                    l=[]
                    l1=pickle.load(f)
                    l.append(l1)
        except EOFerror:
            pass
        except:
            pass
        print('bin filea dump aana rec')
        print(l)
        for  i in l:
            print(i)
            if (i[2].lower()=='finance' or i[2].lower()=='admin') and (i[3].lower()=='manager') and (i[4] > 50000):
                print(i)
                print(i[0],i[1],i[2],i[3],i[4],sep=' : ')
        
    elif q==2:
        try:
            while True:
                with open('EMPLOYEE.dat','rb') as f:
                    l=[]
                    l1=pickle.load(f)
                    l.append(l1)
        except EOFerror:
            pass
        except:
            pass
        print('bin filea dump aana rec')
        print(l)
        for i in l:
            print(i)
            if i[1] >= 58:
                print(i)
                print(i[0],i[1],i[2],i[3],i[4],sep=' : ')
                l.remove(i)
        with open('EMPLOYEE.dat','wb') as f:
            for i in l:
                pickle.dump(i,f)
    elif q==3:
        print('Program Ended')
        break
    elif 1<q>3:
        print('Invalid Menu Code')
