import mysql.connector as mc
cn=mc.connect(host='sql.freedb.tech',user='freedb_iehwf',password='NdVBt%!EkGepQ@4',database='freedb_XII Project')
cr=cn.cursor()
cr.execute('Alter table Credentials modify Password1 varchar(600)')
cr.execute('Alter table Credentials modify Password2 varchar(600)')
cr.execute('Alter table Credentials modify Password3 varchar(600)')
cr.execute('Alter table Credentials modify Password4 varchar(600)')
cr.execute('Alter table Credentials modify Password5 varchar(600)')
