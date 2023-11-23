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
    if 1 < l <=500:
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
        fi_s=char_compression(l)
        main=''
        for i in range(len(fi_s)):       
            while len(fi_s[i]) < 500:
                c=0
                b=int(fi_s[i])
                c=b**2
                fi_s[i]=str(c)
            main+=fi_s[i][:-501:-1]
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
    main=main[:500] 
    #Main is the hash value            
    return main
