import math

class Calculator:
    def add(self, a, b):
        # Adds two numbers
        return a + b

    def subtract(self, a, b):
        # Subtracts the second number from the first
        return a - b

    def multiply(self, a, b):
        # Multiplies two numbers
        return a * b

    def divide(self, a, b):
        # Divides the first number by the second
        # Raises a ValueError if the second number is zero
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def square_root(self, a):
        # Returns the square root of a number
        # Raises a ValueError if the number is negative
        if a < 0:
            raise ValueError("Cannot calculate the square root of a negative number")
        return math.sqrt(a)

    def power(self, a, b):
        # Returns the first number raised to the power of the second number
        return a ** b

    def logarithm(self, a, base=math.e):
        # Returns the logarithm of a number with the specified base
        # Raises a ValueError if the number is non-positive
        if a <= 0:
            raise ValueError("Logarithm undefined for non-positive values")
        return math.log(a, base)

    def factorial(self, a):
        # Returns the factorial of a number
        # Raises a ValueError if the number is negative
        if a < 0:
            raise ValueError("Factorial undefined for negative values")
        return math.factorial(a)