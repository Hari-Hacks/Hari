def ShowP():
    with open('IONS.txt','w') as f:
        l=['Whether an atom will form a cation or an anion is based on its','position in the periodic table is not a presumption']
        for i in l:
            f.write(i+'\n')
    with open('IONS.txt','r') as f:
        l=f.readlines()
        for i in l:
            for j in i.split():
                if (j.lower().startswith('p')) and (j.lower().endswith('ion')):
                    print(j)
                else:
                    continue  
ShowP()