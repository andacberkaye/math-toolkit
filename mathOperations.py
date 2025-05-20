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
    numbers = [i for i in args]
    for x in numbers:
        multiplication = multiplication * x
    return multiplication


def Division(a = 1,b=1):    
    if b == 0:
        return "Division by zero is not allowed."
    return a / b


def Exponents(a = 1, b = 1):    
    return a**b


def Roots(a = 1):
    return a ** 0.5


def Factorial(a = 1):
    if a < 0:
        return "Factorial is undefined for negative numbers."
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
    else:   return a % b
    

def absolute_value(a = 0):
    if a > 0:   return  a
    elif a < 0: return (-a)
    else:   return 0
    

def Permutation(a = 1 , b = 1):
    if a < 0 or b < 0:
        return "Permutation is undefined for negative numbers."
    if a < b:
        return "Permutation is undefined when a < b."
    return Factorial(a) / Factorial((a - b))


def Combination(a = 1, b = 1):
    if a < 0 or b < 0:
        return "Combination is undefined for negative numbers."
    if a < b:
        return "Combination is undefined when a < b."
    return Factorial(a) / (Factorial(b)*Factorial((a-b)))


def even_odd(a = 0):
    if a == 0: return "Number is zero"
    elif a % 2 == 0 and a != 0: return f"{a} number is even"
    else: return f"{a} number is odd"


def is_prime(a = 0):    
    if a < 2:
        return f"{a} is not prime"
    for i in range(2, a):
        if a % i == 0:
            return f"{a} isn't prime"
    return f"{a} is prime"


def perfect_number(a = 0):
    addition = 0
    for x in range(1,a):
        if a % x == 0:
            addition += x
        else:
            continue
    if addition == a:
        return f"{a} is perfect number"
    else:
        return f"{a} isn't perfect number"
    

def armstrong_number(a):
    if a < 0:
        return "Enter a positive number"
    digits = len(str(a))
    numbers = [int(x) for x in str(a)]
    addition = sum([r**digits for r in numbers])
    if addition == a:
        return f"The number ({a}) you entered is an Armstrong number"
    else:
        return f"The number ({a}) you entered is not an Armstrong number"
    

def log_base(x = 1, base = 1):
    if x <= 0 or base <= 0 or base == 1:
        return "Undefined value"

    low = 0.0
    high = max(1.0, x)  # burada düzeltme
    epsilon = 0.00001
    guess = (low + high) / 2

    while True:
        current = base ** guess
        difference = current - x

        if difference < 0:
            difference = -difference

        if difference < epsilon:
            return guess
        elif current > x:
            high = guess
        else:
            low = guess                 

        guess = (low + high) / 2


def pythagoras_three(a = 1, b =1, c = 1):
    if a <= 0 or b <= 0 or c <= 0:
        return "Any side of a triangle must be greater than zero"
    if a > b and a > c:
        return "This is a Pythagorean triangle" if b**2 + c**2 == a**2 else "This isn't a Pythagorean triangle"
    elif b > a and b > c:
        return "This is a Pythagorean triangle" if a**2 + c**2 == b**2 else "This isn't a Pythagorean triangle"
    else:
        return "This is a Pythagorean triangle" if a**2 + b**2 == c**2 else "This isn't a Pythagorean triangle"


def Hypotenuse(a = 1, b = 1):
    if a == 0 or b == 0:
        return "Any side of a triangle must be greater than zero"
    return f"Hypotenuse: {(a**2 + b**2) ** 0.5}"


def digits_sum(a = 0):
    if a == 0:
        return "None"
    else:
        i = [x for x in str(a)]
        addition = 0
        for y in i:
            addition += int(y)
        return addition
    

def Cascad(a = 0):
    if a == 0:
        return "None"
    return str(len(str(a))) + " cascading"


def Hexadecimal(a = 0):
    if a == 0:
        return "None"
    digits = "0123456789ABCDEF"
    result = ""
    while a > 0:
        result = digits[a % 16] + result
        a = a // 16
    return result


def Octal(a = 0):
    if a == 0:
        return "None"
    result = ""
    while a > 0:
        result = str(a % 8) + result
        a = a // 8
    return result


def Binary(a = 0):
    if a == 0:
        return "None"
    result = ""
    while a > 0:
        result = str(a % 2) + result
        a = a // 2
    return result