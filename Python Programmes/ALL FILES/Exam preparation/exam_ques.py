while True:
    q=int(input('1  or 2 or 3:'))
    if q==3:
        break
    else:
        if q==1:
            ll=110
            ul=990
            b=''
            for i in range(ll,ul+1):
                s=str(i)
                for j in range(-1,-len(s)-1,-1):
                    b+=s[j]
                if b==s:
                    if b%2==1:
                        print('prime palindrome')


    