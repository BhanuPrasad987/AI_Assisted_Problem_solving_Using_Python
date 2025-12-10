#Generate a Python solution for the following task:

#Task:
#write test cases for conversion convert_date_format(date_str) to switch from "YYYY-MM-DD" to "DD-MM-YYYY".
#Example: "2023-10-15" → "15-10-2023"

#Expected Output:
#Function converts input format correctly for all test cases
def convert_date_format(date_str):
    try:
        year, month, day = date_str.split('-')
        # Validate structure and ensure all are digits
        if (len(year) == 4 and len(month) == 2 and len(day) == 2 
                and year.isdigit() and month.isdigit() and day.isdigit()):
            return f"{day}-{month}-{year}"
        else:
            return "Invalid date format"
    except ValueError:
        return "Invalid date format"

