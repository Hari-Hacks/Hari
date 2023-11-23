'''
13.WAP to input 'n' company names as keys; the values should be a nested
dictionary whose key will be a product name & value will be the price
eg : D= {'SONY': {'TV': 56000, 'MOBILE' : 32000, 'LAPTOP': 45000}, 'HP': {'Printer': 12000, 'PC': 25000}} & do the
following:
1. Print products company wise
2. Print only company name
3. Print company, product, price in tabular form
4. search for a company & if found print its details'''
from json import*
n=int(input('Enter the no. of companies:'))
d={}
for i in range(n):
    com_nam=input('enter the company name:')
    prod_nam=input('Enter the product name:')
    price=float(input('enter the price:'))
    d[com_nam]={prod_nam:price}
print('''
1. Print products company wise
2. Print only company name
3. Print company, product, price in tabular form
4. search for a company & if found print its details
5. Quit''')
while True:
    ch=int(input('Enter the menu code:'))
    if ch==1:
        for i in d:
            print(i,':')
            for j in d[i]:
                print('    ',end='')
                print(j)
            print('-'*50)
    if ch==2:
        for i in d:
            print(i)           
    if ch==3:
        print(dumps(d,indent=4))
    if ch==4:
        search=input('Enter the company name:')
        for i in d:
            if search==i:
                print(i,dumps(d[i],indent=2))
    if ch==5:
        print('The program has ended')
        break
