x=int(input("Enter ll"))
y=int(input("Enter ul"))
for i in range(x,y+1):
   if i<=1:
      continue
   for j in range(2,i):
         if i%j==0:
             break
   else:
      print(i,end='  ')
