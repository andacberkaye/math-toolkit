def addition(*args):
    """
    Returns the sum of all given numbers.

    Parameters:
    *args: list of numbers

    Returns:
    int or float: The sum of all numbers
    """
    addition = 0
    numbers = [i for i in args]
    for x in numbers:
        addition = addition + x
    return addition


def subtraction(*args):   
    """
    Returns the result of subtracting all following numbers from the first one.
    ! [rejected]        main -> main (fetch first)
    error: failed to push some refs to 'https://github.com/andacberkaye/math-toolkit.git'
    hint: Updates were rejected because the remote contains work that you do
    hint: not have locally. This is usually caused by another repository pushing
    hint: to the same ref. You may want to first integrate the remote changes
    hint: (e.g., 'git pull ...') before pushing again.
    hint: See the 'Note about fast-forwards' in 'git push --help' for details.
    (base) andacberkayekren@Andac-MacBook-Air math-toolkit % git -m  push
        Parameters:
        *args: list of numbers

    Returns:
    int or float: The result of subtraction
    """ 

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


def multiplication(*args):  
    """
    Returns the product of all given numbers.

    Parameters:
    *args: list of numbers

    Returns:
    int or float: The product of all numbers
    """

    multiplication = 1
    numbers = [i for i in args]
    for x in numbers:
        multiplication = multiplication * x
    return multiplication


def division(a = 1,b=1): 
    """
    Divides a by b.

    Parameters:
    a: dividend (int or float)
    b: divisor (int or float)

    Returns:
    float: Result of division or error message
    """

    if b == 0:
        return "Division by zero is not allowed."
    return a / b


def exponents(a = 1, b = 1):    
    """
    Raises a to the power of b.

    Parameters:
    a: base (int or float)
    b: exponent (int or float)

    Returns:
    int or float: Result of exponentiation
    """

    return a**b


def roots(a = 1):
    """
    Returns the square root of a.

    Parameters:
    a: number (int or float)

    Returns:
    float: Square root of a
    """

    return a ** 0.5


def factorial(a = 1):
    """
    Calculates the factorial of a non-negative integer a.

    Parameters:
    a: integer

    Returns:
    int: Factorial of a or error message
    """

    if a < 0:
        return "Factorial is undefined for negative numbers."
    conclusion = 1
    while a >= 1:
        conclusion = conclusion * a
        a -= 1
    return conclusion


def mean(*args):    
    """
    Calculates the mean (average) of the given numbers.

    Parameters:
    *args: list of numbers

    Returns:
    float: Mean value
    """

    mean = 0
    addition = 0
    numbers = [i for i in args]
    for x in numbers:
        addition = addition + x
    if len(numbers) == 0: mean = 0
    else: mean = addition / len(numbers)
    return mean


def mod(a = 1,b = 1):
    """
    Returns the remainder when a is divided by b.

    Parameters:
    a: dividend (int)
    b: divisor (int)

    Returns:
    int or str: Remainder or error message
    """
    
    if b == 0:  return "Division by zero is not allowed."
    else:   return a % b
    

def absolute_value(a = 0):
    """
    Returns the absolute value of a.

    Parameters:
    a: number (int or float)

    Returns:
    int or float: Absolute value of a
    """

    if a > 0:   return  a
    elif a < 0: return (-a)
    else:   return 0
    

def permutation(a = 1 , b = 1):
    """
    Calculates the number of permutations (P(a, b)).

    Returns:
    float or str: Number of permutations or error message
    """

    if a < 0 or b < 0:
        return "Permutation is undefined for negative numbers."
    if a < b:
        return "Permutation is undefined when a < b."
    return factorial(a) / factorial((a - b))


def combination(a = 1, b = 1):
    """
    Calculates the number of combinations (C(a, b)).

    Returns:
    float or str: Number of combinations or error message
    """

    if a < 0 or b < 0:
        return "Combination is undefined for negative numbers."
    if a < b:
        return "Combination is undefined when a < b."
    return factorial(a) / (factorial(b)*factorial((a-b)))


def even_odd(a = 0):    
    """
    Checks if a number is even or odd.

    Parameters:
    a (int): The number to check.

    Returns:
    str: "Number is zero", or a message stating whether the number is even or odd.
    """

    if a == 0: return "Number is zero"
    elif a % 2 == 0 and a != 0: return f"{a} number is even"
    else: return f"{a} number is odd"


def is_prime(a = 0):   
    """
    Checks if a number is a prime number.

    Parameters:
    a (int): The number to check.

    Returns:
    str: A message stating whether the number is prime or not.
    """

    if a < 2:
        return f"{a} is not prime"
    for i in range(2, a):
        if a % i == 0:
            return f"{a} isn't prime"
    return f"{a} is prime"


def perfect_number(a = 0):
    """
    Checks if a number is a perfect number.

    Parameters:
    a (int): The number to check.

    Returns:
    str: A message stating whether the number is perfect or not.
    """

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
    """
    Checks if a number is an Armstrong number.

    Parameters:
    a (int): The number to check.

    Returns:
    str: A message stating whether the number is Armstrong or not.
    """

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
    """
    Calculates the logarithm of x with the given base using binary search.

    Parameters:
    x (float): The number to calculate the log for.
    base (float): The base of the logarithm.

    Returns:
    float or str: The logarithm value or an error message.
    """

    if x <= 0 or base <= 0 or base == 1:
        return "Undefined value"

    low = 0.0
    high = max(1.0, x)  
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
    """
    Checks if three sides form a Pythagorean triangle.

    Parameters:
    a, b, c (float): The lengths of the sides of the triangle.

    Returns:
    str: Message stating whether the triangle is Pythagorean or not.
    """

    if a <= 0 or b <= 0 or c <= 0:
        return "Any side of a triangle must be greater than zero"
    if a > b and a > c:
        return "This is a Pythagorean triangle" if b**2 + c**2 == a**2 else "This isn't a Pythagorean triangle"
    elif b > a and b > c:
        return "This is a Pythagorean triangle" if a**2 + c**2 == b**2 else "This isn't a Pythagorean triangle"
    else:
        return "This is a Pythagorean triangle" if a**2 + b**2 == c**2 else "This isn't a Pythagorean triangle"


def hypotenuse(a = 1, b = 1):
    """
    Calculates the hypotenuse of a right triangle given the other two sides.

    Parameters:
    a, b (float): The lengths of the other two sides.

    Returns:
    float or str: The hypotenuse length or an error message.
    """

    if a == 0 or b == 0:
        return "Any side of a triangle must be greater than zero"
    return f"Hypotenuse: {(a**2 + b**2) ** 0.5}"


def digits_sum(a = 0):
    """
    Calculates the sum of digits of a number.

    Parameters:
    a (int): The number.

    Returns:
    int or str: Sum of digits or "None" if input is zero.
    """

    if a == 0:
        return "None"
    else:
        i = [x for x in str(a)]
        addition = 0
        for y in i:
            addition += int(y)
        return addition
    

def cascad(a = 0):
    """
    Returns the length of the number as a string with 'cascading' appended.

    Parameters:
    a (int): The number.

    Returns:
    str: Length of the number followed by ' cascading', or 'None' if zero.
    """

    if a == 0:
        return "None"
    return str(len(str(a))) + " cascading"


def hexadecimal(a = 0):
    """
    Converts a decimal number to its hexadecimal representation.

    Parameters:
    a (int): The decimal number.

    Returns:
    str: Hexadecimal string or 'None' if zero.
    """

    if a == 0:
        return "None"
    digits = "0123456789ABCDEF"
    result = ""
    while a > 0:
        result = digits[a % 16] + result
        a = a // 16
    return result


def octal(a = 0):
    """
    Converts a decimal number to its octal representation.

    Parameters:
    a (int): The decimal number.

    Returns:
    str: Octal string or 'None' if zero.
    """

    if a == 0:
        return "None"
    result = ""
    while a > 0:
        result = str(a % 8) + result
        a = a // 8
    return result


def binary(a = 0):
    """
    Converts a decimal number to its binary representation.

    Parameters:
    a (int): The decimal number.

    Returns:
    str: Binary string or 'None' if zero.
    """

    if a == 0:
        return "None"
    result = ""
    while a > 0:
        result = str(a % 2) + result
        a = a // 2
    return result


def reverse_number(a = 0):
    """
    Reverses the digits of a number.

    Parameters:
    a (int): The number.

    Returns:
    str: The reversed number as a string.
    """

    a = str(a)
    return a[::-1]


def gcd(a = 0, b = 0):
    """
    Calculates the greatest common divisor (GCD) of two numbers without using any external module.

    Parameters:
    a, b (int): The numbers.

    Returns:
    int or str: The GCD or 'None' if any input is zero.
    """

    if a == 0 or b == 0:
        return "None"
    i = 1
    ebob = 1

    while (i <= a and i <= b):
        if a % i == 0 and b % i == 0:
            ebob = i
        i += 1
    return ebob


def lcm(a = 0,b = 0):
    """
    Calculates the least common multiple (LCM) of two numbers without using any external module.

    Parameters:
    a, b (int): The numbers.

    Returns:
    int or str: The LCM or 'None' if any input is zero.
    """
    
    if a == 0 or b == 0:
        return "None"
    i = 2
    ekok = 1
    while True:
        if (a % i == 0 and b % i == 0):
            ekok *= i

            a //= i
            b //= i


        elif (a % i ==  0 and b % i != 0):
            ekok *= i

            a //= i


        elif (a % i != 0 and b % i == 0):
            ekok *= i

            b //= i
        else:
            i += 1
        if (a == 1 and b == 1):
            break
    return ekok