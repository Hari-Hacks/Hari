import pickle
n=int(input("Enter the number of employees : "))
with open('EMPLOYEE.DAT','wb') as f:
    for i in range(n):
        n=input("Name :")
        a=input("Age :")
        dep=input("Department :")
        des=input("Designation :")
        sal=input("Salary :")
        pickle.dump({'Name':n,'Age':a,'Department':dep,'Designation':des,'Salary':sal},f)

print('''
==========================================MENU=========================================
1.Diplay details of Managers earning more than 50000 in Finance and in Admin Department
2.Delete the employee details who have reached retirement age(58 years)
3.Exit''')

while True:
    c=int(input("Enter choice :"))
    if 1< c >3:
        print("Invalid Menu Code")
    elif c==1:
        with open('EMPLOYEE.DAT','rb') as f:
            try:
                while True:
                    l=pickle.load(f)
                    if (l['Department']=='Finance' or l['Department']=='Admin') and int(l['Salary'])>50000 and l['Designation']=='Manager':
                        for i in l:
                            print(i,l[i],sep=' : ')
                        print()
            except:pass
    elif c==2:
        l1=[]
        with open('EMPLOYEE.DAT','rb') as f:
            try:
                while True:
                    l=pickle.load(f)
                    l1.append(l)
            except:pass
        for i in l1:
            if int(i['Age'])>=58:
                l1.remove(i)
                for j in i:
                    print(j,i[j],sep=' - ')
                print()
    elif c==3:
        print("The Program is Ended")
        break
