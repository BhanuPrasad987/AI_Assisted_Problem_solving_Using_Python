#Function to find the largest number in a list
def find_largest_number(numbers):
    if not numbers:
        return None
    largest = numbers[0]
    for num in numbers[1:]:
        if num > largest:
            largest = num
    return largest
print(find_largest_number([10, 25, 7, 99, 42]))

#Review
#The function is easy to read and understand 
#The logic is well-structured using a simple loop
#Adding a docstring would improve documentation
#Returning None for an empty list, but we can also raise an error to make it more explict
#Efficient for small and large lists alike