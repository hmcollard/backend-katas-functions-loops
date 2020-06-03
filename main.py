
#!/usr/bin/env python
"""Implements math functions without using operators,
except for '+' and '-'.
"""

__author__ = "Haley Collard"


def add(x, y):
    """Add two integers."""
    return x + y


def multiply(x, y):
    """Multiply x with y using the add() function above."""
    total = 0
    for i in range(x):
        total = add(y, total)
    return total


def power(x, n):
    """Raise x to power n, where n >= 0, using the functions above."""
    total = x
    if n >= 0:
        for i in range(n-1):
            total = multiply(x, total)
    return total


def factorial(x):
    """Compute the factorial of x, where x > 0, using the functions above."""
    if x > 0:
        total = 1
        for i in range(x-1):
            total = multiply(total, i+2)
    return total


def fibonacci(n):
    """Compute the nth term of fibonacci sequence using the functions above."""
    result1 = 0
    result2 = 1
    for i in range(n):
        result3 = add(result1, result2)
        result2 = result1
        result1 = result3
    return result3


# if __name__ == '__main__':
print(add(2, 4))
print(multiply(6, -8))
print(power(2, 8))
print(factorial(4))
print(fibonacci(8))
