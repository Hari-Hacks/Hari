def hs_hash_code():
    l=len(s)
    if l > 6:
        n=l%5
        h1=s[0:n]
        h2=s[n:n*2]
        h3=s[n*2:n*3]
        h4=s[n*3:n*4]
        h5=s[n*4::]
        l1=[h1,h2,h3,h4,h5]
        def char_compression(l):
            global a,c
            a=c=''
            for i in l:
                for j in i:
                    a+=format(ord(j),'08b')
                    c+=format(ord(j),'08b')
        char_compression(l1)
        b=''
        flag=0
        for i in range(len(a)):
            if c[i] != c[i+1]:
                b+=c[i]
            elif c[i] == c[i+1]:
                b+=c[i]
                flag=1
                if a[i+1] == a[i+2]:
                    flag=2
                    if a[i+2] == a[i+3]:
                        flag=3
                if flag == 1:
                    b+='2'
                if flag == 2:
                    b+='3'
                if flag == 3:
                    b+='4'
                
