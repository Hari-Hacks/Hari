while True:
    flag=0
    l=eval(input('Enter the array of strings:'))
    n=len(l)
    small_str=''
    for i in range(len(l)-1):
        if len(l[i])<len(l[i+1]):
            small_str=l[i]
        else:
            small_str=l[i+1]
    ##print(small_str)
    ##print('*'*50)
    m=len(small_str)
    l1=[]
    for i in range(len(l)):
        l1.append(l[i][:m])
    #print(l1)
    #print('+'*50)
    l2=[]
    for i in range(len(l)-1):
        same_str=''
        for j in range(m):
            if l[i][j]==l[i+1][j]:
                same_str+=l[i][j]
                flag=1
        l2.append(same_str)
    if len(l2)==1:
        print(l2[0])
        break
    #print(l2)
    #print('.'*50)
    small_str1=''
    for i in range(len(l2)-1):
        if len(l2[i])<len(l2[i+1]):
            small_str1=l2[i]
        else:
            small_str1=l2[i+1]
    #print(small_str1)
    #print('!'*50)
    m=len(small_str1)
    l3=[]
    for i in range(len(l2)):
        l3.append(l[i][:m])
    #print(l3)
    #print('@'*50)
    same_str2=''
    l4=[]
    for i in range(len(l3)-1):
        for j in range(m):
            if l3[i][j]==l3[i+1][j]:
                same_str2+=l3[i][j]
        l4.append(same_str2)
    #print(l4)
    #print('#'*50)
    max=''
    for i in range(len(l4)):
        if l4[i]>max:
            max+=l4[i]
    #print(max)
    #print('$'*50)
    if max=='':
        print('')
    else:
        print(max)
    s=input('y/n:')
    if s=='n':
        break