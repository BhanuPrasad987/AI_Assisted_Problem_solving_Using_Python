#Generate a Python solution for the following task:

#Task:
#generate test cases for a ShoppingCart class (add_item, remove_item, total_cost).

#Methods to be included:
#Add_item(name,price)
#Remove_item(name)
#Total_cost()


#Expected Output:
#Full class with tested functionalities
class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, name, price):
        if name in self.items:
            self.items[name] += price
        else:
            self.items[name] = price

    def remove_item(self, name):
        if name in self.items:
            del self.items[name]
        else:
            return "Item not found in cart."

    def total_cost(self):
        return sum(self.items.values()) 
