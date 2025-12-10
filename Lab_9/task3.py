"""
This module defines basic calculator operations such as addition, subtraction,multiplication, and division. It demonstrates how to use NumPy-style docstrings for documenting Python functions. The goal is to compare manually written 
docstrings with AI-generated ones for clarity and precision.
"""
# --- Manual Docstrings (NumPy Style) ---
def add(a, b):
    """
    Add two numbers.
    Parameters
    ----------
    a : int or float
        The first number.
    b : int or float
        The second number.
    Returns
    -------
    float
        The sum of `a` and `b`.
    """
    return a + b
def subtract(a, b):
    """
    Subtract one number from another.

    Parameters
    ----------
    a : int or float
        The number to subtract from.
    b : int or float
        The number to be subtracted.
    Returns
    -------
    float
        The result of `a - b`.
    """
    return a - b
def multiply(a, b):
    """
    Multiply two numbers.
    Parameters
    ----------
    a : int or float
        The first number.
    b : int or float
        The second number.
    Returns
    -------
    float
        The product of `a` and `b`.
    """
    return a * b
def divide(a, b):
    """
    Divide one number by another.
    Parameters
    ----------
    a : int or float
        The numerator.
    b : int or float
        The denominator.
    Returns
    -------
    float
        The result of `a / b`.
    Raises
    ------
    ValueError
        If `b` is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


# Generate a module-level docstring + individual function docstrings for the above code.

"""
AI-Generated Module Docstring
=============================
This module provides simple arithmetic operations including addition,
subtraction, multiplication, and division functions.
Each function takes two numbers as inputs and returns the computed result.
"""


def add_ai(a, b):
    """
    Returns the sum of two numbers.

    Parameters
    ----------
    a : float
        First value.
    b : float
        Second value.

    Returns
    -------
    float
        Sum of both values.
    """
    return a + b


def subtract_ai(a, b):
    """
    Returns the difference between two numbers.

    Parameters
    ----------
    a : float
        Minuend.
    b : float
        Subtrahend.

    Returns
    -------
    float
        Difference of the numbers.
    """
    return a - b
def multiply_ai(a, b):
    """
    Returns the product of two numbers.

    Parameters
    ----------
    a : float
        First multiplier.
    b : float
        Second multiplier.

    Returns
    -------
    float
        Product of the numbers.
    """
    return a * b


def divide_ai(a, b):
    """
    Returns the result of division.
    Parameters
    ----------
    a : float
        Numerator.
    b : float
        Denominator.
    Returns
    -------
    float
        Division result.
    Raises
    ------
    ZeroDivisionError
        If the denominator is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return a / b
# --- Testing the functions ---
if __name__ == "__main__":
    x, y = 10, 5
    print("Manual Functions:")
    print(f"Add: {add(x, y)}")
    print(f"Subtract: {subtract(x, y)}")
    print(f"Multiply: {multiply(x, y)}")
    print(f"Divide: {divide(x, y)}")
    print("\nAI-Generated Functions:")
    print(f"Add: {add_ai(x, y)}")
    print(f"Subtract: {subtract_ai(x, y)}")
    print(f"Multiply: {multiply_ai(x, y)}")
    print(f"Divide: {divide_ai(x, y)}")
