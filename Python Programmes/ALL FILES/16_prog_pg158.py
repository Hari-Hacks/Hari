#Prgramme no.16_pg 158
ch=input('Enter any character:')
if ch>='A' and ch<='Z':
    ch=ch.lower()
    print('The entered character was in upper case. In lower case it is:',ch)
else:
    ch=ch.upper()
    print('The entered character was in lower case. In upper case it is:',ch)
