print('-/'*50)
'''
    * 
   ***
  *****
 *******
*********'''
n=5
for i in range(1,6):
    for j in range(i+1,6):
        print(' ',end='')
    for k in range(0,i):
        print('*',end='')
    for j in range(1,i):
        print('*',end='')
    print()
print('-/'*50)
'''
*********
 *******
  *****
   ***
    *
'''
n=5
sp=6
for i in range(6):
    for j in range(6,sp-i,-1):
        print(' ',end='')
    for k in range(n-i,-1,-1):
        print('*',end='')
    for j in range(6,i+1,-1):
        print('*',end='')
    print()