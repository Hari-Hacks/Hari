#Programme no.13_Pg 140
qty=float(input('Enter the quantity of the item sold:'))
val=float(input('Enter the value of the item:'))
dis=float(input('Enter the discount percentage:'))
tax=float(input('Enter the  tax:'))
amt=qty*val
dis_amt=(amt*dis)/100
sub_total=amt-dis_amt
tax_amt=(sub_total*tax)/100
total_amt=sub_total+tax_amt
print('****************BILL*******************')
print(' Quantity sold:\t',qty)
print('Price per item:\t',val,'\n\t------------------','\nAmount:\t\t',amt,'\nDiscount:\t\t',dis_amt,'\n\t------------------','\nDsicounted total:\t',sub_total,'\nTax: \t\t',tax_amt,'\n\t------------------','\nTotal amount to be paid:',total_amt)
