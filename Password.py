import re

def assess_password_strength(password: str) -> str:
    # Criteria flags
    length_ok = len(password) >= 8  # Password length
    has_upper = bool(re.search(r'[A-Z]', password))  # Uppercase letter
    has_lower = bool(re.search(r'[a-z]', password))  # Lowercase letter
    has_digit = bool(re.search(r'\d', password))  # Number
    has_special = bool(re.search(r'[\W_]', password))  # Special character

    # Count the number of criteria satisfied
    criteria_met = sum([length_ok, has_upper, has_lower, has_digit, has_special])

    # Determine strength based on the number of criteria met
    if criteria_met == 5:
        strength = "Strong"
    elif criteria_met == 4:
        strength = "Medium"
    else:
        strength = "Weak"

    # Provide feedback on the password
    feedback = []

    if not length_ok:
        feedback.append("Password should be at least 8 characters.")
    if not has_upper:
        feedback.append("Password should contain at least one uppercase letter.")
    if not has_lower:
        feedback.append("Password should contain at least one lowercase letter.")
    if not has_digit:
        feedback.append("Password should contain at least one digit.")
    if not has_special:
        feedback.append("Password should contain at least one special character.")

    return strength, feedback

# Prompt the user to enter a password
password = input("Enter a password to assess its strength: ")

# Assess the password strength
strength, feedback = assess_password_strength(password)

# Output the result
print(f"\nPassword Strength: {strength}")
for message in feedback:
    print(message)