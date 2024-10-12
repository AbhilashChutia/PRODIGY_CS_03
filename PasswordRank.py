import re
import tkinter as tk
from tkinter import messagebox

def check_password_strength(password):
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
    if re.search(r'[\W_]', password):
        strength_score += 1
    else:
        feedback.append("Password should contain at least one special character (e.g., @, #, $, etc.).")


    if strength_score == 4:
        return "Strong Password", feedback
    elif strength_score == 3:
        return "Moderate Password", feedback
    else:
        return "Weak Password", feedback


def on_check_password():
    password = password_entry.get()
    if not password:
        messagebox.showwarning("Input Error", "Please enter a password.")
        return
    
    strength, feedback = check_password_strength(password)
    

    result_message = f"Password Strength: {strength}\n"
    if feedback:
        result_message += "Feedback for improvement:\n"
        for comment in feedback:
            result_message += f"- {comment}\n"
    
    messagebox.showinfo("Password Strength Result", result_message)


root = tk.Tk()
root.title("Password Strength Checker")

root.geometry("600x120")


instruction_label = tk.Label(root, text="Enter your password to check its strength:")
instruction_label.pack(pady=10, padx=10)

password_entry = tk.Entry(root, show="", width=30)
password_entry.pack(pady=5)

check_button = tk.Button(root, text="Check Password Strength", command=on_check_password)
check_button.pack(pady=10)

root.mainloop()
