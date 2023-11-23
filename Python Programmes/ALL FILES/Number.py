'''9. USER DEFINED MODULE – 1
AIM: To create an user defined module NUMBER to include 2 user defined functions
PALINDROME(), SPECIAL() and import this module in another python code and execute the
functions
METHODOLOGY: A module NUMBER is created to include the 2 functions namely
PALINDROME() which takes a number as parameter and returns 1 if it’s a palindrome and -1
otherwise; SPECIAL() which takes a number as parameter and returns 1 if it’s a special
number and -1 otherwise.
This module is imported in another python code and both the functions are executed. For the
PALINDROME() function, a tuple of integers are read and the code displays all the palindrome
numbers in the tuple. If there weren’t any palindrome numbers appropriate message is
shown. For the SPECIAL() function 2 limits are read and all the special numbers between
these limits are generated. If there were no special numbers, appropriate message is shown.
Note: Create a module NUMBER to include the functions, with each function to include
docstrings to describe the function. Also write a python code to import this module and use the
two functions for inputs from the user.
i) palindrome() to take as parameter a number and returns 1 if the number is a palindrome and
–1 otherwise. This function to be tested with a tuple of integers
ii) special() - takes as parameter a number and returns 1 if it’s a special number and -1
otherwise. [ A special number is a number equal to the sum of the factorial of the individual
digits of the number] This function to be tested to generate list of special numbers between
two limits accepted from the user.'''
def PALINDROME(i):
    reversed_num = 0
    while i != 0:
        digit = i % 10
        reversed_num = reversed_num * 10 + digit
        i //= 10
    if i==reversed_num:
        return 1
    else:
        return -1
def SPECIAL(ll,ul):
    l=[]
    for i in range(ll,ul+1):
        s=0
        f=0
        while i!=0:
            num=i%10
            for j in range(1,num+1):
                f*=j
            s+=f
        if i==s:
            l.append(1)
        else:
            l.append(-1)
    print(l)
    if 1 in l:
        return 1
    else:
        return -1
a=1001
b=5
c=10
d=PALINDROME(a)
e=SPECIAL(b,c)
print(d,e)
        
