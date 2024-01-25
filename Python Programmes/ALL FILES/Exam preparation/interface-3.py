import mysql.connector as mc
cn=mc.connect(host='localhost',password='harivin',username='root')
cr=cn.cursor()
cr.execute('Create database if not exists record')
cr.execute('Use record')
cr.execute("Create table if not exists Employee(Empno integer Primary Key,\
Name varchar(30), Desig varchar(30), Deptno integer, Salary integer)")
cr.execute("Create table if not exists Department(Deptno integer, Dname varchar(30), Location varchar(60))")
cr.execute('Select * from Employee')
res=cr.fetchall()
if cr.rowcount==0:
    cr.execute("Insert into employee values(1,'Ram','Admin',100,50000)")
    cr.execute("Insert into employee values(2,'Manoj','Manager',101,60000)")
    cr.execute("Insert into employee values(3,'Seetha','Manager',102,45000)")
    cr.execute("Insert into employee values(4,'Hari','Financier',101,56000)")
    cr.execute("Insert into employee values(5,'Sriman','Admin',100,57000)")
    cn.commit()
cr.execute('Select * from Department')
res=cr.fetchall()
if cr.rowcount==0:
    cr.execute("Insert into Department values(100,'IT','Block A')")
    cr.execute("Insert into Department values(101,'Think Tank','Block A')")
    cr.execute("Insert into Department values(102,'Sales','Block C')")
    cr.execute("Insert into Department values(103,'HR','Block B')")
    cn.commit()
cr.execute('Select * from employee e,Department t where e.deptno=t.deptno')
res=cr.fetchall()
print('Joined tables')
for i in res:
    for j in i:
        print(j,end=' ')
    print()
print()
print()
cr.execute("Select Empno,Name, Salary, Dname, Location from employee e,Department t where e.deptno=t.deptno and desig='Manager'")
res=cr.fetchall()
print('Details of all managers')
for i in res:
    for j in i:
        print(j,end=' ')
    print()
cn.close()
