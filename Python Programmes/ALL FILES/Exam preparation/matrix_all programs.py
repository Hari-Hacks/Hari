l=eval(input('enter the elements:'))
n=int(input('enter the no. of rows:'))
m=int(input('enter the no. of coloumns:'))
for i in range(n):
    for j in range(m):
        print(l[i][j],end=' ')
    print()
print('*'*50)
print('lower triangle')
for i in range(n):
    for j in range(0,i+1):
        print(l[i][j],end=' ')
    print()
print('*'*50)
print('upper triangle')
sp=0
for i in range(n):
    print(' '*sp,end='')
    sp+=2
    for j in range(i,n):
        print(l[i][j],end=' ')
    print()
print('*'*50)
print('border elements')
a=len(l)
for i in range(n):
    for j in range(m):
        if i==0 or j==0 or j==a-1 or i==a-1:
            print(l[i][j],end=' ')
        else:
            print(' ',end=' ')
    print()
print('*'*50)
print('main diagonal single loop:')
for i in range(len(l)):
    print(l[i][i],end=' ')
print()
print('*'*50)
print('main diagonal nested loop:')
for i in range(len(l)):
    for j in range(len(l)):
        if i==j:
            print(l[i][j],end=' ')
        else:print(' ',end=' ')
    print()
print('*'*50)
print('secondary diagonal single loop:')
for i in range(len(l)):
    print(l[i][len(l)-i-1],end=' ')
print()
print('*'*50)
print('secondary diagonal nested loop:')
for i in range(len(l)):
    for j in range(len(l)):
        if i+j==len(l)-1:
            print(l[i][j])
        else:print(' ',end=' ')
    print()
print('*'*50)
print('sum of diagonals')
s=0
for i in range(len(l)):
    for j in range(len(l)):
        if i==j or i+j==len(l)-1:
            s+=l[i][j]
print(s)
print('*'*50)
print('sum of border elements')
a=len(l)
s=0
for i in range(n):
    for j in range(m):
        if i==0 or j==0 or j==a-1 or i==a-1:
            s+=l[i][j]
print(s)
print('*'*50)

