from random import randint
flag=0
toss=input('Choose whether odd or even:')
toss_num=int(input('Enter the toss number:'))
pc_toss_num=randint(1,10)
toss_tot=(toss_num+pc_toss_num)%2
print('Toss tot',toss_tot)
print('toss',toss)
print('toss num',pc_toss_num)
if (toss_tot==0 and toss == 'even') or (toss_tot==1 and toss == 'odd'):
    print('Choose whether you want to bowl or bat:',end=' ')
    user_choice=input()
else:
    l=['bat','bowl']
    pc_choice=randint(0,1)
    if pc_choice==0:
        print('You are going to Bat')
        print('Computer is going to Bowl')
        user_choice='bat'
    else:
        print('You are going to Bowl')
        print('Computer is going to Bat')
        user_choice='bowl'
#user batting
print(user_choice)
if user_choice=='bat':
    score=target=0
    over=[]
    while True:
        nest_over=[]
        for j in range(6):
            bat_num=int(input('Enter the number:'))
            bowl_num=randint(1,5)
            print(bowl_num)
            if bat_num==bowl_num:
                flag=1
                break
            score+=bat_num
            target+=score
            nest_over.append(bat_num)
            print(nest_over)
        over.append(nest_over)
        if flag==1:
            break
    print(over)
    target=score+1
    print(score)
    print(target)
#user bowling
if user_choice=='bowl':
    score=target=0
    over=[]
    while True:
        nest_over=[]
        for j in range(6):
            bowl_num=int(input('Enter the number:'))
            bat_num=randint(1,5)
            print(bat_num)
            if bat_num==bowl_num:
                flag=1
                break
            score+=bat_num
            target+=score
            nest_over.append(bat_num)
            print(nest_over)
        over.append(nest_over)
        if flag==1:
            break
    print(over)
    target=score+1
    print(score)
    print(target)
#IInd innings
if user_choice=='bat':
    user_choice='bowl'
    score1=target1=flag1=0
    over=[]
    while True:
        nest_over=[]
        for i in range(6):
            bowl_num=int(input('Enter the number:'))
            bat_num=randint(1,5)
            if bat_num==bowl_num:
                flag1=1
                break
            score+=bat_num
            target1+=score1
            nest_over.append(bat_num)
            print(nest_over)
            if target1<target:
                print('You have won')
                break
            elif target1>target:
                print('You have lost')
                break
            elif target1==target:
                print('Its an tie')
                break
        over.append(nest_over)
        if flag1==1:
            break
    print(over)
    target1=score+1
    print(score)
    print(target)
if user_choice=='bowl':
    user_choice='bat'
    score1=target1=flag1=0
    over=[]
    while True:
        nest_over=[]
        for i in range(6):
            bat_num=int(input('Enter the number:'))
            bowl_num=randint(1,5)
            if bat_num==bowl_num:
                flag1=1
                break
            score+=bat_num
            target1+=score1
            nest_over.append(bat_num)
            print(nest_over)
            if target1<target:
                print('You have lost')
                break
            elif target1>target:
                print('You have won')
                break
            elif target1==target:
                print('Its an tie')
                break
        over.append(nest_over)
        if flag1==1:
            break
    print(over)
    target1=score+1
    print(score)
    print(target)