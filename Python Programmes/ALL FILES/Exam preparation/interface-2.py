import mysql.connector as mc
import csv
f=open('Student.csv','w',newline='')
wr=csv.writer(f)
cn=mc.connect(host='localhost',password='harivin',username='root')
cr=cn.cursor()
cr.execute('Create database if not exists record')
cr.execute('Use record')
cr.execute("Create table if not exists STUDENT(ROLL integer Primary Key,\
NAME varchar(30), TOTAL integer, COURSE varchar(20) CHECK(COURSE in\
('CS', 'BIOLOGY', 'COMMERCE', 'EG')), DOB DATE)")
cr.execute('Select * from student')
res=cr.fetchall()
for i in res:
    wr.writerow(i)
f.close()
print('Details of all students')
f=open('Student.csv','r')
rr=csv.reader(f)
for i in rr:
    print(i[0],i[1],i[2],i[3],i[4],sep=',')
marks=[]
f.close()
f=open('Student.csv','r')
rr=csv.reader(f)
print('Top scorer name')
for i in range(len(res)):
    marks.append(res[i][2])
maxm=max(marks)
for i in rr:
    if int(i[2])==maxm:
        print(i[1])
f.close()
cn.close()
