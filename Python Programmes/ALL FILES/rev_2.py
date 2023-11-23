'''21. Define a function addup() with list and no of elements as argument ,in which all even positions
(0,2,4,…) of the list should be added with content of the element in the next position and odd
position(1,3,5…) elements should be incremented by 10.
Eg if the list is
A= 23 30 45 10 15 25
Output should be
A=53 40 55 20 40 35
Note
 The function should only alter the content in the same array.
 The function should not copy the altered content in another array .
 The function should not display the altered content of the array.
 Assuming the number of element in the array are even.'''
l=eval(input('enter the list:'))
n=len(l)
def addup(n):
    for i in range(n):
        if i % 2 == 0:
            l[i]+=l[i+1]

        else:
            l[i]+=10

    print(l)
addup(n)