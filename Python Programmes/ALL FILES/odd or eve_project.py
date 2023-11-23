'''1stu toss'''
from random import randint
toss=input('Choose whether Odd or Even:')
toss_num=int(input('Enter number for toss:'))
pc_num=randint(0,10)
result=pc_num+toss_num
if result%2==0:
    toss_result='even'
else:
    toss_result='odd'
if toss_result==toss:
    print('Choose whether you want to bowl or bat:',end=' ')
    user_choice=input()
else:
    print('You have lost the toss\n')
    l=['bat','bowl']
    a=randint(0,1)
    pc_choice=l[a]
    if pc_choice=='bat':
        user_choice='bowl'
        print('Computer has chosen to bat')
        print('You are going to bowl\n')
    else:
        user_choice='bat'
        print('Computer has chosen to bowl')
        print('You are going to bat\n')
        print('Your Innings starts')
print('*'*50)
#Ist innings
if user_choice=='bat':
    over=[]
    score=0
    flag=0
    while True:
        nest_over=[]
        for i in range(6):
            bat_num=int(input('Enter run:'))
            bowl_num=randint(1,5)
            print(bowl_num)
            score+=bat_num
            nest_over+=[bat_num]
            print(nest_over)
            if bat_num==bowl_num:
                flag=1
                break
        over.append(nest_over)
        if flag==1:
            target=score+1
            break
    print(over)
    print(score)
    print(target)
        