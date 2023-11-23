'''18.A binary file FACTORY.dat has the detail of Factory id-fid,Factory name-fname and Production -
prod, Define search_id () to search and display the content in pickled file where fid is matching with
‘108’,and an appropriate msg if no records found.'''
import pickle
def add():
    n=int(input('Enter the no. of records:'))
    with open('FACTORY.dat','wb') as f:
        for k in range(n):
            fid=int(input('enter factory id:'))
            fname=input('enter name:')
            prod=int(input('Enter production:'))
            pickle.dump([fid,fname,prod],f)
def search_id():
    with open('FACTORY.dat','rb') as f1:
        try:
            while True:
                l=pickle.load(f1)
                if l[0] == 108:
                    print(l[0],l[1],l[2])
        except EOFError:
            pass
        except FileNotFoundError:
            print('the file is not found')
add()
search_id()
