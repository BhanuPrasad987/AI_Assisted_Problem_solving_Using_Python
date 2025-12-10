#For the given below python script make readability and modularity improvements:

'''
class Student:
    def __init__(self, n, a, m1, m2, m3):
        self.n = n
        self.a = a
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    def details(self):
        print("Name:", self.n, "Age:", self.a)
    def total(self):
        return self.m1+self.m2+self.m3'''
class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks  # marks should be a list or tuple of three marks
    def display_details(self):
        print(f"Name: {self.name}, Age: {self.age}")
    def calculate_total_marks(self):
        return sum(self.marks)
# Example usage:
student = Student("Alice", 20, (85, 90, 95))
student.display_details()
print("Total Marks:", student.calculate_total_marks())



