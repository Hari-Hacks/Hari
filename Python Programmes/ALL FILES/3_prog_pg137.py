#Programme no.3_Pg 137
a=float(input('Enter the first side of the triangle:'))
b=float(input('Enter the second side of the triangle:'))
c=float(input('Enter the third side of the triangle:'))
print(a,b,c)
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print('Area=',area)
