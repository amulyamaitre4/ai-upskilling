expenses = [120, 450, 75, 300, 90, 600, 50, 250]
total_expenses = 0
expenses_above_200 = 0
expenses_below_100 = 0
largest_expense = expenses[0]
for expense in expenses:
    total_expenses += expense
    if expense > 200:
        expenses_above_200 += 1
    if expense > largest_expense:
        largest_expense = expense
    if expense < 100:
        expenses_below_100 += 1
average_expense = total_expenses / len(expenses)
print("Total expenses: Rs.", total_expenses)   
print("Expenses above Rs. 200: ", expenses_above_200)
print("Largest expense: Rs.", largest_expense)
print("Expenses below Rs. 100: ", expenses_below_100)
print(f"Average expense: Rs. {average_expense:.2f}")
