import pickle
n=int(input("Enter number of students : "))
with open('STUDENT.DAT','wb') as f:
    for i in range(n):
        r=input("Enter roll no. :")
        m=input("Enter name :")
        s=input("Enter Stream :")
        e=int(input("Enter total :"))
        pickle.dump([r,m,s,e],f)

print('''
========================================MENU===========================================
1.Display Steam wise topper detail
2.Increment total by 3 marks for biology students and decrement 2 for EG stream students
3.Exit''')
while True:
    c=int(input("Enter Menu Code:"))
    if 1< c >3:
        print("Invalid Menu Code")
    elif c==1:
        l1=[]
        with open('STUDENT.DAT','rb') as f:
            try:
                while True:
                    l=pickle.load(f)
                    l1.append(l)
            except:
                pass
        d={}
        for i in l1:
            d[i[2]]={}
        for i in l1:
            d[i[2]][i[0]]=[i[1],i[3]]
        for i in d:
            m=0
            for j in d[i]:
                if d[i][j][1]>m:
                    m=d[i][j][1]
            print(i,':')
            for j in d[i]:
                if d[i][j][1]==m:
                    print(j,d[i][j][0],d[i][j][1],sep=' : ')
    elif c==2:
        l1=[]
        with open('STUDENT.DAT','rb') as f:
            try:
                while True:
                    l=pickle.load(f)
                    l1.append(l)
            except:
                pass
        for i in range(len(l1)):
                        if l1[i][2].lower()=='biology':
                           l1[i][3]+=3
                        elif l1[i][2].lower()=='eg':                        
                            l1[i][3]-=2
        with open('STUDENT.DAT','wb') as f:
            for i in l1:
                pickle.dump(i,f)
                print(i)
    elif c==3:
        print("The Program is Ended")
        break