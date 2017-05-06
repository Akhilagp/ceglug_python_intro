def add(p,q):
    return p+q
    
def subtract(p,q):
    return p-q

def multiply (p,q):
    return p*q

def divide (p,q):
    return float(p)/float(q)
a = input("num1:")
b = input("num2:")
print '\n'
print add (a,b)
print subtract (a,b)
print multiply (a,b)
print float(divide (a,b))
