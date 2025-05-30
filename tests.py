from mathOperations import *

def run_tests():
    print("Running tests...")

    assert addition(1, 2, 3) == 6, "Addition failed"
    assert subtraction(10, 3, 2) == 5, "Subtraction failed"
    assert multiplication(2, 3, 4) == 24, "Multiplication failed"
    assert division(10, 2) == 5, "Division failed"
    assert division(10, 0) == "Division by zero is not allowed.", "Division by zero failed"
    assert exponents(2, 3) == 8, "Exponents failed"
    assert roots(25) == 5, "Roots failed"
    assert factorial(5) == 120, "Factorial failed"
    assert mean(2, 4, 6) == 4, "Mean failed"
    assert mod(10, 3) == 1, "Mod failed"
    assert absolute_value(-5) == 5, "Absolute value failed"
    assert permutation(5, 2) == 20.0, "Permutation failed"
    assert combination(5, 2) == 10.0, "Combination failed"
    assert even_odd(4) == "4 number is even", "Even check failed"
    assert is_prime(7) == "7 is prime", "Prime check failed"
    assert perfect_number(28) == "28 is perfect number", "Perfect number failed"
    assert armstrong_number(153) == "The number (153) you entered is an Armstrong number", "Armstrong check failed"
    assert pythagoras_three(5, 3, 4) == "This is a Pythagorean triangle", "Pythagoras check failed"
    assert hypotenuse(3, 4) == "Hypotenuse: 5.0", "Hypotenuse failed"
    assert digits_sum(123) == 6, "Digits sum failed"
    assert cascad(123) == "3 cascading", "Cascad failed"
    assert hexadecimal(255) == "FF", "Hexadecimal failed"
    assert octal(10) == "12", "Octal failed"
    assert binary(5) == "101", "Binary failed"
    assert reverse_number(1234) == "4321", "Reverse number failed"
    assert ebob(12, 18) == 6, "EBOB failed"
    assert ekok(4, 6) == 12, "EKOK failed"

    print("✅ All tests passed successfully!")

if __name__ == "__main__":
    run_tests()
