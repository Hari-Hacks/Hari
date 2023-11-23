k=8
for i in range(1,6):
    for j in range(1,i+1):
        print('*',end='') #for having numbers take out * and give j
    print(k*" ",end='')
    k-=2
    for m in range(i,0,-1):
        print('*',end='') #for having numbers take out * and give m
    print()
k=2
for i in range(4,0,-1):
    for j in range(1,i+1):
        print('*',end='') #for having numbers take out * and give j
    print(k*" ",end='')
    k+=2
    for m in range(i,0,-1):
        print('*',end='') #for having numbers take out * and give m
    print()