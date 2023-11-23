'''Write a program, which will find all such numbers between two limits (both 
included) such that each digit of the number is an even number or odd number .
The numbers obtained should be written in a dictionary with number as key and value as nested dictionary with “odd” as key and count of odd numbers as value and even as key and count of even number as value .Display the output printed in a commaseparated sequence on a single line of each key
Suppose the limit is 1121 to 1125
Dictionary created should be
{1121:{“odd”:3,”even”:1},1121:{“odd”:3,”even”:1},1122:{“odd”:2,”even”:2},1123:{“odd”:3,”even”:1},1124:{“odd”:2,”even”:2},1125:{“odd”:3,”even”:1}}
Output should be
Number :1121 ,”no odd:-”3,”no even:-“1
Number :1122 ,”no odd:-”2,”no even:-“2
Number :1123 ,”no odd:-”3,”no even:-“1
Number :1124 ,”no odd:-”2,”no even:-“2
Number :1125 ,”no odd:-”3,”no even:-“1'''
ll=int(input('Enter the lower limit:'))
ul=int(input('enter the upper limit:'))
d={}
for i in range(ll,ul+1):
    odd=0
    even=0
    for j in range(len(str(i))):
        if int(str(i)[:j+1])%2==0:
            even+=1
        else:
            odd+=1
    d[i]={'odd':odd,'even':even}
print(d)
for i in d:
    print('Number: ',i,' no. odd ',d[i]['odd'],' no. even: ',d[i]['even'])