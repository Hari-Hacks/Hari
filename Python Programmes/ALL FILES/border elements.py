l=eval(input('enter the nested list:'))
s=0
for i in range(len(l)):
    if i==l[0] or i==l[-1]:
        s+=i
        for j in range(len(l)):
            s+=l[i][j]
            print(l[i][j],l[0],l[-1],sep='  ')
print(s)
