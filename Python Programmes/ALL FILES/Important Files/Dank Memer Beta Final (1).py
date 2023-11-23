
#Importing Modules

import math as m
import random as r
import time as t


'''#Functions for Login and Signup

db = open("database.txt", "w")

def signup():

    global db
    db=open("database.txt","r")
    user=input("Enter a username : ")
    pwd=input("Enter a password : ")
    pwd1=input("Confirm password : ")
    
    if pwd!=pwd1:
        print("passwords do not match")
        signup()
        
    elif (len(pwd))<6:
        print("select a bigger password")
        signup()
        
    elif user in db:
        print("Username already taken")
        signup()
        
    else:
        db =open("database.txt","a")
        db.write(user+", "+pwd)
signup()
--------------------------
db={}
def signup():

    global db
    
    user=input("Enter a username : ")
    pwd=input("Enter a password : ")
    pwd1=input("Confirm password : ")
    
    if pwd!=pwd1:
        print("passwords do not match")
        signup()
        
    elif (len(pwd))<6:
        print("select a bigger password")
        signup()
        
    elif user in db:
        print("Username already taken")
        signup()
        
    else:
        db.update({user:pwd})

def auth():

    global db

    user=input("Enter your username : ")
    pwd=input("Enter your password : ")
    a=db[user]
    if a==pwd:
        print("Sucessfully Logged in")
    else:
        print("Username or Password incorrect")


#Login and Signup

lgn=int(input("Log-in or Sign-up ?(1/2)"))
        
if lgn==2:
    signup()
    auth()
if lgn==1:
    auth()'''


#Main Variables

name = input("Enter your name :- ")

bal=0
inv=[[],[],[],[]]
work=""
salary=0

print(""" Welcome to dank memer

          i will explain the game now

          This is an text based RPG game which is still in development.
          You can search different locations and if your lucky you might
          find some money. If not you die . You can use the bank to
          deposit and withdraw your money.

          Buy equipments you need and go for hunting and fishing.
          sell whatever you got in the shop and increase your networth.
          Pick a job and work in shifts to gain money.

          There is no save state in the game so your progess wont be saved

          """)
#Player inventory

 #Fishes
crab=0
goldfish=0
tropicalfish=0
shark=0
   
 #Animals
skunk=0
rabbit=0
deer=0
boar=0

 #Items
hrifle=0
fpole=0
laptop=0
padlock=0

#Functions for inventory

def invupdate(x):

    global inv
    global crab
    global goldfish
    global tropicalfish
    global shark
    global skunk
    global rabbit
    global deer
    global boar
    
    for g in inv[x]:
        
        if '🦀crab'==g:
            crab+=1            
        elif '🐟gold fish'==g:
            goldfish+=1
        elif '🐠tropical fish'==g:
            tropicalfish+=1
        elif '🦈shark'==g:
            shark+=1
        elif '🦨skunk'==g:
            skunk+=1
        elif '🐇rabbit'==g:
            rabbit+=1
        elif '🦌deer'==g:
            deer+=1
        elif '🐗boar'==g:
            boar+=1
    
def invshow():

    global crab
    global goldfish
    global tropicalfish
    global shark
    global skunk
    global rabbit
    global deer
    global boar
    global fpole
    global hrifle
    global laptop
    global padlock

    print("\n YOUR INVENTORY \n")
    print("🦀CRABS :",crab,"\n🐟GOLD FISHES :",goldfish,"\n🐠TROPICAL FISHES :",tropicalfish,"\n🦈SHARKS :",shark,"\n")
    print("🦨SKUNKS :",skunk,"\n🐇RABBITS :",rabbit,"\n🦌DEERS :",deer,"\n🐗BOARS :",boar,"\n")
    print("FISHING POLES :",fpole,"\nHUNTING RIFLES :",hrifle,"\nLAPTOPS :",laptop,"\nPADLOCKS :",padlock,"\n")

#Search locations

srch = ['Guha home','Air' , 'Attic' , 'Bank' , 'Basement' ,'Bed' , 'beehive' , 'book' ,
        'Car' , 'Coffee' , 'Dark Room' ,'Dank museum' , 'puppy' , 'dumpster' , 'fridge' ,
        'grass' , 'hospital' ,'purse' , 'sewer' , 'shoe' , 'tree' , 'tesla' , 'street' ,
        'souls chamber']

#Location comments

a0=[', oh it was in my home ?','the securities killed you']
a1=[', out of AIR ?!?','so how did u die ? AIR :)']
a2=[', wasnt it dusty','the rats bit u to death']
a3=[', so ur a criminal now ?','The police caught you']
a4=[', woah u have guts','u tripped in the staircase']
a5=[', you sleep on money, dont you','the monster under the bed welcomes you']
a6=[', RUN !! the bees are chasing you','you got stinged by the bees']
a7=[', this is why you open your book once in a while','wrong book']
a8=[', vroom !','you got hit by the car']
a9=[', *slurps*','you choked while drinking the coffee']
a10=[', the ghosts were watching you','you are officially possesed by the ghost']
a11=[', how dare you','you couldnt escape']
a12=[', poor puppy','the puppys parents arrived and bit you']
a13=[', thats nasty','the cat scratched you']
a14=[', why was it there anyways ?','you got frostbites']
a15=[', time to bring that lawnmower','you got infested']
a16=[', you stole from the patients...','u died from the diseases there']
a17=[', WHOA UR RICH','there isnt anything , what would u expect']
a18=[', you escaped the maze','you got lost']
a19=[', you have money in your footsteps','you fainted from the stinky smell']
a20=[', hope the birds dont mind that','the birds are chasing you']
a21=[', *calls elon musk*','tesla sued you']
a22=[', so you were the reason for the traffic jam','you got hit by a truck']
a23=[', .......','you lost your soul']

#Functions for Search option

def rands(x):
    abc=r.choices(x,weights=(75,25))
    
def randsearch():
    global padlock
    global bal
    global srch
    
    bal1=0
   
    ops=r.sample(srch,3)
    
    print("\n Where do you want to search now",name,"? (1/2/3) \n",ops,"\n")
    b=input("= ")
    if b == '1':
        for j in srch :
            if j == ops[0]:
                
                mon1 = r.randrange(50,10000)
                selection=[0,mon1]
                money=(r.choices(selection,weights=(25,75)))
                mon=money[0]

                for k in range (len(srch)):
                    if srch[k]==j:
                        b=k
                    if b == 0:
                        if mon!=0:
                            abc=a0[0]
                        else:
                            abc=a0[1]                        
                    elif b == 1:
                        if mon!=0:
                            abc=a1[0]
                        else:
                            abc=a1[1]
                    elif b == 2:
                        if mon!=0:
                            abc=a2[0]
                        else:
                            abc=a2[1]
                    elif b == 3:
                        if mon!=0:
                            abc=a3[0]
                        else:
                            abc=a3[1]
                    elif b == 4:
                        if mon!=0:
                            abc=a4[0]
                        else:
                            abc=a4[1]
                    elif b == 5:
                        if mon!=0:
                            abc=a5[0]
                        else:
                            abc=a5[1]
                    elif b == 6:
                        if mon!=0:
                            abc=a6[0]
                        else:
                            abc=a6[1]
                    elif b == 7:
                        if mon!=0:
                            abc=a7[0]
                        else:
                            abc=a7[1]
                    elif b == 8:
                        if mon!=0:
                            abc=a8[0]
                        else:
                            abc=a8[1]
                    elif b == 9:
                        if mon!=0:
                            abc=a9[0]
                        else:
                            abc=a9[1]
                    elif b == 10:
                        if mon!=0:
                            abc=a10[0]
                        else:
                            abc=a10[1]
                    elif b == 11:
                        if mon!=0:
                            abc=a11[0]
                        else:
                            abc=a11[1]
                    elif b == 12:
                        if mon!=0:
                            abc=a12[0]
                        else:
                            abc=a12[1]
                    elif b == 13:
                        if mon!=0:
                            abc=a13[0]
                        else:
                            abc=a13[1]
                    elif b == 14:
                        if mon!=0:
                            abc=a14[0]
                        else:
                            abc=a14[1]
                    elif b == 15:
                        if mon!=0:
                            abc=a15[0]
                        else:
                            abc=a15[1]
                    elif b == 16:
                        if mon!=0:
                            abc=a16[0]
                        else:
                            abc=a16[1]
                    elif b == 17:
                        if mon!=0:
                            abc=a17[0]
                        else:
                            abc=a17[1]
                    elif b == 18:
                        if mon!=0:
                            abc=a18[0]
                        else:
                            abc=a18[1]
                    elif b == 19:
                        if mon!=0:
                            abc=a19[0]
                        else:
                            abc=a19[1]
                    elif b == 20:
                        if mon!=0:
                            abc=a20[0]
                        else:
                            abc=a20[1]
                    elif b == 21:
                        if mon!=0:
                            abc=a21[0]
                        else:
                            abc=a21[1]
                    elif b == 22:
                        if mon!=0:
                            abc=a22[0]
                        else:
                            abc=a22[1]
                    elif b == 23:
                        if mon!=0:
                            abc=a23[0]
                        else:
                            abc=a23[1]

                print("...")
                t.sleep(3)
                print("You Found ⏣",mon,abc)
                
                bal1+= mon
                bal+=bal1

                if mon==0:
                    if padlock==0:
                        print("...")
                        t.sleep(3)
                        print("You lost your money , deposit in bank to avoid this or buy a padlock")
                        bal=0
                    else:
                        padlock-=1
                        print("Using the padlock...")
                        t.sleep(3)
                        print("You might have lost your money , deposit in bank to avoid this or buy a padlock")
                else:
                    continue

                
    elif b == '2':
        for j in srch :
            if j == ops[1]:
                
                mon1 = r.randrange(50,10000)
                selection=[0,mon1]
                money=(r.choices(selection,weights=(25,75)))
                mon=money[0]

                for k in range (len(srch)):
                    if srch[k]==j:
                        b=k
                    if b == 0:
                        if mon!=0:
                            abc=a0[0]
                        else:
                            abc=a0[1]                        
                    elif b == 1:
                        if mon!=0:
                            abc=a1[0]
                        else:
                            abc=a1[1]
                    elif b == 2:
                        if mon!=0:
                            abc=a2[0]
                        else:
                            abc=a2[1]
                    elif b == 3:
                        if mon!=0:
                            abc=a3[0]
                        else:
                            abc=a3[1]
                    elif b == 4:
                        if mon!=0:
                            abc=a4[0]
                        else:
                            abc=a4[1]
                    elif b == 5:
                        if mon!=0:
                            abc=a5[0]
                        else:
                            abc=a5[1]
                    elif b == 6:
                        if mon!=0:
                            abc=a6[0]
                        else:
                            abc=a6[1]
                    elif b == 7:
                        if mon!=0:
                            abc=a7[0]
                        else:
                            abc=a7[1]
                    elif b == 8:
                        if mon!=0:
                            abc=a8[0]
                        else:
                            abc=a8[1]
                    elif b == 9:
                        if mon!=0:
                            abc=a9[0]
                        else:
                            abc=a9[1]
                    elif b == 10:
                        if mon!=0:
                            abc=a10[0]
                        else:
                            abc=a10[1]
                    elif b == 11:
                        if mon!=0:
                            abc=a11[0]
                        else:
                            abc=a11[1]
                    elif b == 12:
                        if mon!=0:
                            abc=a12[0]
                        else:
                            abc=a12[1]
                    elif b == 13:
                        if mon!=0:
                            abc=a13[0]
                        else:
                            abc=a13[1]
                    elif b == 14:
                        if mon!=0:
                            abc=a14[0]
                        else:
                            abc=a14[1]
                    elif b == 15:
                        if mon!=0:
                            abc=a15[0]
                        else:
                            abc=a15[1]
                    elif b == 16:
                        if mon!=0:
                            abc=a16[0]
                        else:
                            abc=a16[1]
                    elif b == 17:
                        if mon!=0:
                            abc=a17[0]
                        else:
                            abc=a17[1]
                    elif b == 18:
                        if mon!=0:
                            abc=a18[0]
                        else:
                            abc=a18[1]
                    elif b == 19:
                        if mon!=0:
                            abc=a19[0]
                        else:
                            abc=a19[1]
                    elif b == 20:
                        if mon!=0:
                            abc=a20[0]
                        else:
                            abc=a20[1]
                    elif b == 21:
                        if mon!=0:
                            abc=a21[0]
                        else:
                            abc=a21[1]
                    elif b == 22:
                        if mon!=0:
                            abc=a22[0]
                        else:
                            abc=a22[1]
                    elif b == 23:
                        if mon!=0:
                            abc=a23[0]
                        else:
                            abc=a23[1]

                print("...")
                t.sleep(3)
                print("You Found ⏣",mon,abc)
                
                bal1+= mon
                bal+=bal1

                if mon==0:
                    if padlock==0:
                        print("...")
                        t.sleep(3)
                        print("You lost your money , deposit in bank to avoid this or buy a padlock")
                        bal=0
                    else:
                        padlock-=1
                        print("Using the padlock...")
                        t.sleep(3)
                        print("You might have lost your money , deposit in bank to avoid this or buy a padlock")
                else:
                    continue

                
    elif b == '3':
        for j in srch :
            if j == ops[2]:
                
                mon1 = r.randrange(50,10000)
                selection=[0,mon1]
                money=(r.choices(selection,weights=(25,75)))
                mon=money[0]

                for k in range (len(srch)):
                    if srch[k]==j:
                        b=k
                    if b == 0:
                        if mon!=0:
                            abc=a0[0]
                        else:
                            abc=a0[1]                        
                    elif b == 1:
                        if mon!=0:
                            abc=a1[0]
                        else:
                            abc=a1[1]
                    elif b == 2:
                        if mon!=0:
                            abc=a2[0]
                        else:
                            abc=a2[1]
                    elif b == 3:
                        if mon!=0:
                            abc=a3[0]
                        else:
                            abc=a3[1]
                    elif b == 4:
                        if mon!=0:
                            abc=a4[0]
                        else:
                            abc=a4[1]
                    elif b == 5:
                        if mon!=0:
                            abc=a5[0]
                        else:
                            abc=a5[1]
                    elif b == 6:
                        if mon!=0:
                            abc=a6[0]
                        else:
                            abc=a6[1]
                    elif b == 7:
                        if mon!=0:
                            abc=a7[0]
                        else:
                            abc=a7[1]
                    elif b == 8:
                        if mon!=0:
                            abc=a8[0]
                        else:
                            abc=a8[1]
                    elif b == 9:
                        if mon!=0:
                            abc=a9[0]
                        else:
                            abc=a9[1]
                    elif b == 10:
                        if mon!=0:
                            abc=a10[0]
                        else:
                            abc=a10[1]
                    elif b == 11:
                        if mon!=0:
                            abc=a11[0]
                        else:
                            abc=a11[1]
                    elif b == 12:
                        if mon!=0:
                            abc=a12[0]
                        else:
                            abc=a12[1]
                    elif b == 13:
                        if mon!=0:
                            abc=a13[0]
                        else:
                            abc=a13[1]
                    elif b == 14:
                        if mon!=0:
                            abc=a14[0]
                        else:
                            abc=a14[1]
                    elif b == 15:
                        if mon!=0:
                            abc=a15[0]
                        else:
                            abc=a15[1]
                    elif b == 16:
                        if mon!=0:
                            abc=a16[0]
                        else:
                            abc=a16[1]
                    elif b == 17:
                        if mon!=0:
                            abc=a17[0]
                        else:
                            abc=a17[1]
                    elif b == 18:
                        if mon!=0:
                            abc=a18[0]
                        else:
                            abc=a18[1]
                    elif b == 19:
                        if mon!=0:
                            abc=a19[0]
                        else:
                            abc=a19[1]
                    elif b == 20:
                        if mon!=0:
                            abc=a20[0]
                        else:
                            abc=a20[1]
                    elif b == 21:
                        if mon!=0:
                            abc=a21[0]
                        else:
                            abc=a21[1]
                    elif b == 22:
                        if mon!=0:
                            abc=a22[0]
                        else:
                            abc=a22[1]
                    elif b == 23:
                        if mon!=0:
                            abc=a23[0]
                        else:
                            abc=a23[1]

                print("...")
                t.sleep(3)
                print("You Found ⏣",mon,abc)
                
                bal1+= mon
                bal+=bal1

                if mon==0:
                    if padlock==0:
                        print("...")
                        t.sleep(3)
                        print("You lost your money , deposit in bank to avoid this or buy a padlock")
                        bal=0
                    else:
                        padlock-=1
                        print("Using the padlock...")
                        t.sleep(3)
                        print("You might have lost your money , deposit in bank to avoid this or buy a padlock")
                else:
                    continue

                
                
    else:
        "invalid option"

#Bank Functions

bank=0

def deposit(x):
    global bal
    global bank

    if x > bal:
        print("Insufficient money")

    else:
        bank+=x
        bal-=x
        print("\n Succesfully deposited ⏣",x,"\n")



def withdraw(x):
    global bal
    global bank

    if x > bank:
        print("Insufficient money")
        
    else:
        bank-=x
        bal+=x
        print("\n Succesfully withdrawed ⏣",x,"\n")
        
#Variables & Functions for fishing,hunting,digging
        
fishes=['🦀crab','🐟gold fish','🐠tropical fish','🦈shark']
def fishing():

    global inv
    global fishes

    
    a=r.choices(fishes,weights=(55,18,15,12))
    print("...")
    t.sleep(2)
    print("\nYou have caught ",a[0])
    inv[0].append(a[0])

hunts=['🦨skunk','🐇rabbit','🦌deer','🐗boar']
def hunting():

    global inv
    global hunts

    
    a=r.choices(hunts,weights=(55,18,15,12))
    print("...")
    t.sleep(2)
    print("\nYou have hunted ",a[0])
    inv[1].append(a[0])


#Shop and Sell

def buyitem(x,y):
    global bal
    global hrifle
    global fpole
    global laptop
    global padlock

    if x==1:
        if y*10000>bal:
            print("\nInsufficient Money")
        else:
            money=10000*y
            bal-=money
            fpole+=y
            print("\nSucessfully bought ",y,"Fishing Poles")
            print("\n",y,"Fishing Poles added to inventory\n")
            inv[3].append(y*"Fishing Pole")


    elif x==2:
        if y*15000>bal:
            print("\nInsufficient Money")
        else:            
            money=15000*y
            bal-=money
            hrifle+=y
            print("\nSucessfully bought ",y,"Hunting Rifles")
            print("\n",y,"Hunting rifles added to inventory\n")
            inv[3].append(y*"Hunting Rifle")
            
    elif x==3:
        if y*50000>bal:
            print("\nInsufficient Money")
        else:            
            money=15000*y
            bal-=money
            laptop+=y
            print("\nSucessfully bought ",y,"Laptops")
            print("\n",y,"Laptops added to inventory\n")
            inv[3].append(y*"Laptop")

    elif x==4:
        if y*60000>bal:
            print("\nInsufficient Money")
        else:            
            money=60000*y
            bal-=money
            padlock+=y
            print("\nSucessfully bought ",y,"Padlocks")
            print("\n",y,"PadLocks added to inventory\n")
            inv[3].append(y*"Padlock")

    
def sellitem(x,y):

    global bal
    global crab
    global goldfish
    global tropicalfish
    global shark
    global skunk
    global rabbit
    global deer
    global boar
    
    if x==1:
        if y>crab:
            print("\nInsufficient 🦀 crabs in inventory")
        else:            
            money=500*y
            bal+=money
            crab-=y
            print("\nSucessfully sold ",y,"🦀 Crabs")
            print("\n⏣",money," added to balance\n")
            
        
    elif x==2:
        if y>goldfish:
            print("\nInsufficient 🐟 gold fishes in inventory")
        else:      
            money=1000*y
            bal+=money
            goldfish-=y
            print("\nSucessfully sold ",y,"🐟 Gold Fishes")
            print("\n⏣",money," added to balance\n")
          

    elif x==3:
        if y>tropicalfish:
            print("\nInsufficient 🐠 tropical fishes in inventory")
        else:                
            money=2500*y
            bal+=money
            tropicalfish-=y
            print("\nSucessfully sold ",y,"🐠 Tropical Fishes")
            print("\n⏣",money," added to balance\n")
            

    elif x==4:
        if y>shark:
            print("\nInsufficient 🦈 sharks in inventory")
        else:                
            money=4000*y
            bal+=money
            shark-=y
            print("\nSucessfully sold ",y,"🦈 Sharks")
            print("\n⏣",money," added to balance\n")
            

    elif x==5:
        if y>skunk:
            print("\nInsufficient 🦨 skunks in inventory")
        else:                
            money=700*y
            bal+=money
            skunk-=y
            print("\nSucessfully sold ",y,"Skunks")
            print("\n⏣",money," added to balance\n")
            

    elif x==6:
        if y>rabbit:
            print("\nInsufficient 🐇 rabbits in inventory")
        else:                
            money=2000*y
            bal+=money
            rabbit-=y
            print("\nSucessfully sold ",y,"🐇 Rabbits")
            print("\n⏣",money," added to balance\n")
            

    elif x==7:
        if y>deer:
            print("\nInsufficient 🦌 deers in inventory")
        else:                
            money=6000*y
            bal+=money
            deer-=y
            print("\nSucessfully sold ",y,"🦌 Deers")
            print("\n⏣",money," added to balance\n")
            

    elif x==8:
        if y>boar:
            print("\nInsufficient 🐗 boars in inventory")
        else:                
            money=7500*y
            bal+=money
            boar-=y
            print("\nSucessfully sold ",y,"🐗 Boars")
            print("\n⏣",money," added to balance\n")
           
#Functions For Working and getting salary
def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\n')
        t.sleep(1)
        time_sec -= 1


def Work():
    global salary
    global work
    global bal

    if work=='Youtuber':
        countdown(30)
        print("Shift Done")
        bal+=salary
    elif work=='Teacher':
        countdown(40)
        print("Shift Done")
        bal+=salary
    elif work=='Programmer':
        countdown(55)
        print("Shift Done")
        bal+=salary
    elif work=='NBA Player':
        countdown(75)
        print("Shift Done")
        bal+=salary
        

#Main Code For Executing The Program
        
pl=0
while pl == 0:
    play=input('''\nWhat do you want to do now ?

            1)search
            2)balance
            3)fishing
            4)hunting
            5)inventory
            6)bank
            7)shop
            8)sell
            9)work
            10)quit 

            : ''')
    
    if play.lower() == 'search':
        t.sleep(1)
        sr=0
        broo=input("\nShall we start ? (y/n)\n")
        if broo =='y':
            while sr==0:
                randsearch()
                broo1=input("\nDo you want to continue ?(y/n)\n")
                if broo1=='y':
                    continue
                else:
                    sr=1
        else:
            print("\nOkay\n")
        
    elif play.lower() == 'balance':
        t.sleep(1)
        print("\nYour Current Balance is : ⏣",bal)
        print("\nYour Bank Balance is : ⏣",bank)
        
    elif play.lower() == 'bank':
        t.sleep(1)
        bankfun=input("\nWhat would you like to do ?(deposit/withdraw) \n")

        if bankfun.lower()=='deposit':
            t.sleep(1)
            print("(*Type Max to deposit all of your money*)")
            amt=(input("Enter the amount to Deposit : ⏣"))
            if amt.lower() =='max':
                deposit(bal)
            else:
                amt=int(amt)
                deposit(amt)
                
                
        elif bankfun.lower()=='withdraw':
            t.sleep(1)
            print("(*Type Max to Withdraw all of your money*)")
            amt=(input("Enter the amount to Withdraw : ⏣"))
            if amt.lower() =='max':
                withdraw(bank)
            else:
                amt=int(amt)
                withdraw(amt)
                

    elif play.lower()=='fishing':
        t.sleep(1)
        
        if fpole>=1:                
            fsh=0
            bro=input("\nShall we start ? (y/n)\n")
            if bro.lower() =='y':
                while fsh==0:
                    fishing()
                    bro1=input("\nDo you want to continue ?(y/n)\n")
                    if bro1.lower()=='y':
                        continue
                    else:
                        fsh=1
                        invupdate(0)
            else:
                print("\nOkay\n")
        else:
            print("\nNo Fishing Poles in inventory , buy one from the shop\n")

    
    elif play.lower()=='hunting':
        t.sleep(1)        
        if hrifle>=1:            
            hun=0
            sis=input("\nShall we start ? (y/n)\n")
            if sis.lower() =='y':
                while hun==0:
                    hunting()
                    sis1=input("\nDo you want to continue ?(y/n)\n")
                    if sis1.lower()=='y':
                        continue
                    else:
                        hun=1
                        invupdate(1)
            else:
                print("\nOkay\n")
        else:
            print("\nNo Hunting Rifles in inventory , buy one from the shop\n")
        
    elif play.lower()=='inventory':
        t.sleep(1)
        invshow()

    elif play.lower()=='shop':
        t.sleep(1)

        print('''\n\n
                        WELCOME TO THE BUYING AREA
                        ===========================


              FISHING POLE  [1] = ⏣10000  [''',fpole,'''in inventory]

              HUNTING RIFLE [2] = ⏣15000 [''',hrifle,'''in inventory]

                 LAPTOP     [3] = ⏣50000 [''',laptop,'''in inventory]

                 PADLOCK    [4] = ⏣60000 [''',padlock,'''in inventory]


                select the numbers to buy  ''')
        
        t.sleep(2)
        x1=int(input("What do you want to buy ? : "))
        if x1<=4:
            y1=int(input("How much would you want to buy ? : "))
            chs1=input("Can we confirm your order ? (y/n)")
            if chs1.lower()=='y':
                t.sleep(2)
                buyitem(x1,y1)
            else:
                print("\nSee you again later")
        else:
            print("\nProvide a correct option")

        
        
    elif play.lower()=='sell':
        t.sleep(1)

        print('''\n\n

                        WELCOME TO THE SELLING AREA
                        ===========================


              🦀CRAB      [1] = ⏣500  [''',crab,'''in inventory]
            🐟GOLD FISH   [2] = ⏣1000 [''',goldfish,'''in inventory]
          🐠TROPICAL FISH [3] = ⏣2500 [''',tropicalfish,'''in inventory]
             🦈SHARK      [4] = ⏣4000 [''',shark,'''in inventory]

             🦨SKUNKS     [5] = ⏣700  [''',skunk,'''in inventory]
             🐇RABBITS    [6] = ⏣2000 [''',rabbit,'''in inventory]
             🦌DEERS      [7] = ⏣6000 [''',deer,'''in inventory]
             🐗BOARS      [8] = ⏣7500 [''',boar,'''in inventory]

                select the numbers to sell  ''')
        t.sleep(2)
        x=int(input("What do you want to sell ? : "))
        if x<=8:
            y1=int(input("How much would you want to sell ? : "))
            chs=input("Can we confirm your order ? (y/n)")
            if chs.lower()=='y':
                t.sleep(2)
                sellitem(x,y1)
            else:
                print("\nSee you again later")
        else:
            print("\nProvide a correct option")

    elif play.lower()=="work":
        choiceoP=int(input('''
              1)Get a Job /Change Job
              2)Work in current Job
        
               [1 / 2 ]
               
              :'''))
                     
        if choiceoP==1:
            apl=int(input('''

            1) Youtuber   [1]
               ===> Time per Shift   : 30s
               ===> Salary per Shift : ⏣ 17,000
               
            2) Teacher    [2]
               ===> Time per Shift   : 40s
               ===> Salary per Shift : ⏣ 20,000

            3) Programmer [3]
               ===> Time per Shift   : 55s
               ===> Salary per Shit  : ⏣ 32,000
               
            4) NBA Player [4]
               ===> Time per Shift   : 70s
               ===> Salary per Shift : ⏣ 50,000

                [ 1 / 2 / 3 / 4 ]

               :'''))
            if apl==1:
                work='Youtuber'
                salary=17000
                print("You are currently a Youtuber and your salary is ⏣ 17,000")
            elif apl==2:
                work='Teacher'
                salary=20000
                print("You are currently a Teacher and your salary is ⏣ 20,000")
            elif apl==3:
                work='Programmer'
                salary=32000
                print("You are currently a Programmer and your salary is ⏣ 32,000")
            elif apl==4:
                work='NBA Player'
                salary=50000
                print("You are currently a NBA Player and your salary is ⏣ 50,000")

        elif choiceoP==2:
            Work()
            
                    
    elif play.lower()=='quit':
        t.sleep(1)
        print("\n Final Balance ⏣",bal,"\n")
        print("\n Final Bank Balance ⏣",bank,"\n")
        
        print("\n Your final inventory \n")
        invshow()
        print("\n SEE YOU LATER  \n")
        pl=1

    else:print("Invalid command")
    
