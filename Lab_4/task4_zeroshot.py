#Write a Python function that counts the number of vowels in a string.
def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in input_string:
        if char in vowels:
            count += 1
    return count
#Example Usage:
print(count_vowels("Hello World"))  # Output: 3