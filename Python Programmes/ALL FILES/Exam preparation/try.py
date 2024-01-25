def find():
    with open('country.txt','w') as f:
        l=['Whose woods these are I think I know.','His house is in the village though;','He will not see me stopping here','To watch his woods fill up with snow.']
        for i in l:
            f.write(i+'\n')
    with open('country.txt','r') as f:
        l=f.readlines()
        cw=ch=0
        for i in l:
            if i[0][0].lower()=='w':
                cw+=1
            elif i[0][0].lower()=='h':
                ch+=1
            else: continue
        print('W or w:',cw)
        print('H or h:',ch)
find()


