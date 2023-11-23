n=5
for j in range(1,n+1):
    ch='A'
    for k in range(1,j+1):
        print(ch,end=' ')
        ch=chr(ord(ch)+2)
    print('@',j,end=' ')
    print()