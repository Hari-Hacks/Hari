'''import pickle#1.To import appropriate module
Num = { 1: 'I', 4 : 'IV', 5 : 'V', 9: 'IX', 10:'X', 40 : 'XL', 50 : 'L', 100 : 'C'}
F1 = open('roman.bin','wb') #2. To open Roman.bin in for writing
pickle.dump(Num,F1)#3. To write the dictionary into the file
F1.close()
F2=open('roman.bin', 'rb')
X=pickle.load(F2)#4.To load the record into X
N=0
while N != -1:
    N=int(input('Enter 1,4,5,9,10,40,50,100 and -1 to exit' ))
    if N == -1: break
    else: print('Roman numeral of', N , 'is ', Num[N]) #5. To display result
'''
X = 200
def XXX( A = 15, B = 30) :
    global X
    if A % 3 == 0: X+= A // 10
    else: X += B % 7
    Sum = A + B + X
    print( X, Sum, sep= '@', end=':')
XXX()
XXX(18,50)
XXX(B=12, A= 4)