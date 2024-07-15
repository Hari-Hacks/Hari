def displaywords(t):
    b='aeiou'
    for i in t:
        if all(x in i for x in b):
            print(i)
        else:
            continue
