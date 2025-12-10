# Task: Basic Docstring Generation

# Write a Python function that returns the sum of even and odd numbers in a given list.

""" Calculates the sum of even and odd numbers in a given list."""
def sum_even_odd(numbers):
    """Initialize variables to store sums of even and odd numbers"""
    even_sum = 0
    odd_sum = 0
    """Loop through each number in the given list"""
    for num in numbers:
        """Check if the number is even (divisible by 2)"""
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num
    """Return both sums as a tuple (even_sum, odd_sum)"""
    return even_sum, odd_sum   

"""Define a list of numbers to test the function"""
numbers = [1, 2, 3, 4, 5, 6]

"""Call the function and unpack the returned tuple into two variables"""
even_sum, odd_sum = sum_even_odd(numbers)
"""Print the list """
print(f"List: {numbers}")
"""Print the Sum of even numbers"""
print(f"Sum of even numbers: {even_sum}")
"""Print the Sum of odd numbers"""
print(f"Sum of odd numbers: {odd_sum}")


#Generate a docstring automatically for the same function.
def sum_even_odd_ai(numbers):
    """
    Calculate the sum of even and odd numbers in a list.

    Args:
        numbers (list): A list of integers.

    Returns:
        tuple: A tuple containing two integers - the sum of even numbers and the sum of odd numbers.

    Example:
        >>> sum_even_odd_ai([1, 2, 3, 4, 5, 6])
        (12, 9)
    """
    even_sum = 0
    odd_sum = 0
    for num in numbers:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num
    return even_sum, odd_sum

