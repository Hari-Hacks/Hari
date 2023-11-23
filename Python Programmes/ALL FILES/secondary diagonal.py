l=eval(input('enter the nested list:'))
for i in range(len(l)):
    for j in range(len(l)-1,-1,-1):
        if i+j==len(l)-1:
            print(l[i][j])
        else:print(' ',end='')
    print()
