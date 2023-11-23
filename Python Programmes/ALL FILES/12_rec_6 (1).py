def vowel(t1):
    t2=()
    for i in t1:
        if 'a' in i.lower() and 'e' in i.lower() and 'i' in i.lower() and 'o' in i.lower() and 'u' in i.lower():
            t2+=(i,)
    print(t2)
def bmi(t1):
    for i in t1:
            bmi=i[1]/(i[0]**2)
            if bmi >= 30:
                print('Your BMI is',round(bmi,3),'and you are Obese')
            elif bmi > 25:
                print('Your BMI is',round(bmi,3),'and you are Overweight')
            elif bmi >= 18.5 and bmi <= 25:
                print('Your BMI is',round(bmi,3),'and you are Normal')
            elif bmi < 18.5:
                print('Your BMI is',round(bmi,3),'and you are Underweight')
print('''
===============MENU===============
1. Display words with all vowels
2. Check BMI
3.Exit''')
while True:
    ch=int(input('Enter the menu code:'))
    if ch==1:
        n=int(input('Enter the number of values:'))
        t=()
        for i in range(n):
            x=input('Enter the string:')
            t+=(x,)
        vowel(t)
    elif ch==2:
        n=int(input('Enter the number of values:'))
        t=()
        for i in range(n):
            t2=()
            for j in range(1):
                h=float(input('Enter the height in m:'))
                w=float(input('Enter the weight in kilograms:'))
                t2+=(h,w)
            t+=(t2,)
        print(t)
        bmi(t)
    elif ch==3:
        print('The Program is ended')
        break
    elif ch<1 or ch>3:
        print('Incorrect menu code')
