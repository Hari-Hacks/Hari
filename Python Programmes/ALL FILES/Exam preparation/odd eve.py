l=[30,16,17,2,13,19,4]
l1,l2=[],[]
for i in l:
    if i%2==0:
        l1+=[i]
        print(l1)
    elif i%2==1:
        l2+=[i]
print(l1+l2)