#Debug the following code
def divide(a, b):
    return a/b
print(divide(10, 0))  # This will raise a ZeroDivisionError
try:
    print(divide(10, 0))        
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")