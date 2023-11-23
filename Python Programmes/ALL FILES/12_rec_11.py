with open("textfile.txt",'w') as f:
    while True:
        x=input('Enter the line:')
        f.write(x+'\n')
        c=input("Do you want to continue (Y/N)?:")
        if c.lower()=='n':
            break

print('''
================================MENU================================
1.Display number of lines
2.Copy the words containing 'U' into another file and display new file
3.Convert case of letters in orginal text file and display contents
4.Exit''')

while True:
        c=int(input("Enter the Menu Code: "))
        if 1< c >4:
            print("Invalid Menu Code")
        elif c==1:
            with open("textfile.txt",'r+') as f:
                print(len(f.readlines()))
        elif c==2:
            with open("textfile.txt",'r') as f:
                with open('copyfile.txt','w') as f1:
                    a=f.readlines()
                    for i in a:
                        b=i.split()
                        for j in b:
                            if 'u' in j.lower():
                                f1.write(j+'\n')
            with open('copyfile.txt','r+') as f:
                for i in f.read().split():
                    print(i)
        elif c==3:
            with open("textfile.txt",'r') as f:
                a=f.read()
            with open("textfile.txt",'w') as f:
                for i in a:
                    if i.isupper():
                        f.write(i.lower())
                    elif i.islower():
                        f.write(i.upper())
                    else:
                        f.write(i)
            with open("textfile.txt",'r') as f:
                print(f.read())
        elif c==4:
            print('The Program is Ended')
            break
                
                

            
                
                
            
            
            
