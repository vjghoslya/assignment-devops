import re

def check_password_strength(password):
    # Check Minimum Length of password
    if len(password) < 8:
        return False
    
    # Check for uppercase character in password
    if not any(char.isupper() for char in password):
        return False
    
    # Check for lowercase character in password
    if not any(char.islower() for char in password):
        return False
    
    # Check for digit in password
    if not any(char.isdigit() for char in password):
        return False
    
    # Check for special character in given password
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    
    return True

# Get password from user
    password = input("Enter your password: ")
    
    if check_password_strength(password):
        print("Entered password is strong")
    else:
        print("Entered password is weak. Password must have following characters")
        print("1. At least 8 characters long.")
        print("2. Contains both uppercase and lowercase letters.")
        print("3. Contains at least one digit (0-9).")
        print("4. Contains at least one special character (e.g., !, @, #, $, %).")