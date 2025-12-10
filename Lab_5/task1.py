#Generate a python code to create a login system
import getpass  
# A simple login system
def login_system():
    # Predefined username and password
    USERNAME = "admin"
    PASSWORD = "password123"

    print("Welcome to the Login System")
    
    # Prompt user for username and password
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")

    # Check if the entered credentials match the predefined ones
    if username == USERNAME and password == PASSWORD:
        print("Login successful! Welcome, " + username + ".")
    else:
        print("Login failed! Invalid username or password.")
        
#provide the revised secured version of the login system
import getpass
import hashlib

# Secure login system using password hashing
def secure_login_system():
    print("Welcome to the Secure Login System")

    # Simulated user database (in real cases, store in a database or encrypted file)
    stored_username = "admin"
    # Store only the hashed password (hash of "password123")
    stored_password_hash = hashlib.sha256("password123".encode()).hexdigest()

    # Prompt user for login credentials
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")

    # Hash the entered password before comparison
    entered_password_hash = hashlib.sha256(password.encode()).hexdigest()

    # Compare username and password hash
    if username == stored_username and entered_password_hash == stored_password_hash:
        print(f"✅ Login successful! Welcome, {username}.")
    else:
        print("❌ Login failed! Invalid username or password.")

