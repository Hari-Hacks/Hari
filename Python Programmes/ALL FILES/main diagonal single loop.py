l=eval(input('enter the list:'))
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