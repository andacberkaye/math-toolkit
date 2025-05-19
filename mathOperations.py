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