def task (x, y, z):
    if z == "+" :
        return (x + y)
    elif z == "-":
        return (x - y)
    elif z == "*":
        return (x * y)
    elif z == "/":
        return (x / y)
    else :
        return ("Неизвестная операция")
print (task(231, 231, '+'))
print (task(2, 2, '*'))
print (task(5554, 31, '-'))
print (task(231, 2, '/'))
print (task(4, 2, 0)) 
