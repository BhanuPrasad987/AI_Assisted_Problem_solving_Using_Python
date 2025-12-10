#Write a Python function that performs this formatting.
#Examples:
#“Sucharitha Kondaparthi” → “Kondaparthi, Sucharitha”
#“Anusha Kurla” → “kurla, Anusha”
#“Likitha Joshi” → “Joshi, Likitha”
def format_name(full_name):
    names = full_name.split()
    if len(names) != 2:
        return "Invalid input"
    first_name, last_name = names
    formatted_name = f"{last_name}, {first_name}"
    return formatted_name
