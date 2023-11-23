a=int(input('enter the no. of tuples:'))
b=int(input('enter the no. of elements in a tuple:'))
t=()
for i in range(a):
    t1=()
    for j in range(b):
        t1+=int(input('enter the element:')),
    t+=t1,
print(t)
t_mean=()
for i in t:
    s=0
    for j in i:
        s+=j
    t_mean+=(s/b),
print(t_mean)
s=0
for i in t_mean:
    s+=i
print(s/a)

