
class sru_student:
    """A class to represent an SR University student with hostel and fee details."""

    def __init__(self, name, roll_no, hostel_status):
        # Initialize the student's name, roll number, and hostel status
        self.name = name
        self.roll_no = roll_no
        self.hostel_status = hostel_status
        self.fee_paid = False  # Default fee status is unpaid

    def fee_update(self, status):
        # Update the student's fee payment status
        self.fee_paid = status

    def display_details(self):
        # Display all details of the student in a readable format
        print("----- Student Details -----")
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"Hostel Status: {'Hosteller' if self.hostel_status else 'Day Scholar'}")
        print(f"Fee Paid: {'Yes' if self.fee_paid else 'No'}")


# Create an object for the sru_student class and test methods
student1 = sru_student("Sucharitha", 102, True)  # Creating a student instance
student1.fee_update(True)  # Updating fee status as paid
student1.display_details()  # Displaying all student information


#Add Inline Comments to the above code for explaining the functionality.

class sru_student:
    """Represents a student with attributes for name, roll number, and hostel details."""

    def __init__(self, name, roll_no, hostel_status):
        self.name = name  # Stores the student’s name
        self.roll_no = roll_no  # Stores the student’s roll number
        self.hostel_status = hostel_status  # Indicates if the student stays in a hostel
        self.fee_paid = False  # Initializes fee status as not paid

    def fee_update(self, status):
        self.fee_paid = status  # Updates the student's fee payment status (True/False)

    def display_details(self):
        # Prints the student's complete details including name, roll number, hostel status, and fee status
        print("----- Student Details -----")
        print(f"Name: {self.name}")  # Displays student name
        print(f"Roll No: {self.roll_no}")  # Displays roll number
        print(f"Hostel Status: {'Hosteller' if self.hostel_status else 'Day Scholar'}")  # Displays hostel status
        print(f"Fee Paid: {'Yes' if self.fee_paid else 'No'}")  # Displays whether the fee is paid or not


student1 = sru_student("Sucharitha", 102, True)  # Creates a student object with name, roll no, and hostel info
student1.fee_update(True)  # Calls the method to update the fee payment status
student1.display_details()  # Calls the method to print all student details
