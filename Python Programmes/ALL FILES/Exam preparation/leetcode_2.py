l=eval(input('Enter the array of strings:'))
l2=[]
for i in l:
    l2.append(i[::-1])
print(l2)
print('*'*50)
l3=[]
for i in range(len(l)):
    str1=''
    for j in range(len(l[i])):
        if l[i][j:j+1]==l2[i][j:j+1]:
            str1+=l[i][j:j+1]
    print(str1)
    print('+'*50)
    l3.append(str1)
print(l3)
print('-'*50)
d={}
for i in range(len(l)):
    d[l[i]]=l3[i]
print(d)
'''s = input("Enter string")
res = str()
for i in range(len(s)):
    for j in range(i,len(s)):
        if len(res) < len(s[i:j+1]) and (s[i:j+1][::-1] == s[i:j+1]):
            res = s[i:j+1]
print(res)'''