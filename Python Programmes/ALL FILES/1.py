name=input('enter your name: ')
salary=int(input(' enter your salary: '))
HRA=int(input('enter your HRA: '))
DA=int(input('enter your DA: '))
if salary>6000:
 bonus=10
elif 6000>=salary>5000:
 bonus=8
elif 3500<salary<=5000:
 bonus=6
else:
 bonus=5
net=salary+(salary*bonus/100)+HRA+DA
print()
print('\t\t\tNet Salary Calculator')
print('\t\t\t----------+----------')
print()
print(name,',your net salary is',net)
