#12. Create a dictionary to have key as decimal numbers and value as its octal equivalent
n=int(input('Enter the no. of numbers:'))
d={}
for i in range(n):
    dec=int(input('Enter the decimal number:'))
    oct=0
    i=0
    while dec:
        dig=dec%8
        oct+=dig*10**i
        i+=1
        dec//=8
    d[dec]=oct
print(d)