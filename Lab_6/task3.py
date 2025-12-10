#Write a Python program using nested if-elif-else statements to classify a person's age group, 
# then modify it using another conditional structure and provide explanation 
def classify_age_group(age):
    if age < 0:
        return "Invalid age"
    elif age <= 12:
        return "Child"
    elif age <= 19:
        return "Teenager"
    elif age <= 64:
        return "Adult"
    else:
        return "Senior"
# Using nested if-elif-else statements
age = 25
age_group = classify_age_group(age)
print(f"Age: {age}, Age Group: {age_group}")

# Modified version using match-case (Python 3.10+)
def classify_age_group_match_case(age):
    match age:
        case _ if age < 0:
            return "Invalid age"
        case _ if age <= 12:
            return "Child"
        case _ if age <= 19:
            return "Teenager"
        case _ if age <= 64:
            return "Adult"
        case _:
            return "Senior"
age_group_match_case = classify_age_group_match_case(age)
print(f"Age: {age}, Age Group (match-case): {age_group_match_case}")

