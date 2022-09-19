x = 'global'
def f():
    global x
    x = 'enclosing'
    print (x)
    def g():
        x = 'local'
        print(x)
    g()
    print(x)  
print(x) 
f() 