#•	Write a Python function factorial(n) that calculates factorial of a number using recursion.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
# Example usage
print(factorial(5))  # Output: 120
print(factorial(0))  # Output: 1
