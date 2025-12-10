# Improve Naming conventions , Encapsulation , Readability & maintainability of the below python script
'''class emp:
    def __init__(self,n,s):
        self.n=n
        self.s=s
    def inc(self,p):
        self.s=self.s+(self.s*p/100)
    def pr(self):
        print("emp:",self.n,"salary:",self.s)'''
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def increase_salary(self, percentage):
        self.salary += self.salary * (percentage / 100)

    def print_details(self):
        print(f"Employee: {self.name}, Salary: {self.salary}")
# Example usage:
emp1 = Employee("John Doe", 50000)
emp1.increase_salary(10)
emp1.print_details()  # Output: Employee: John Doe, Salary: 55000.0