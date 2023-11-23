import pickle
with open('student.dat','wb') as f:
    n=int(input('enter the no. of records:'))
    for i in range(n):
        n=input('name:')
        a=int(input('age:'))
        de=input('department:')
        desig=input('desig:')
        s=int(input('salary:'))
        pickle.dump([n,a,de,desig,s],f)
print()
print()
with open('student.dat','rb') as f:
    try:
        while True:
            l=pickle.load(f)
            if (l[2].lower() == 'admin' and l[3].lower() == 'manager' and l[4] > 50000) or (l[2].lower() == 'finance' and l[3].lower() == 'manager' and l[4] > 50000):
                print('name:',l[0],'\nage:',l[1],'\ndepartment:',l[2],'\ndesignation:',l[3],'\nsalary:',l[4])
                print()
    except EOFError or FileNotFoundError:
        print('@'*50)
        pass
print('*'*50)

l=[]
with open('student.dat','rb') as f:
    try:
        while True:
            l1=pickle.load(f)
            l.append(l1)
    except:
        pass
print('='*50)
with open('student.dat','wb') as f:
    for i in l:
        if i[1] >= 58:
            print('name:',i[0],'\nage:',i[1],'\ndepartment:',i[2],'\ndesignation:',i[3],'\nsalary:',i[4])
            l.remove(i)
            print('+'*50)
        print('/'*50)
    for i in l:
        pickle.dump(i,f)
        print('successfully dumped')


                