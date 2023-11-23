d={}
a=int(input('Enter the score for senior Shivaji:'))
b=int(input('Enter the score for senior Bharathi:'))
c=int(input('Enter the score for senior Tagore:'))
e=int(input('Enter the score for senior Pratap:'))
d['SENIORS']={'BHARATHI':b,'TAGORE':c,'SHIVAJI':a,'PRATAP':e}
a=int(input('Enter the score for junior Shivaji:'))
b=int(input('Enter the score for junior Bharathi:'))
c=int(input('Enter the score for junior Tagore:'))
e=int(input('Enter the score for junior Pratap:'))
d['JUNIORS']={'BHARATHI':b,'TAGORE':c,'SHIVAJI':a,'PRATAP':e}
a=int(input('Enter the score for sub-junior Shivaji:'))
b=int(input('Enter the score for sub-junior Bharathi:'))
c=int(input('Enter the score for sub-junior Tagore:'))
e=int(input('Enter the score for sub-junior Pratap:'))
d['SUBJUNIORS']={'BHARATHI':b,'TAGORE':c,'SHIVAJI':a,'PRATAP':e}
def MAX_SCORE(d):
    l=[]
    for i in d:
        c=0
        for j in d[i]:
          if d[i][j] > c:
              c=d[i][j]
              a=j
        l.append([a,c,i])
    for i in range(len(l)):
        print('Maximum score acquired by',l[i][0],'is',l[i][1],'in',l[i][2],'category')
MAX_SCORE(d)  
