import csv
with open('GST.csv','w',newline='') as f:
    l=csv.writer(f)
    l.writerow(['CATEGORY','GST_PERCENTAGE'])
    l.writerows([['Automobiles','25'],['Stationary','12']])
    l.writerows([['Chocolates','10'],['Dairy','3']])
f=open('GST.csv','r',newline='')
l1=csv.reader(f)
l={}
for i in l1:
    l[i[0]]=i[1]
f.close()
with open('ITEMS.csv','w',newline='') as f:
    a=csv.writer(f)
    n=int(input("Enter number of items : "))
    for i in range(n):
        print("Item No.",i+1)
        it=input("ItemID : ")
        na=input("Name : ")
        ca=input("Category : ")
        if ca.lower().title() in l:
            k=ca.lower().title()
            u=int(input("Unitprice : "))
            fin=u+(u*(int(l[k]))/100)
            a.writerow([it,na,k,u,fin])
        else:
            print("Category unavailable")
with open('ITEMS.csv','r',newline='') as f:
    l=csv.reader(f)
    print('[Item,Name,Category,Unit price,Final Price]')
    for i in l:
        print(i)
    
    
            
    

