#Programme no.14_Pg141
act_wtg=30.0
spt_wtg=20.0
xam_wtg=50.0
Xam_total=200.0
Act_total=60.0
Spt_total=50.0
xam_scr1=int(input('Enter the marks in first examination (out of 100):'))
xam_scr2=int(input('Enter the marks in second examination (out of 100):'))
spt_scr=int(input('Enter the score obtained in sports activities (out of 50):'))
act_scr1=int(input('Enter the marks in first activity (out of 20):'))
act_scr2=int(input('Enter the marks in second activity (out of 20):'))
act_scr3=int(input('Enter the marks in third activity (out of 20):'))
xam_total=xam_scr1+xam_scr2
act_total=act_scr1+act_scr2+act_scr3
xam_percent=float(xam_total*xam_wtg/Xam_total)
spt_percent=float(spt_scr*spt_wtg/Spt_total)
act_percent=float(act_total*act_wtg/Act_total)
total_percent=xam_percent+spt_percent+act_percent
print('\n\n*************************************RESULT*************************************')
print('\nTotal percent in Examination:',xam_percent)
print('\nTotal percent in activities:',act_percent)
print('\nTotal percent in sports:',spt_percent)
print('\n------------------------------------------')
print('\nTotal percentage:',total_percent)


