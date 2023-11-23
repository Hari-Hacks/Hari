n=5
sp=4
for i in range(5,0,-1):
    print(' '*sp,end=' ')
    sp-=1
    for j in range(n-i,n):
        print(j,end=' ')
    print()
