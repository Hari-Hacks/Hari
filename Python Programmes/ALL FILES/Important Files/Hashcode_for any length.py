def char_compression(l1):
    cnt = 1
    l=[]
    for i in range(len(l1)):
            res = ""
            for j in range(1,len(l1[i])):
                    if l1[i][j - 1] == l1[i][j]:
                        cnt += 1
                    else:
                        res = res + l1[i][j - 1]
                        if cnt > 1:
                            res += str(cnt)
                            cnt = 1
            if len(l1[i])==0:
                #This check if l1[i] is empty
                #else error will come because we can't
                #access l1[i][-1]
                res=res+'0'
            elif len(l1[i])>0:
                res = res + l1[i][-1]
            if cnt > 1:
                res += str(cnt)
            l.append(res)
    return l

lst=[chr(i) for i in range(33,126)]
lst+=[chr(i) for i in range(33,126)]
lst+=[chr(i) for i in range(33,47)]

def hs_hashcode(s):
    l=len(s)
    if 1 < l > 500:
        n=l//5
        h1=s[0:n]
        h2=s[n:n*2]
        h3=s[n*2:n*3]
        h4=s[n*3:n*4]
        h5=s[n*4::]
        l=[h1,h2,h3,h4,h5]
        for i in l:
            a=''
            for j in i:
                a+=format(ord(j),'08b')
                l.pop(0)
                l.append(a)
        fi_s=char_compression(l)
        main=''
        for i in range(len(fi_s)):       
            while len(fi_s[i]) < 500:
                c=0
                b=int(fi_s[i])
                c=b**2
                fi_s[i]+=str(c)
            main+=fi_s[i][:-501:-1]

    if l > 500:
        a=s[:500]
        r=s[500::]
        h1=a[0:100]
        h2=a[100:200]
        h3=a[200:300]
        h4=a[300:400]
        h5=a[400:500]
        l=[h1,h2,h3,h4,h5]
        for i in l:
            c=''
            for j in i:
                c+=format(ord(j),'08b')
            l.append(c)
            l.pop(0)
        b=char_compression(l)
        if len(r) % 500 !=0:
           rnge=(len(r)//500)+1
        elif len(r) % 500 == 0:
            rnge=len(r)//500
        l1=[]
        for i in range(rnge):
            l1.append(r[i*500:(i+1)*500])
        for i in l1:
            r1=r[0:100]
            r2=r[100:200]
            r3=r[200:300]
            r4=r[300:400]
            r5=r[400:500]
            l2=[r1,r2,r3,r4,r5]
            char_compression(l2)
            h1=str(int(l[0])+int(l2[0]))
            h2=str(int(l[1])+int(l2[1]))
            h3=str(int(l[2])+int(l2[2]))
            h4=str(int(l[3])+int(l2[3]))
            h5=str(int(l[4])+int(l2[4]))
        l=[h1,h2,h3,h4,h5]
        rage=range(20,201)
        for i in range(len(l)):
            srt=''
            h=''
            for j in l[i]:
                srt+=j
                if int(srt) in rage:
                    h+=str(lst[int(srt)])
                    srt=''
            l[i]=h
        main=''
        for i in l:
            main+=i
    return main