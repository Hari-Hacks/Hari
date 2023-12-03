#File contains all functions for encryption
# NOTE- All necessary imports are done in the respective partitions

#Functions to convert int to base 37 and vice versa
#Functions start

d={0: ';', 1: '{', 2: 'V', 3: 'C', 4: 'n', 5: ':', 6: 'a', 7: 'G', 8: 'O', 9: '!', 10: '$',
   11: '5', 12: ')', 13: 'N', 14: 'R', 15: '#', 16: '/', 17: '9', 18: 'F', 19: '@', 20: '2',
   21: 's', 22: 'S', 23: '|', 24: 'g', 25: 'x', 26: '}', 27: "'", 28: '(', 29: '7',30: '<',
   31: 'v', 32: 'Z', 33: '3', 34: '^', 35: 'b', 36: 'j'}
l=[]

def inttosys(n):
    #function converts decimal to base 37
    #Function takes input an integer and return a string contains number in base 37

    l=[]
    while  n >= 37:
        i=n%37
        l.append(i)
        n=n//37
    else:
        l.append(n)
    aa=''
    for i in l[::-1]:
        aa+=d[i]
    return aa

def systoint(n):
    #Function converts base 37 to decimal
    #Function takes input a string of base 37 and returns integer

    l=list(str(n))
    t=[]
    for i in l:
        for k in d:
            if d[k]==i:
                t.append(k)
    no=0
    t=t[::-1]
    for j in range(len(t)):
        no+=t[j]*(37**j)
    return no

#Functions end

#functions to related to hashing. (also contains authentication functions)
#functions start

lst=[chr(i) for i in range(33,126)]
lst+=[chr(i) for i in range(33,126)]
lst+=[chr(i) for i in range(33,47)]

#list 'lst' is created for use in the function char_ascii


def char_compression(l1):
    #This functions takes input a list and returns a list
    #This function converts a string into a string which has reduced the repeating characters
    #if l='aaaabbb'
    #then the function returns l='a4b3'

    cnt = 1
    #cnt counts number of repeatitions taking place
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
            cnt=1
            l.append(res)
    return l

def char_ascii(a):
    #This function takes input a string and returns a string
    #functions converts every single character in the string into its ascii value
    #and add the ascii values as string to a new string
    #NOTE-Function adds ASCII value as string not INT

    o=''
    for i in a:
        o+=str(ord(i))
    o=str(int(o)**2)
    rage=range(20,201)
    srt=''
    h=''
    for i in o:
        srt+=i
        if int(srt) in rage:
            h+=str(lst[int(srt)])
            srt=''
    return h
    
def hs_hashcode(s):
    #Function takes input a string and converts into its hash value and return a string

    l=len(s)
    if l==0:
        #If file size equals 0

        main='0'*500

    elif l<=4:
        #IF fiel size is less than 4

        h1=s[0:1]
        h2=s[1:2]
        h3=s[2:3]
        h4=s[3:4]
        h5=s[4::]
        #the string is divided into five and stored in 5 variables
        l=[h1,h2,h3,h4,h5]
        bin_list=l.copy()
        for i in bin_list:
            k=''
            for j in i:
                k+=format(ord(j),'08b')
                #This converts every character in the string into its binary value
            l.pop(0)
            l.append(k)
            #above two functions converts all values in 'l' to binary
        fi_s=char_compression(l)
        main=''
        for i in range(len(fi_s)):       
            while len(fi_s[i]) < 500 and fi_s[i]!='0':
                c=0
                b=int(fi_s[i])
                c=b**2
                fi_s[i]=str(c)
            main+=fi_s[i][:-501:-1]
            #only the last 500 characters is taken and that too in reverse order
        #Main is the hash value

    elif 4 < l <=500:
        #File size between 4 and 500

        n=l//5
        h1=s[0:n]
        h2=s[n:n*2]
        h3=s[n*2:n*3]
        h4=s[n*3:n*4]
        h5=s[n*4::]
        #the string is divided into five and stored in 5 variables
        l=[h1,h2,h3,h4,h5]
        bin_list=l.copy()
        for i in bin_list:
            k=''
            for j in i:
                k+=format(ord(j),'08b')
                #This converts every character in the string into its binary value
            l.pop(0)
            l.append(k)
            #above two functions converts all values in 'l' to binary
        l=char_compression(l)
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
        main=char_ascii(main)
        while len(main)<500:
            #THis is done to extend the main to 500 characters
            main=char_ascii(main)
            
            #only the last 500 characters is taken and that too in reverse order
        #Main is the hash value

    elif l > 500:
        #if file size is above 500 characters

        a=s[:500]
        r=s[500::]
        h1=a[0:100]
        h2=a[100:200]
        h3=a[200:300]
        h4=a[300:400]
        h5=a[400:500]
        l=[h1,h2,h3,h4,h5]
        chrlist=l.copy()
        for i in chrlist:
            c=''
            for j in i:
                c+=format(ord(j),'08b')
            l.append(c)
            l.pop(0)
        l=char_compression(l)
        c=''
        for i in r:
            c+=format(ord(j),'08b')
        r=c
        if len(r) % 500 !=0:
           rnge=(len(r)//500)+1
        elif len(r) % 500 == 0:
            rnge=len(r)//500
        l1=[]
        for i in range(rnge):
            l1.append(r[i*500:(i+1)*500])
        for i in l1:
            #from the file 500 characters are taken at a time and stored in 5 variables and manipulated
            #This process is repeated until the file becomes empty
            #NOTE- here, file is used synonymous with the input value
            r1=i[0:100]
            r2=i[100:200]
            r3=i[200:300]
            r4=i[300:400]
            r5=i[400:500]
            l2=[r1,r2,r3,r4,r5]
            l2=char_compression(l2)
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
        main=char_ascii(main)
        while len(main)<500:
            #THis is done to extend the main to 500 characters
            main=char_ascii(main)
    main=main[:-501:-1] 
    #Main is the hash value            
    return main

def HS_authenticateme(a,skey=''):
    #Functions authenticates the encrypted message
    #Function takes input a string (Encrypted message)
    #Return True if correct message
    #Returns False otherwise

    hss=a[-500:]
    #hss refers to the hash value
    sk=a[:500]
    if sk!=hs_hashcode(skey):
        return False
    a=a[500:-500:1]
    l=hs_hashcode(a)
    if l==hss:
        return True
    else:
        return False
#Functions End

#functions related to encryption 
#functions Start

from random import randint as ran
#library to convert raw string to normal string
import codecs

#in37 means integer to base 37
#i37in means base 37 to integer

key=[]
tey=[]

#KEY
#KEY=
#To generate table for encryption and decryption

#tey is used because of error which is occuring while trying to decrypt
#message because there is out of index error if the tey have only (32,126) characters
#so now by doing this the chr() of symbol is same as the index position in tey
for j in range(126):
    tey.append(chr(j))
for j in range(32,126):
    tey.append(chr(j))
    
def shulist(t,key):
    #Function shifts elements of table by specified amount

    for i in range(t):
        x=key[:len(key)-1]
        y=key[len(key)-1:]
        y.extend(x)
        key=list(y)
    return key

def se(inpt,skey=''):
    #This is actual function which encrypts message
    #this function is used because encr cannot be used for large messages
    #Hence this function splits the message and passes into encr
    #inpt is split into parts of 100 each
    try:
        a=int((len(inpt)-1)//100)+1
        #-1 is used because if the len is 100, a list with one string is needed, but instead two strings come where the last string is empty
        l=[]
        for i in range(a):
            l.append(inpt[i*100:(i+1)*100])
        ttt=''
        for i in l:
            ttt=ttt+encr(i,skey)+'~'
        #add hash below
        hash_value=hs_hashcode(ttt)
        #hash is added to ttt in the end
        ttt=ttt+hash_value
        #Secretkey hash is added
        secretkeyhash=hs_hashcode(skey)
        ttt=secretkeyhash+ttt
        #ttt is the main final encrypted message
        return ttt    
    except:
        return False
def sd(inpt,skey=''):
    #this is actual function which decrypts message
    #function seperates the string in list by splitting at '~'
    try:
        #secretkeyhash is checked
        secrekeyhash=inpt[:500]
        #secrethash is hash of skey entered as input
        secrethash=hs_hashcode(skey)
        if secrethash==secrekeyhash:
            pass
        else:
            return False
        #secretkey hash is removedx
        inpt=inpt[500:]
        #hash is removed
        hash_value=inpt[-500::]
        inpt=inpt[:-500]
        if hash_value==hs_hashcode(inpt):
            pass
        else:
            return False
        l=inpt.split('~')
        #l contains the message to be decrypted
        #here in the end an empty string will be present
        #this is because there will be '~' before the hash starts.
        #pop is used to remove it
        l.pop()
        ttd=''
        for i in l:
            ttd=ttd+decr(i,skey)
        #decode is used to convert '\n' characters which was initially 2 characters
        #into 1 character
        ttd=codecs.decode(ttd, 'unicode_escape')
        #here ttd is the final decrypted message
        return ttd
    except :return False
    

def encr(i,skey=''):
    #Function encrypts message
    #If 'inpt' contains invalid characters, function return False


        #repr is used as input may also have '\n' but the character list doesn't
        #incluse '\n'
        #repr convert '\n' as two diff characters
        
        i=repr(i)
        l=list(i)
        #between Random number generated
        b=ran(4,36)        
        randmid=''
        for i in range(b):
            randmid+=chr(ran(32,125))
        b=inttosys(b)
        #Terminal Random number Generator
        n=ran(4,36)
        n=inttosys(n)
        a=systoint(n)
        randstr=''
        for i in range(a):
            randstr+=chr(ran(32,125))
        randstr+=n+b
        b=systoint(b)
        key=[]
        ttt=''
        
        #secretkey value is found
        secretkey=1
        secretkeyhash=hs_hashcode(skey)
        for i in skey:
            secretkey+=ord(i)+ord(secretkeyhash[-1])
        

        
        for i in range(32,126):
            key.append(chr(i))
        for i in range(len(l)):
            key=shulist(i*12+a+1+secretkey,key)       
            ttt+=key[ord(l[i])-33]
        if len(ttt)>b:
            ttt=ttt[:b]+randmid+ttt[b:]
        elif len(ttt)<=b:
            ttt=randmid+ttt
        ttt+=randstr
        #Matrix Manipulation
        l=Matrix_Maker(ttt)
        l=Matrix_Jumbler(l)
        l=Matrixflip(l)
        ttt=Matrixtostr(l)
        #ttt is encrypted message
        return ttt    

def decr(i,skey=''):
    #Function decrypts message
    #If message is non decryptable, function returns False
    
        #now inpt is encrypted message
        #message unjumbler
        l=Matrix_Makerde(i)
        l=Matrixflip(l)
        l=Matrix_Jumbler(l)
        #Function for removing all |
        i=Matrixtostrde(l)

        n=i[-2]
        b=i[-1]
        i=i[:-2:1]
        n=systoint(n)
        i=i[:len(i)-n]
        b=systoint(b)
        if len(i)<=2*b:
            i=i[b:]
        else:
            i=i[:b]+i[2*b:]
        key=[]
        for j in range(32,126):
            key.append(chr(j))

         #secretkey value is found
        secretkey=1
        secretkeyhash=hs_hashcode(skey)
        for patt in skey:
            secretkey+=ord(patt)+ord(secretkeyhash[-1])

        
        ttd=''
        for j in range(len(i)):
            key=shulist(j*12+n+1+secretkey,key)
            ttd+=tey[key.index(i[j])+33]
        
        #ttd is the decrypted message
        ttd=ttd[1:-1:1]
        return ttd
    
def intc(n):
    #Function to check if the number is present as integer or float

    if int(n)==n:
        return True
    else:
        return False
    
def Matrix_Maker(a):
    #To convert the string into a matrix

    k=len(a)
    p=1
    m=[]
    for i in range(k):
        if intc(i**(0.5)):
            p=i**0.5
    p=int(p+1)
    del k
    k=int(p**2-len(a))
    s=chr(448)*k
    a=a+s
    i=1
    n=[]
    d=[]
    for i in a:
        d.append(i)
    for j in range(int(p)):
        l=d[j*p:j*p+p]
        m.append(l)
    del l
    s=chr(448)*p
    s=list(s)
    n=m.count(s)
    for i in range(n):
        m.remove(s)
    return m

def Matrix_Makerde(i):
    #To convert the string into a matrix
    #But for decryption
    #Problem is sometimes decrypted letters are not
    #Square number. therefore previous function
    #Can't be used

    a=len(i)
    while True:
        if intc(a**0.5):
            break
        else:
            a+=1
    p=a**0.5
    b=int(len(i)/p)
    m=[]
    for j in range(int(p)):
        l=list(i[j*b:j*b+b])
        m.append(l)
    return m     
            

def Matrix_Jumbler(l):
    #Function finds the transpose of the matrix

    a=len(l)
    b=len(l[0])
    m=[]
    n=[]
    for i in range(b):
        for j in range(a):
            n.append(l[j][i])
        m.append(n)
        n=[]
    l=m
    del m
    return l

def Matrixtostr(l):
    #Function converts the matrix into a string in order in which the
    #elements are present in the nested list

    s=''

    for i in range(len(l)):
        for j in range(len(l[0])):
            s+=str(l[i][j])
    return s

def Matrixtostrde(l):
    #Function converts the matrix into a string in order in which the
    #elements are present in the nested list but removes |

    s=''
    for i in range(len(l)):
        for j in range(len(l[0])):
            s+=str(l[i][j])
    a=s.count(chr(448))
    s=s[:len(s)-a]
    return s

def Matrixflip(l):
    #Function flips the matrix sideways
    for i in range(len(l)):
        l[i]=l[i][::-1]
    return l

#Functions End

#Functions related to encryption and decryption of files and functions related to password
#Functions Start

from random import randint as ran
'''def chrreplaceencr(s):
    #Function follows all rules as next function
    #It is used for encryption
    '\\','[',']','(',')','{','}','"',"'",'<','>'
    l=''
    s=list(s)
    for i in range(len(s)):
        k=s[i]
        if k=='\\':
            s[i]='£'
        elif k=='[':
        elif k==']':
        elif k=='(':
        elif k==')':
        elif k=='{':'''
def chrreplace(s):
    #Function replaces all quotes, slashes and brackets
    #Error raises in SQL server due to the presence of
    #above characters. Hence they are replaced
    #Function takes input a string and returns a string
    #NOTE-THe input is the hash code
    l=''
    s=list(s)
    ref=[]
    for i in range(97,123):
        ref.append(chr(i))
    #ref is a list contains reference to replace the characters
    refno=s.count('\\')+s.count('[')+s.count(']')+s.count('(')
    refno+=s.count(')')+s.count('{')+s.count('}')+s.count('"')
    refno+=s.count("'")
    ref=shulist(refno,ref)
    character=['\\','[',']','(',')','{','}','"',"'",'<','>']
    #all characters are put into a list
    for i in range(len(s)):
        k=s[i]
        if k in ('\\','[',']','(',')','{','}','"',"'",'<','>'):
            s[i]=ref[character.index(k)]
    for i in s:
        l=l+i
    #l is the return valu
    return l
            
def hs_hashpass(s):
    #Function takes input a string and returns a list of 5 strings
    #function returns False if all characters in the password are same
    #function returns a list of 5 strings

    #To check if all characters are same
    if s[0]*(len(s))==s:
        return False
    
    l=hs_hashcode(s)
    l=chrreplace(l)
    rand=[]
    for i in range(5):
        #random character is selected
        ch=chr(int(ran(36,125)))
        #random index number of a string of 500 characters is selected
        inde=int(ran(0,499))
        #random password 
        ranp=l[:inde]+ch+l[inde+1:]
        ranp=chrreplace(ranp)
        rand.append(ranp)
    #random index number is selected
    inde=int(ran(0,4))
    password=[]
    password=rand[:inde]
    password.append(l)
    password.extend(rand[inde+1:])
    return password

def hs_passverify(a,b):
    #function takes input 'a' (a list) and 'b' (a string)
    #returns True, if password is correct
    #False, otherwise

    l=hs_hashcode(b)
    l=chrreplace(l)
    flag=0
    for i in a:
        if i==l:
            flag=1
            return True
    if flag==0:
        return False


def encrfile(a,skey=''):
    #funtions takes input a file path and gives output which is stored in a file
    #output is False if message is non encryptable
    #output if no error will be  a string
    f=open(a,'r')
    a=f.read()
    f.close()
    p=se(a,skey)
    smul=1
    for i in skey:
        smul+=ord(i)
    #P is reversed
    p=p[::-1]
    #now p contains the encrypted text
    l=[]
    for i in p:
        l.append((ord(i))+smul*len(skey))
    #l contains the encrypted text
    #fileen will contain the entire encrypted text
    fileen=[]
    has=hs_hashcode(skey)
    for i in has:
        fileen.append(ord(i))
    fileen.extend(l)
    fileen=str(fileen)
    #first 500 characters contains the hash of skey
    return fileen

def Filedecr(a,skey=''):
    #function takes input the a file path and returns a string which is the decrypted
    #message is a list output is a string
    #function returns False if message is incorrect
    #checking list of hash's ord
    f=open(a,'r')
    a=f.read()
    f.close()
    a=a[1:-1].split(', ')
    try:
        for i in range(len(a)):
            a[i]=int(a[i])
    except:return False
    haslsit=a[:500]
    a=a[500:]
    has=''
    for i in haslsit:
        has=has+chr(i)
    #l is the hash of skey taken as input
    l=hs_hashcode(skey)
    if l==has:
        pass
    else:
        return False
    smul=1
    for i in skey:
        smul+=ord(i)
    #dec will contain the decrypted text in reverse
    dec=''
    for i in a:
        dec=dec+chr(i-smul*len(skey))
    dec=dec[::-1]
    p=sd(dec,skey)
    #p is the decrypted text
    return p

def HS_authenticate(a,skey=''):
    #Function authenticates the encrypted file
    #function takes input path of file
    #returns True of file contents are correct
    #returns False otherwise
    f=open(a,'r')
    a=f.read()
    f.close()
    a=a[1:-1].split(', ')
    try:
        for i in range(len(a)):
            a[i]=int(a[i])
    except:return False
    haslsit=a[:500]
    a=a[500:]
    has=''
    for i in haslsit:
        has=has+chr(i)
    #l is the hash of skey taken as input
    l=hs_hashcode(skey)
    if l==has:
        pass
    else:
        return False
    smul=1
    for i in skey:
        smul+=ord(i)
    #dec will contain the decrypted text in reverse
    dec=''
    for i in a:
        dec=dec+chr(i-smul*len(skey))
    dec=dec[::-1]
    return HS_authenticateme(dec,skey)
    

#Functions End

