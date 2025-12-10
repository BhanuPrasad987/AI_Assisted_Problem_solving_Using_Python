# Write a Python function to calculate the sum of squares of numbers in a list
def sum_of_squares(numbers):

    return sum(x**2 for x in numbers)

# Test the function
print(sum_of_squares([1, 2, 3, 4, 5]))

