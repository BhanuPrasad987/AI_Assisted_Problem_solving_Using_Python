def greet_user(name, gender):
    if gender.lower() == "male":
        title = "Mr."
    else:
        title = "Mrs."
    return f"Hello, {title} {name}! Welcome."

#Regenerate code that includes gender-neutral also
def greet_user_neutral(name, gender):
    if gender.lower() == "male":
        title = "Mr."
    elif gender.lower() == "female":
        title = "Ms."
    else:
        title = "Mx."
    return f"Hello, {title} {name}! Welcome."

# Example usage
print(greet_user_neutral("John Doe", "male"))
