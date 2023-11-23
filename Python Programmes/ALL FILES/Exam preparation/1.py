d={'name':'vinay','age':23,1:100,34:500}
x=d.pop('age')
print(d)
print("the deleted age is",x)
y=d.popitem()
print(d)
print("popitem deleted the last key and value of the dict",y)
print("returns an empty dict",d.clear())