def check_password(password):
    length_ok = len(password) >= 8
    uppercase_ok = False
    lowercase_ok = False
    number_ok = False
    special_ok = False

    for char in password:
        if char.isupper():
            uppercase_ok = True

        if char.islower():
            lowercase_ok = True

        if char.isdigit():
            number_ok = True

        if not char.isalnum():
            special_ok = True

    satisfied = 0

    if length_ok:
        satisfied += 1

    if uppercase_ok:
        satisfied += 1

    if lowercase_ok:
        satisfied += 1

    if number_ok:
        satisfied += 1

    if special_ok:
        satisfied += 1

    if satisfied <= 2:
        strength = "WEAK"
    elif satisfied <= 4:
        strength = "MEDIUM"
    else:
        strength = "STRONG"

    print("\n===== PASSWORD ANALYSIS =====")

    print("At least 8 characters:", length_ok)
    print("Contains uppercase letter:", uppercase_ok)
    print("Contains lowercase letter:", lowercase_ok)
    print("Contains a number:", number_ok)
    print("Contains special character:", special_ok)

    print("\nStrength:", strength)


print("Password Strength Checker")

password = input("Enter your password: ")

check_password(password)