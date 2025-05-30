# Math Toolkit

A comprehensive Python library offering a wide range of fundamental mathematical functions implemented from scratch without relying on external modules. This toolkit aims to provide clear, efficient, and well-documented solutions for common mathematical operations, ideal for educational purposes and lightweight computational tasks.

---

## Features

- Basic arithmetic operations: addition, subtraction, multiplication, division  
- Advanced functions: factorial, permutations, combinations, exponents, roots  
- Number theory utilities: prime checking, perfect numbers, GCD (Ebob), LCM (Ekok)  
- Number system conversions: binary, octal, hexadecimal  
- Special number checks: Armstrong number, even/odd classification, perfect numbers  
- Additional utilities: digit sums, reverse numbers, logarithm calculations (custom implementation), Pythagorean checks  

---

## Function List

### Arithmetic
- `addition(*args)`
- `subtraction(*args)`
- `multiplication(*args)`
- `division(a, b)`
- `mod(a, b)`
- `absolute_value(a)`

### Powers & Roots
- `exponents(a, b)`
- `roots(a)`
- `log_base(x, base)`

### Statistical
- `mean(*args)`

### Factorials, Permutations, Combinations
- `factorial(a)`
- `permutation(a, b)`
- `combination(a, b)`

### Number Theory
- `even_odd(a)`
- `is_prime(a)`
- `perfect_number(a)`
- `armstrong_number(a)`
- `gcd(a, b)` (GCD)
- `lcm(a, b)` (LCM)

### Number Utilities
- `digits_sum(a)`
- `reverse_number(a)`
- `cascad(a)` — digit count string

### Conversions
- `binary(a)`
- `octal(a)`
- `hexadecimal(a)`

### Geometry
- `pythagoras_three(a, b, c)`
- `hypotenuse(a, b)`

---

## Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/andacberkaye/math-toolkit.git
```

No external dependencies required — pure Python.

---

## Usage

Import the module and call desired functions:

```python
from math_toolkit import Addition, Factorial, is_prime

print(addition(1, 2, 3))         # Output: 6
print(factorial(5))              # Output: 120
print(is_prime(17))              # Output: 17 is prime
```

---

## ✅ How to Run Tests

This project includes a lightweight `tests.py` file to validate core functionality of all implemented mathematical functions — without relying on any external libraries.

### Steps

1. Make sure you're in the root folder of the project.
2. Run the test file using:

```bash
python tests.py
```

If everything works correctly, you will see:

```
Running tests...
✅ All tests passed successfully!
```

If any function fails, a clear error message will be shown to help you debug the problem.

---


## Contribution

Contributions are welcome!  
Feel free to open issues or submit pull requests to improve functionality, add new features, or fix bugs.

---

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## Contact

Created by Andaç Berkaye  
GitHub: [andacberkaye](https://github.com/andacberkaye)
