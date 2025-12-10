# Write a Python program that creates a scoring system for job applicants based on features                                 
def job_applicant_scoring_system():
    print("Welcome to the Job Applicant Scoring System")
    
    # Get applicant details
    try:
        experience = int(input("Enter years of experience: "))
    except ValueError:
        print("Invalid input for experience. Please enter a numeric value.")
        return
    
    education = input("Enter highest education level (High School/Bachelor/Master/PhD): ").strip().lower()
    skills = input("Enter number of relevant skills you possess: ")
    
    try:
        skills = int(skills)
    except ValueError:
        print("Invalid input for skills. Please enter a numeric value.")
        return
    
    # Initialize score
    score = 0
    
    # Scoring based on experience
    if experience >= 5:
        score += 40
    elif experience >= 3:
        score += 25
    elif experience >= 1:
        score += 10
    
    # Scoring based on education
    if education == "phd":
        score += 30
    elif education == "master":
        score += 20
    elif education == "bachelor":
        score += 10
    elif education == "high school":
        score += 5
    
    # Scoring based on skills
    score += min(skills * 5, 25)  # Max 25 points for skills
    
    # Display final score and evaluation
    print(f"Your total score is: {score}")
    
    if score >= 70:
        print("Congratulations! You are a strong candidate for the job.")
    elif score >= 40:
        print("You have potential, but there is room for improvement.")
    else:
        print("Unfortunately, you may not be a suitable candidate for this position.")