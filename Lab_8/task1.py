#Generate a Python solution for the following task:

#Task:
#Generate test cases for the function is_valid_email(email) and then implement the validator function.

#Requirements:
#1. The email must contain both '@' and '.' characters.
#2. The email must not start or end with special characters (like '.', '-', '_', or '@').
#3. The email should not allow multiple '@' characters.
#4. Write a set of at least 10 test cases (both valid and invalid).
#5. Implement the is_valid_email(email) function to validate according to the above rules.
#6. Print the result of each test case clearly in the format:
   #Email: <email> → Valid / Invalid

#Expected Output:
#Email validation logic should pass all test cases.
import re

def is_valid_email(email):
    # Rule 1: Must contain both '@' and '.'
    if '@' not in email or '.' not in email:
        return False

    # Rule 2: Should not start or end with special characters
    if email[0] in ['.', '-', '_', '@'] or email[-1] in ['.', '-', '_', '@']:
        return False

    # Rule 3: Should not have multiple '@' characters
    if email.count('@') != 1:
        return False

    # Additional sanity check: basic structure before and after '@'
    username, domain = email.split('@')
    if not username or not domain:
        return False

    # Domain must contain at least one '.' after '@'
    if '.' not in domain:
        return False

    # No consecutive special characters
    if re.search(r'[.\-_@]{2,}', email):
        return False

    return True

