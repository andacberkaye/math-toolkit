def Addition(*args):
    
    addition = 0
    
    numbers = [i for i in args]
     
    for x in numbers:
        addition = addition + x
    
    return addition

def Subtraction(*args):
    
    numbers = [i for i in args]
     
    if len(numbers) == 0:
        return 0
    else:
        subtraction = numbers[0]

    for x in numbers:
        if subtraction == x:
            continue
        else:
            subtraction = subtraction - x
    
    return subtraction

def Multiplication(*args):
    
    multiplication = 1
    
    numbers = [i for i in a]
     
    for x in numbers:
        multiplication = multiplication * x
    
    return multiplication

def Division(a = 1,b=1):
    
    if b == 0 or a == 0:
        return "Division by zero is not allowed."
    
    return a / b

def Exponents(a = 1, b = 1):
    
    return a**b

def Roots(a = 1):

    return a ** 0.5

def Factorial(a = 1):

    conclusion = 1

    while a >= 1:
        conclusion = conclusion * a
        a -= 1

    return conclusion

def Mean(*args):
    
    mean = 0
    addition = 0

    numbers = [i for i in args]
     
    for x in numbers:
        addition = addition + x

    if len(numbers) == 0: mean = 0
    else: mean = addition / len(numbers)

    return mean

def Mod(a = 1,b = 1):

    if b == 0:  return "Division by zero is not allowed."
    else:   return a // b
    