#Programme no.17_pg158
ch=input('Enter the sex of the employee (m or f):')
sal=int(input('Enter the salary of the employee :'))
if ch=='m':
    bonus=0.05*sal
else: bonus=0.10*sal
amt_paid=sal+bonus
print('Salary =',sal,'\nBonus =',bonus,'\n**************************','\nAmount to be paid :',amt_paid)

