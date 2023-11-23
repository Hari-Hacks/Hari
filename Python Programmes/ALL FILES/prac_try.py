'''
AIM : To create a Binary file STUDENT.DAT/.BIN/.TXT with each record having details of
rollnumber ,name, stream, total and perform the operations using a menu driven code.
METHODOLOGY: The binary file is created to store details of 'N' students, with input read in
the form of a list. The menu is displayed and the related operations are performed on the
binary file depending on user's choice.
Note: The menu options to be as follows:
MENU
1. Display Stream wise topper detail
2. Increment the total by 3 marks for students in the biology stream and decrement by 2for
students in EG stream.
3. Exit'''
import pickle 
d={}
with open('student.dat','wb') as f:
    n= int(input('Enter the no. of records:'))
    for i in range(n):
        r=int(input('Roll no.:'))
        n=input('Name:')
        s=input('stream:')
        tot=int(input('Total:'))                                               #{cs:{123:{n:hs,tot:540},124:{n:rs,tot:545}},eg:{...}}
    pickle.dump(d,f)
print('''
MENU
1. Display Stream wise topper detail
2. Increment the total by 3 marks for students in the biology stream and decrement by 2for
students in EG stream.
3. Exit''')
while True:
    q=int(input('Enter the menu code: '))
    if 1< q >3:
        print('invalid menu code')
    elif q==1:
        with open('student.dat','rb') as f:
            try:
                while True:
                    d=pickle.load(f)
            except EOFError or FileNotFoundError :
                pass
            for i in d:
                m=0
                for j in d[i]:
                    if d[i][j]['total'] > m:
                        m=d[i][j]['total']
                        a=j
                if d[i][a]['total'] == m: 
                    print('Name:',d[i][a]['name'],'\nRoll no.:',a,'\nStream:',i,'\nTotal:',m)
                print()
    elif q==2:
        with open('student.dat','rb') as f:
            try:
                while True:
                    d=pickle.load(f)
            except:
                pass
        with open('student.dat','wb') as f:
            for i in d:
                if i.lower() == 'biology':
                    for j in d[i]:
                        d[i][j]['total'] += 3 
                if i.lower() == 'eg':
                    for j in d[i]:
                        d[i][j]['total'] -= 2
            pickle.dump(d,f)
        with open('student.dat','rb') as f:
            try:
                while True:
                    d=pickle.load(f)
                    print(d)
            except:
                pass
    elif q==3:
        print('The program is ended')
        break

                    
