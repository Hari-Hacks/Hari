#Programme no.18_pg159
yr=int(input('Enter any year:'))
if (yr%4==0 and yr%100!=0) or (yr%400==0):
    print('Leap year')
else: print('Not a leap year')
