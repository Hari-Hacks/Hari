'''     1 
      1 2 1 
    1 2 3 2 1
  1 2 3 4 3 2 1
1 2 3 4 5 4 3 2 1'''
for i in range(1,6):
    for j in range(i+1,6):
        print(' ',end=' ')
    for k in range(1,i+1):
        print(k,end=' ')
    for j in range(i-1,0,-1):
        print(j,end=' ')
    print()
print('*'*50)
'''
1 2 3 4 5 4 3 2 1
  1 2 3 4 3 2 1
    1 2 3 2 1
      1 2 1
        1'''
for i in range(5,0,-1):
    for j in range(i+1,6):
        print(' ',end=' ')
    for k in range(1,i+1):
        print(k,end=' ')
    for j in range(i-1,0,-1):
        print(j,end=' ')
    print()