password = input("Enter a password to validate: ")

failed_conditions = []

if len(password) < 8:
    failed_conditions.append("Minimum 8 characters")

if not any(char.isupper() for char in password):
    failed_conditions.append("At least one uppercase letter")

if not any(char.islower() for char in password):
    failed_conditions.append("At least one lowercase letter")

if not any(char.isdigit() for char in password):
    failed_conditions.append("At least one digit")

if not any(not char.isalnum() and not char.isspace() for char in password):
    failed_conditions.append("At least one special character")

if not failed_conditions:
    print("Password is valid!")
else:
    print("Password is invalid! The following condition(s) were not satisfied:")
    for condition in failed_conditions:
        print(f"- {condition}")
