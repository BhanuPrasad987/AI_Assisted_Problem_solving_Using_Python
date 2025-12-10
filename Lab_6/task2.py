# Write a Python function that prints the first 10 multiples of a given number using a loop.
# Then modify the function to use another type of controlled loop 
def print_multiples_for_loop(number):
    for i in range(1, 11):
        print(number * i)

def print_multiples_while_loop(number):
    i = 1
    while i <= 10:
        print(number * i)
        i += 1
# Example usage:
print("Using for loop:")            
print_multiples_for_loop(5)
print("Using while loop:")
print_multiples_while_loop(5)