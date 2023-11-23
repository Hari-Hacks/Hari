q=int(input())
if q==1:
    st=input('enter the string:')
    b=st[::-1]
    if b==st:
        print('s')
    else:print('no')
elif q==2:
    st=input('enter the string:')
    b=''
    print(st)
    for i in range(-1,-len(st)-1,-1):
        b+=st[i]
    print(b)
    if b==st:
        print('yes')
    else:print('no')
