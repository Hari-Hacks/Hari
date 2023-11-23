from random import randint as ran
key=[]
tey=[]
for j in range(126):
    tey.append(chr(j))
for j in range(32,126):
        tey.append(chr(j))
def shulist(t,key):
    for i in range(t):
        x=key[:len(key)-1]
        y=key[len(key)-1:]
        y.extend(x)
        key=list(y)
    return key
def se():
    try:
        print("Message to be encrypted:")
        i=input()
        l=list(i)
        n=ran(1,3)
        b=ran(1,3)
        randmid=''
        for i in range(b):
            randmid+=chr(ran(32,125))
        b=hex(b)
        n=hex(n)
        a=int(n,base=16)
        randstr=''
        for i in range(a):
            randstr+=chr(ran(32,125))
        n='02'+n[2::1]
        randstr+=n+b
        b=int(b,base=16)
        key=[]
        ttt=''
        for i in range(32,126):
            key.append(chr(i))
        for i in range(len(l)):
            key=shulist(i*12+a+1,key)       
            ttt+=key[ord(l[i])-33]
        if len(ttt)>b:
            ttt=ttt[:b]+randmid+ttt[b:]
        elif len(ttt)<=b:
            ttt=randmid+ttt
        ttt+=randstr
        print("Encrypted Message :")
        print(ttt)
    except:
        print("Invalid Characters entered")
    
se()
def sd():
    try:
        print("Message to be decrypted :")
        i=input()
        k=i[::-1]
        n=k.find('20')
        n=len(i)-n-2
        no=i[n:]
        i=i[:n]
        b=no.find('0x')
        n=no[:b]
        n='0x'+n[2:b]
        n=int(n,base=16)
        i=i[:len(i)-n]
        b=no[b:]
        b=int(b,base=16)
        if len(i)<=2*b:
            i=i[b:]
        else:
            i=i[:b]+i[2*b:]
        key=[]
        for j in range(32,126):
            key.append(chr(j))
        ttd=''
        for j in range(len(i)):
            key=shulist(j*12+n+1,key)
            ttd+=tey[key.index(i[j])+33]
        print("Decrypted Message :")
        print(ttd)
    except :print("*** Non-decryptable Message ***")
sd()
