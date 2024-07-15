str='moon is beautiful'
b=str.split()
for i in range(len(b)):
    b[i]=chr(ord(b[i][0])-32)+b[i][1::]
' '.join(b)
print(b)