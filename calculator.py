"""
Calculator Module
A simple calculator application for demonstrating continuous testing pipeline.
"""


class Calculator:
    """A simple calculator class with basic arithmetic operations."""

    @staticmethod
    def add(a, b):
        """
        Add two numbers.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            Sum of a and b
        """
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Operands must be numbers")
        return a + b

    @staticmethod
    def subtract(a, b):
        """
        Subtract two numbers.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            Difference of a and b
        """
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Operands must be numbers")
        return a - b

    @staticmethod
    def multiply(a, b):
        """
        Multiply two numbers.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            Product of a and b
        """
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Operands must be numbers")
        return a * b

    @staticmethod
    def divide(a, b):
        """
        Divide two numbers.
        
        Args:
            a: Dividend (first number)
            b: Divisor (second number)
            
        Returns:
            Quotient of a divided by b
            
        Raises:
            ValueError: If b is zero
            TypeError: If operands are not numbers
        """
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Operands must be numbers")
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        return a / b

    @staticmethod
    def power(base, exponent):
        """
        Calculate base raised to the power of exponent.
        
        Args:
            base: Base number
            exponent: Exponent
            
        Returns:
            Result of base ** exponent
        """
        if not isinstance(base, (int, float)) or not isinstance(exponent, (int, float)):
            raise TypeError("Operands must be numbers")
        return base ** exponent

    @staticmethod
    def square_root(num):
        """
        Calculate the square root of a number.
        
        Args:
            num: Number to find square root of
            
        Returns:
            Square root of num
            
        Raises:
            ValueError: If num is negative
            TypeError: If num is not a number
        """
        if not isinstance(num, (int, float)):
            raise TypeError("Operand must be a number")
        if num < 0:
            raise ValueError("Cannot calculate square root of negative number")
        return num ** 0.5
