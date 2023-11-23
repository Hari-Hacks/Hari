exam={}
n=int(input('enter the no. of students:'))
for i in range(n):
    roll_no=int(input('Enter the roll number:'))
    quaterly=input('Enter the quaterly marks:')
    half=float(input('Enter the half yearly marks:'))
    annual=int(input('Enter the annual marks:'))
    exam[roll_no]={'quaterly':quaterly,'half yearly':half ,'annual':annual}
max=0
for i in exam:
    if exam[i]['annual']>max:
        max=exam[i]['annual']
for i in exam:
    if max==exam[i]['annual']:
        print('The person who scored the highest marks in annual exam is',i,'with a score of',exam[i]['annual'],sep=' ')