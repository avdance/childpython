def add(a,b):
    return a+b

def loop():
    for i in range(3) :
        for a in range(0, i+1) :
            print('*', end ="")
        print('')

# c=add(3,3)
# print(c)
loop()