
# Function to check if a string is a palindrome
def is_palindrome(s):
    # Remove spaces and convert to lowercase
    cleaned = ''.join(s.split()).lower()
    # Check if the cleaned string is equal to its reverse
    return cleaned == cleaned[::-1]
