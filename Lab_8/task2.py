#Generate a Python solution for the following task:

#Task:
#Generate test cases for assign_grade(score) function. Handle boundary and invalid inputs.

#Requirements
#Generate test cases for assign_grade(score) where: 90-100: A, 80-89: B, 70-79: C, 60-69: D, <60: F
#Include boundary values and invalid inputs (e.g., -5, 105, "eighty").

#Expected Output:
#Grade assignment function passing test suite 
def assign_grade(score):
    if not isinstance(score, (int, float)):
        return "Invalid input"
    if score < 0 or score > 100:
        return "Invalid input"
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'


