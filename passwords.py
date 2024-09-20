import re
def createPassword():
    while True:
        password = input("Enter the password (at least 8 characters, with uppercase, lowercase, digit, and special character): ")
        if len(password) < 8:
            print("Password is too short. Please try again.")
        elif not re.search("[a-z]", password):
            print("Password must include at least one lowercase letter. Please try again.")
        elif not re.search("[A-Z]", password):
            print("Password must include at least one uppercase letter. Please try again.")
        elif not re.search("[0-9]", password):
            print("Password must include at least one digit. Please try again.")
        elif not re.search("[@#$%^&+=]", password):
            print("Password must include at least one special character. Please try again.")
        else:
            break
    return password