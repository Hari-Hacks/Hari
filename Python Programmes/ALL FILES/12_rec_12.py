n=int(input("Enter number of lines : "))
with open("textfile.txt",'w') as f:
    for i in range(n):
        i=input("Enter the line:")
        f.write(i+'\n')

print('''
=======================MENU======================
1.Count the number of words
2.Display Palindrome Words
3. Display words starting and ending with a vowel
4.Exit''')
while True:
    c=int(input("Enter Menu Code: "))
    if 1< c >4:
        print("Invalid Menu Code")
    elif c==1:
        with open("textfile.txt",'r') as f:
            k=0
            for i in f.readlines():
                for j in i.split():
                    k+=1
            print(k)
    elif c==2:
        with open("textfile.txt",'r') as f:
            for i in f.readlines():
                for j in i.split():
                    if j.lower()==j[::-1].lower():
                        print(j)
    elif c==3:
        with open("textfile.txt",'r') as f:
            for i in f.readlines():
                for j in i.split():
                    if j[0].lower() in 'aeiou' and j[-1].lower() in 'aeiou':
                        print(j)
    elif c==4:
        print('The Program is Ended')
        break
        
                    
                
