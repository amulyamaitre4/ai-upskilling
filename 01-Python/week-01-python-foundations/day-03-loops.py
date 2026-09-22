#Challenge 1 - for loop
# expenses = [120, 450, 75, 300, 90]
# for expense in expenses:
#     print(expense)

#Challenge 2 — Sum all expenses
# total_expenses = 0
# for expense in expenses:    
#     total_expenses += expense   
# print("Total expenses: Rs.", total_expenses)

#Challenge 3 — Count matching values
# count = 0
# for expense in expenses:
#     if expense > 200:
#         count += 1
# print("Expenses above Rs. 200: ", count)

#Challenge 4 — Find the largest expense
# largest_expense = expenses[0]
# for expense in expenses:
#     if expense > largest_expense:
#         largest_expense = expense
# print("Largest expense: Rs.", largest_expense)

#Challenge 5 — for loop + user input
# expense_count = int(input("How many expenses? "))
# total_expenses = 0
# for i in range(expense_count):
#     expense = float(input(f"Expense {i + 1}: "))
#     total_expenses += expense
# print("Total expenses: Rs.", total_expenses)
# print("Number of expenses: ", expense_count)

#Challenge 6 — while loop
# total_expenses = 0
# expense = 1
# while expense != 0:
#     expense = float(input("Enter expense: "))
#     if expense != 0:
#         total_expenses += expense
# print("Total expenses: Rs.", total_expenses)

#Challenge 7 — while + validation
# total_expenses = 0
# expense = 1
# while expense != 0:
#     expense = float(input("Enter expense: "))
#     if expense != 0:
#         if expense < 0:
#             print("Invalid expense. Please enter a positive amount.")
#             continue
#         total_expenses += expense
# print("Total expenses: Rs.", total_expenses)

#Challenge 8 — Nested loops? Not yet!
# correct_password = "python123"
# counter = 0
# while counter < 3:
#     password = input("Enter password: ")
#     if password == correct_password:
#         print("Login successful.")
#         break
#     else:
#         print("Incorrect password.")
#         counter += 1
#         if counter == 3:
#             print("Account locked.")

#Challenge 9 — for + continue
transaction_amounts = [100, -50, 250, 0, 400, -20, 150]
total_amount = 0
for amount in transaction_amounts:
    if amount < 0:
        continue
    total_amount += amount
print("Total valid transactions: Rs.", total_amount)