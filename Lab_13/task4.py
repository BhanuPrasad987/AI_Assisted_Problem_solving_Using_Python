#Refactor this Code to use list comprehensions for better readability and performance.
'''
nums = [1,2,3,4,5,6,7,8,9,10]
squares = []
for i in nums:
    squares.append(i * i)'''
nums = [1,2,3,4,5,6,7,8,9,10]
squares = [i * i for i in nums]
# Example usage:
print(squares)  # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
