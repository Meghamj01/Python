a = [1,2,3]
def f1():
    global a
    a =100
    print(a)
    
def f2():
    global a
    a =500
    print(a)

f1()
f2()
print(a)
