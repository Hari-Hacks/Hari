n=int(input('enter any number between 10 and 50:'))
Sum=0
count=0
for i in range(10,n+1):
    for k in range(2,i):
        if i%k==0:
            break
    else:
        print(i,end=' ')
        count+=1
        Sum+=i
print('\n',Sum/count,'is the average of prime numbers')
