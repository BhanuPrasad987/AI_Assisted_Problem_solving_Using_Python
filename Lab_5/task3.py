#write a function to calculate the nth Fibonacci number using recursion and explain the code 
def fibonacci(n):
    # Base case: the first Fibonacci number is 0, and the second is 1
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Recursive case: the nth Fibonacci number is the sum of the (n-1)th and (n-2)th Fibonacci numbers
        return fibonacci(n - 1) + fibonacci(n - 2)
