sum=0
for k in range(1,5):
    Fac=1
    for j in range(1,k+1):
        Fac*=j
    if k%2==0:
        Fac*=-1
    sum+=Fac
print(sum)