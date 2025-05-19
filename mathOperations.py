def Addition(*a):
    
    addition = 0
    
    numbers = [i for i in a]
     
    for x in numbers:
        addition = addition + x
    
    return addition

def Subtraction(*a):
    
    numbers = [i for i in a]
     
    subtraction = numbers[0]

    for x in numbers:
        if subtraction == x:
            continue
        else:
            subtraction = subtraction - x
    
    return subtraction

def Multiplication(*a):
    
    multiplication = 1
    
    numbers = [i for i in a]
     
    for x in numbers:
        multiplication = multiplication * x
    
    return multiplication

def Division(a,b=1):
    if b == 0:
        return "Division by zero is not allowed."
    return a / b