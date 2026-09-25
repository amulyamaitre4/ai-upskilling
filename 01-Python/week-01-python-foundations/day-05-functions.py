#Challenge 1 — Your First Function
# def calculate_total(expenses):
#     total_expenses = 0
#     for expense in expenses:    
#         total_expenses += expense   
#     return total_expenses    

# expenses = [120, 450, 75, 300, 90]
# total_expenses = calculate_total(expenses)
# print("Total expenses: Rs.", total_expenses)

#Challenge 2 — Function Parameters
# def calculate_discount(price, discount_percentage):
#     discount_amount = price * (discount_percentage / 100)
#     discounted_price = price - discount_amount
#     return discounted_price
# original_price = 1000
# discount_percentage = 10
# print(f"Original Price: Rs. {original_price}")
# print(f"Discount: {discount_percentage}%")
# print("Final Price: Rs.", calculate_discount(original_price, discount_percentage))

#Challenge 3 — Multiple Return Values
# def analyze_expenses(expenses):
#     total_expenses = sum(expenses)
#     largest_expense = max(expenses)
#     count_above_200 = sum(1 for expense in expenses if expense > 200)
#     return total_expenses, largest_expense, count_above_200
# expenses = [120, 450, 75, 300, 90, 600, 50, 250]
# total_expenses, largest_expense, count_above_200 = analyze_expenses(expenses)
# print("Total: Rs.", total_expenses)
# print("Largest: Rs.", largest_expense)
# print("Above 200:", count_above_200)

#Challenge 4 — Default Parameters
# def calculate_bonus(salary, bonus_percentage=10):
#     bonus_amount = salary * (bonus_percentage / 100)
#     return bonus_amount
# print("Bonus at default rate: Rs.", calculate_bonus(60000))
# print("Bonus at 15%: Rs.", calculate_bonus(60000, 15))

#Challenge 5 — Functions + Conditions
# def get_discount_percentage(age):
#     if age < 18:
#         return 10
#     elif age >= 65:
#         return 15
#     else:
#         return 0
# age = int(input("Age: "))
# print(f"{get_discount_percentage(age)}% discount")

#Challenge 6 — Functions + Loops
# def calculate_total_expenses(expenses):
#     total_expenses = 0
#     for expense in expenses:
#         total_expenses += expense
#     return total_expenses
# expenses = [120, 450, 75, 300, 90, 600]
# print("Total expenses: Rs.", calculate_total_expenses(expenses))

#Challenge 7 — Functions + Validation
# def validate_expense(expense):
#     if expense <= 0:
#         return False
#     else:
#         return True
# expense = [500,-100,0,250]
# for e in expense:
#     check = validate_expense(e)
#     if not check:
#         print(f"{e}: Invalid")
#     else:
#         print(f"{e}: Valid")

#Challenge 8 — Function Scope
tax_rate = 0.18
def calculate_tax(amount):
    tax = amount * tax_rate
    return tax
calculated_tax = calculate_tax(1000)
print("Tax: Rs.", calculated_tax)


#Challenge 9 — Function Composition
def calculate_discount(price, percentage):
    discount_amount = price * (percentage / 100)
    return discount_amount

def calculate_final_price(price, percentage, tax_rate):
    discount = calculate_discount(price, percentage)
    discounted_price = price - discount
    tax = discounted_price * tax_rate
    final_price = discounted_price + tax
    return discounted_price,final_price

discounted_price,final_price =calculate_final_price(1000, 10, 0.18)
print("Discounted Price: Rs.", discounted_price)
print("Final Price: Rs.", final_price)