def func():
    f1=open('covid.txt')
    f2=open('Edited.txt','w')
    a=f1.read()
    f2.write(a)
    print(a)
    l=f2.readlines()
    for i in range(len(l)):
        for j in i:
            if j=='covid':
                l[i][j]='covid'.upper()
    print(f2.read())
func()
'''covid-19 started in the year 2020
the most dangerous virus the world has ever seen was covid-19
covid-19 had many variants
the whole world was under lockdown due to covid-19
many peoples way of life had been changed due to covid-19'''