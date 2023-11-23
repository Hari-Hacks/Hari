STR="bees buzz"
while True:
    if STR[-1] =='z':
        STR = STR[0 :3] +'c'
    elif 'e' in STR:
         STR = STR[0] + 'bb'
    elif not STR.isalpha():
        STR = 'L' + STR[ 1 : ] + 'z'
    else:
        STR = STR + '*'
    if len(STR) >5:
        break
print("new string", STR)
