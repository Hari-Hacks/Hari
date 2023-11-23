def pattern(n):
    c=1
    for i in range(65,69+n,2):
        for j in range(i,64,-2):
            if i in range(65,69+n,4):
                print(chr(j),end='#')
            if i in range(67,69+n,4):
                print(chr(j),end='*')
        print(c)
        c+=2
    print()
num=int(input('Enter no.:'))
pattern(num)