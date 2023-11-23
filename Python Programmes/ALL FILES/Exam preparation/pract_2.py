#8. WAP to create a dictionary ITEM to have as key the prod ID,#as value a nested dictionary with details of
#productname, price & stock
#print('''
#1.Add an item
#2. Display all items
#3. Increase the price of a given product ID by a given amount
#4. Item name with the max price
#5. Remove all items with stock less than 10
#6. Exit ''')'''
d={}
n=int(input('enter the no. of items:'))
for i in range(n):
    itm_id=int(input('Enter the product id:'))
    prod_name=input('Enter the product name:')
    price=float(input('Enter the product price:'))
    stock=int(input('Enter the stock amount:'))
    d[itm_id]={'product':prod_name,'price':price,'stock':stock}
print('''
1.Add an item
2. Display all items
3. Increase the price of a given product ID by a given amount
4. Item name with the max price
5. Remove all items with stock less than 10
6. Exit ''')
while True:
    ch=int(input('Enter the menu number:'))
    if ch==1:
        itm_id=int(input('Enter the product id:'))
        prod_name=input('Enter the product name:')
        price=float(input('Enter the product price:'))
        stock=int(input('Enter the stock amount:'))
        d[itm_id]={'product':prod_name,'price':price,'stock':stock}
        print(d)
    elif ch==2:
        print(d)
    elif ch==3:
        id=int(input('enter the product id:'))
        amt=float(input('Enter the increase in price amt:'))
        if id in d:
            d[id]['price']+=amt
        print(d)
    elif ch==4:
        max=0
        for i in d:
                if d[i]['price']>max:
                    max=d[i]['price']
        for i in d:
            if d[i]['price']==max:
                print('the product which has max price is',d[i]['product'],' of price',d[i]['price'])
    elif ch==5:
        d1=d.copy()
        for i in d1:
            if d[i]['stock']<10:
                del d[i]['stock']
        else: print('no product has stock less than 10')
        print(d)
    elif ch==6:
        print('the program has ended')
        break
    else:
        print('Invalid menu code')