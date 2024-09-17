import re

def check_password_strength(password):
    # Initialize the score
    strength_score = 0
    feedback = []

    # Criteria 1: Password length (minimum 8 characters)
    if len(password) >= 8:
        strength_score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Criteria 2: Contains both uppercase and lowercase letters
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        strength_score += 1
    else:
        feedback.append("Password should contain both uppercase and lowercase letters.")

    # Criteria 3: Contains digits
    if re.search(r'[0-9]', password):
        strength_score += 1
    else:
        feedback.append("Password should contain at least one number.")

    # Criteria 4: Contains special characters
    if re.search(r'[\W_]', password):  # \W matches any non-alphanumeric character
        strength_score += 1
    else:
        feedback.append("Password should contain at least one special character (e.g., @, #, $, etc.).")

    # Assess overall strength based on score
    if strength_score == 4:
        return "Strong Password", feedback
    elif strength_score == 3:
        return "Moderate Password", feedback
    else:
        return "Weak Password", feedback

# Example usage:
if __name__ == "__main__":
    password = input("Enter your password to check: ")
    strength, feedback = check_password_strength(password)
    print(f"Password Strength: {strength}")
    
    if feedback:
        print("Feedback for improvement:")
        for comment in feedback:
            print(f"- {comment}")
