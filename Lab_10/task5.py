#Improve error handling, naming, and readability of the below python script

'''Python Script
def div(a,b):
    return a/b
print(div(10,0))'''
def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
# Example usage:
result = div(10, 0)
print(result)  # Output: Error: Division by zero is not allowed.



