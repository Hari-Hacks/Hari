n=int(input('enter a number without zero:'))
h=list(str(n))
l=[]
m=['1','2','3','4','5','6','7','8','9']
l=['I','II','III','IV','V','VI','VII','VIII','IX']
d={}
for i in range(len(h)):
    for j in range(9):
        if m[j]==h[i]:
            d[int(h[i])]=l[j]
print(d)