#Recursive function to find factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

#Iterative function to find factorial of a number
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

#Example Usage
print(factorial(5))
print(factorial_iterative(5))