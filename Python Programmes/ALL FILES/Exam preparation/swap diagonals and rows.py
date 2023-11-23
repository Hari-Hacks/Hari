l=eval(input('enter the elements:'))
for i in range(5):
    for j in range(5):
        print(l[i][j],end=' ')
    print()
for i in range(5):
    for j in range(5):
        if i==j:
            l[i][j],l[i][4-j]=l[i][4-j],l[i][j]
print('*'*50)
for i in range(5):
    for j in range(5):
        print(l[i][j],end=' ')
    print()
print('*'*50)
l[0],l[4]=l[4],l[0]
for i in range(5):
    for j in range(5):
        print(l[i][j],end=' ')
    print()