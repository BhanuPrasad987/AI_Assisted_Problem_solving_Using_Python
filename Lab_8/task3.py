#Generate a Python solution for the following task:

#Task:
#Generate test cases using AI for is_sentence_palindrome(sentence). Ignore case, punctuation, and spaces.

#Requirements
#create test cases for is_sentence_palindrome(sentence)(ignores case, spaces, and punctuation).

#Expected Output:
#Function returns True/False for cleaned sentences
#Implement the function to pass AI-generated tests.
import re

def is_sentence_palindrome(sentence):
    """
    Checks if a given sentence is a palindrome,
    ignoring case, spaces, and punctuation.
    """
    # Clean the sentence: remove all non-alphanumeric characters and convert to lowercase
    cleaned = re.sub(r'[^A-Za-z0-9]', '', sentence).lower()
    # Check if cleaned string is palindrome
    return cleaned == cleaned[::-1]

