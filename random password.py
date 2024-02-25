import random
import string

def generate_password(length, include_lowercase, include_uppercase, include_digits, include_symbols):
    # Define character sets based on user preferences
    lowercase_chars = string.ascii_lowercase if include_lowercase else ''
    uppercase_chars = string.ascii_uppercase if include_uppercase else ''
    digit_chars = string.digits if include_digits else ''
    symbol_chars = string.punctuation if include_symbols else ''

    # Combine the selected character sets
    all_chars = lowercase_chars + uppercase_chars + digit_chars + symbol_chars

    # Check if at least one character set is selected
    if not all_chars:
        return "Password generation failed. Please select at least one character set."

    # Generate the password
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

# User-defined criteria
length = int(input("Enter the desired password length: "))
include_lowercase = input("Include lowercase letters? (yes/no): ").lower() == "yes"
include_uppercase = input("Include uppercase letters? (yes/no): ").lower() == "yes"
include_digits = input("Include digits? (yes/no): ").lower() == "yes"
include_symbols = input("Include symbols? (yes/no): ").lower() == "yes"

# Generate and print the password
password = generate_password(length, include_lowercase, include_uppercase, include_digits, include_symbols)
print("Generated Password:", password)
