l=eval(input('enter the elements:'))
n=int(input('enter the no. of rows:'))
m=int(input('enter the no. of coloumns:'))
for i in range(n):
    for j in range(m):
        print(l[i][j],end=' ')
    print()
a=len(l)
print('*'*50)
for i in range(n):
    for j in range(m):
        if i==0 or j==0 or j==a-1 or i==a-1:
            print(l[i][j],end=' ')
        else:
            print(' ',end=' ')
    print()
print('*'*50)
count=0
for i in range(n):
    for j in range(m):
        if i==0 or j==0 or j==a-1 or i==a-1:
            if l[i][j]%2==1:
                
                print(l[i][j],end=' ')
                count+=1
            else:
                print('@',end=' ')
        else:
            print(' ',end=' ')
    print()
print('*'*50)
print(count)
print('*'*50)