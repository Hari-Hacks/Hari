n=int(input('Enter the no. of rows:'))
for i in range(n):
    if i%2==0:
        for j in range(1,i*2+2,2):
            print(j,end=' ')
        print()
    if i%2==1:
        for j in range(i*2+1,0,-2):
            print(j,end=' ')
        print()