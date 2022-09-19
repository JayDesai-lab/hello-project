x = 'global'
def f():
    
    x = 'enclosing'
    print (x)
    def g():
        x = 'local'
        print(x)
    g()
    print(x)  
print(x) 
f() 