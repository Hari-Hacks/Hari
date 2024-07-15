def write():
    with open ('writing.txt','w') as f :
        a='yes'
        while a=='yes':
            x=input('enter the sentence')
            f.write(x)
            a=input('do you wnat to enter more sentences')
write()
def num_line():
    with open ('writing.txt','r') as f :
           l=f.readlines()
           print('the no. of lines present in the file is ',len(l))
def copy():
    with open ('writing.txt','r') as f :
        with open ('newfile.txt','w') as f1 :
            l=f.read()
            l1=l.split()
            c1=0
            for i in l1:
                if i.lower()=='u':
                    c1+=1
                    f1.write(i)
    with open ('newfile.txt','w') as f4 :
        x3=f4.readlines()
        if c1:
            for i in x3:
                print('thw words containing u',i)
        else:
            print('no words present ')
def swapcase():
    with open ('writing.txt','r') as f5 :
        l3=[]
        x5=f5.read()
        l3.append(x5.swapcase())
    with open ('writing.txt','w') as f6 :
        for i in l3:
            f6.write(i)
    with open ('writing.txt','r') as f7 :
        x7=f7.readlines()
        for i in x7:
            print(i)
while True:
    ch=int(input('Enter option:'))
    if ch==1:
        with open('data.txt','r') as f:
            print('Number of lines',len(f.readlines()))
    elif ch==2:
        with open('data.txt','r') as f,open('new.txt','w') as f1:
            s=f.readline()
            while s:
                for k in s.split():
                    if 'U' in k:
                        f1.write(k+'\n')
                s=f.readline()
        with open('new.txt','r') as f1:
            print('Words containing U')
            for i in f1.readlines():
                print(i,end='')
    elif ch==3:
        with open('data.txt','r') as f:
            s=f.readline()
            while s:
                print(s.swapcase(),end='')
                s=f.readline()
    elif ch==4:
        print("Exited")
        break
    else:
        print('Invalid option')
