'''1@1
32@3
'''
n=1
m=67
for i in range(m):
    for j in range(n,i,-1):
        print(j,end=' ')
    print('@',end=' ')
    print(n,end=' ')
    n+=2
    print()