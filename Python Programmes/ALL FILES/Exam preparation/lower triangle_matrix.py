l=eval(input('enter the elements:'))
n=int(input('enter the no. of rows:'))
m=int(input('enter the no. of coloumns:'))
for i in range(n):
    for j in range(m):
        print(l[i][j],end=' ')
    print()
print('*'*50)
for i in range(n):
    for j in range(0,i+1):
        print(l[i][j],end=' ')
    print()
print('*'*50)
sp=0
for i in range(n):
    print(' '*sp,end='')
    sp+=2
    for j in range(i,n):
        print(l[i][j],end=' ')
    print()
print('*'*50)
