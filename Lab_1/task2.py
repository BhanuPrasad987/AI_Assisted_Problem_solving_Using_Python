#Function to check if a number is prime
def is_prime(num):
    #prime numbers are greater than 1
    if num<=1:
        return False

    #Check for factors from 2 to the square root of the number
    for i in range(2, int(num**0.5) + 1):
        #If num is divisible by any number other than 1 and itself,it's not prime
        if num % i == 0:
            return False

        #If no factors found, the number is prime
        return True

#Take the input from the user
number = int(input("Enter a number: "))

#Call the function and display result
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")