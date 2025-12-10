#Count the number of vowels (a, e, i, o, u) in a given string using Python.
#The function should return the total number of vowels.
#Examples:
#"hello" → 2
#"apple" → 2
#"Python" → 1
#Write a clean and efficient Python function for the above task.
def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in input_string:
        if char in vowels:
            count += 1
    return count
#Example Usage:
print(count_vowels("hello"))  # Output: 2
print(count_vowels("apple"))  # Output: 2
print(count_vowels("Python"))  # Output: 1