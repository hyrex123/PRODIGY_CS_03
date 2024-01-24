import re

def check_password_strength(password):
    # Minimum length requirement
    if len(password) < 8:
        return "Weak: Password should be at least 8 characters long."

    # Check for uppercase letters
    if not any(char.isupper() for char in password):
        return "Weak: Password should contain at least one uppercase letter."

    # Check for lowercase letters
    if not any(char.islower() for char in password):
        return "Weak: Password should contain at least one lowercase letter."

    # Check for numbers
    if not any(char.isdigit() for char in password):
        return "Weak: Password should contain at least one number."

    # Check for special characters
    special_characters = re.compile(r"[!@#$%^&*(),.?\":{}|<>]")
    if not special_characters.search(password):
        return "Weak: Password should contain at least one special character."

    # Strong password
    return "Strong: Password meets the criteria for strength."

# Example usage
password_input = input("Enter your password: ")
result = check_password_strength(password_input)
print(result)
