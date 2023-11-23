'''13. Write a Python code to create a dictionary of ‘n’ items (Name of item will be the key and value will be a
nested dictionary with stock, price ) by reading values from user. Read another such nested dictionary with
freshly arrived ‘m’ items(Name, stock, price). Update the 1st dictionary using the 2nd dictionary – i.e if item
name of 2nd dictionary exists in the 1st dictionary, increase the stock of that item in the 1st dictionary. If item
name does not exist, include the detail as a new item in the 1st dictionary. Display the updated dictionary.
(eg) if D1 has: { “Soap”: { “Stock”:50, “Price”: 25 }, “Tea” : {“Stock”: 20,“Price”: 35.00} }
if D2 has: { “Soap” :{“Stock”:100, “Price”: 25}, “Pen”:{“Stock”:50, “Price”:17.50} }
D1 should become: {“Soap”: {“Stock”:150, “Price”:25}, “Tea” : {“Stock”: 20,“Price”: 35.00}, “Pen”:{“Stock”:50, “Price”: 17.50} }'''
n=int(input('Enter the no. of items:'))
d1={}
for i in range(n):
    d3={}
    item=input('Enter the product name:')
    stock=int(input('enter the stock amount:'))
    price=float(input('enter the price amount:'))
    d3['stock']=stock
    d3['price']=price
    d1[item]=d3
print(d1)
d2={}
m=int(input('enter the no. of items:'))
for i in range(m):
    d4={}
    item=input('Enter the product name:')
    stock=int(input('enter the stock amount:'))
    price=float(input('enter the price amount:'))
    d4['stock']=stock
    d4['price']=price
    d2[item]=d4
print(d2)
for i in d2:
        if i in d1:
            d1[i]['stock']+=d2[i]['stock']
        else:d1[i]=d2[i]        
print(d1)