'''Write a Python class Car with attributes: brand, model, year.
•	Car Details:
•	Brand: Toyota
•	Model: Corolla
•	Year: 2020
2.	Add a method display_details() that prints car details.
'''
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_details(self):
        print(f"Car Details:\nBrand: {self.brand}\nModel: {self.model}\nYear: {self.year}")
# Example usage
my_car = Car("Toyota", "Corolla", 2020)
my_car.display_details()
