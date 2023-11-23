'''Read a dictionary of 5 items with Item ID as the key and the value to be Item name, Price.
Display the name of the item with prices in the range Rs. 200 to 500(limits inclusive).Also
display the total price of items falling in this price range'''
n=5
d={}
for i in range(n):
    itm_id=int(input('enter the item id:'))
    itm_name=input('Enter the item name:')
    price=int(input('Enter the price:'))
    d[itm_id]={'item name':itm_name,'price':price}
print(d)
s=0
for i in d:
    if (d[i]['price']>=200) and (d[i]['price']<=500):
        print('The name of the item is',d[i]['item name'])
        s+=d[i]['price']
print('the total price of items falling in this price range is',s)