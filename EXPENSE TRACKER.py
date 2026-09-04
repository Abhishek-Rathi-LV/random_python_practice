expenses = []

while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Summary")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        amount = float(input("Amount: "))
        category = input("Category: ")
        description = input("Short description: ")

        expense = {
            "amount": amount,
            "category": category,
            "description": description
        }

        expenses.append(expense)
        print("Expense added successfully!")

    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses recorded.")
        else:
            print("\n===== ALL EXPENSES =====")

            for i, expense in enumerate(expenses, 1):
                print(
                    i, ". Amount:", expense["amount"],
                    "| Category:", expense["category"],
                    "| Description:", expense["description"]
                )

    elif choice == "3":
        if len(expenses) == 0:
            print("No expenses recorded.")
        else:
            total = 0
            category_total = {}

            for expense in expenses:
                total += expense["amount"]

                category = expense["category"]

                if category in category_total:
                    category_total[category] += expense["amount"]
                else:
                    category_total[category] = expense["amount"]

            print("\n===== EXPENSE SUMMARY =====")
            print("Total Amount Spent:", total)

            print("\nAmount Spent in Each Category:")
            for category, amount in category_total.items():
                print(category, ":", amount)

            highest_category = max(category_total, key=category_total.get)

            print(
                "\nCategory Where You Spent the Most:",
                highest_category,
                "(", category_total[highest_category], ")"
            )

    elif choice == "4":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice! Please try again.")