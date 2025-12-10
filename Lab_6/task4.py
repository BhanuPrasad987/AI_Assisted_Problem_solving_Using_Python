# Write a Python function sum_to_n() that calculates the sum of the first n natural numbers using a loop, 
# then modify it to use another controlled looping and also provide the proper explanation for the generated code 

#Using for loop
def sum_to_n(n):
    # Initialize sum to 0
    total_sum = 0
    # Loop from 1 to n (inclusive)
    for i in range(1, n + 1):
        total_sum += i  # Add the current number to total_sum
    return total_sum  # Return the final sum        


#Using while loop
def sum_to_n(n):
    # Initialize sum to 0
    total_sum = 0
    # Initialize counter to 1
    i = 1
    # Loop until counter exceeds n
    while i <= n:
        total_sum += i  # Add the current number to total_sum
        i += 1          # Increment the counter
    return total_sum  # Return the final sum
