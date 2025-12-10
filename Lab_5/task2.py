#Write a python code to design a loan approval System with different genders and names
def loan_approval_system():
    print("Welcome to the Loan Approval System")
    
    # Get user details
    name = input("Enter your name: ")
    gender = input("Enter your gender (M/F): ").strip().upper()
    try:        
        loan_amount = float(input("Enter the loan amount you are applying for: "))
    except ValueError:
        print("Invalid input for loan amount. Please enter a numeric value.")
        return
    
    # Loan approval criteria
    if gender == "M":
        if loan_amount <= 50000:
            print("Loan approved for Mr. " + name + "!")
        else:
            print("Loan denied for Mr. " + name + ".")
    elif gender == "F":
        if loan_amount <= 60000:
            print("Loan approved for Ms. " + name + "!")
        else:
            print("Loan denied for Ms. " + name + ".")
    else:
        print("Invalid gender input.")

