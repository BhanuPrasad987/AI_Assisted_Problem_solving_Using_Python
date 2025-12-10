#Refactor the following redundant Python code into a cleaner and more modular design.
#Use either dictionary-based dispatch or separate functions to remove repeated logic and improve readability.

'''def calculate_area(shape, x, y=0):
    if shape == "rectangle":
        return x * y
    elif shape == "square":
        return x * x
    elif shape == "circle":
        return 3.14 * x * x'''
def calculate_rectangle_area(length, width):
    return length * width
def calculate_square_area(side):
    return side * side
def calculate_circle_area(radius):
    return 3.14 * radius * radius
def calculate_area(shape, x, y=0):
    area_calculators = {
        "rectangle": calculate_rectangle_area,
        "square": calculate_square_area,
        "circle": calculate_circle_area
    }
    if shape in area_calculators:
        if shape == "rectangle":
            return area_calculators[shape](x, y)
        else:
            return area_calculators[shape](x)
    else:
        raise ValueError("Unsupported shape")
# Example usage:
print(calculate_area("rectangle", 5, 10))  # Output: 50
print(calculate_area("square", 4))         # Output: 16
print(calculate_area("circle", 3))         # Output: 28.26  
