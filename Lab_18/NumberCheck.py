#Translate the method present in number.java into a Python function check_number(num).
def check_number(num):
    if num > 0:
        print(f"{num} is a positive number.")
    elif num < 0:
        print(f"{num} is a negative number.")
    else:
        print(f"{num} number is zero.")
# Example usage
check_number(5)
check_number(-7)
check_number(0) 
