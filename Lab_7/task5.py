numbers = [1, 2, 3]
print(numbers[5])  # This will raise an IndexError
try:
    print(numbers[5])
except IndexError:
    print("Error: Index out of range.")
