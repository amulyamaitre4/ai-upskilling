#Challenge 1 - Age Checker
# age = int(input("Enter your age: "))
# if age < 13:
#     print("You are a child.")
# elif 13 <= age <= 19:
#     print("You are a teenager.")
# else:
#     print("You are an adult.")

#Challenge 2 - Discount Checker
# age = int(input("Age: "))
# if age >= 65 or age < 18:
#     print("You are eligible for a discount.")
# else:
#     print("You are not eligible for a discount.")

# Challenge 3 - Premium Discount
# age = int(input("Age: "))
# is_member = input("Are you a member? (yes/no): ")
# if age >= 18 and is_member == "yes":
#     print("You are eligible for the premium discount.")
# else:
#     print("You are not eligible for the premium discount.")


# Challenge 4 - Account Access
# is_blocked = input("Is your account blocked? (yes/no): ")
# if not is_blocked == "yes":
#     print("Access granted.")
# else:
#     print("Access denied.")

#Challenge 5 — BMI Calculator
# weight = float(input("Enter your weight in kg: "))
# height = float(input("Enter your height in meters: "))
# bmi = weight / (height ** 2)
# if bmi < 18.5:
#     print("You are underweight.")
# elif 18.5 <= bmi <= 24.9:
#     print("You have a normal weight.")
# elif 25 <= bmi <= 29.9:
#     print("You are overweight.")
# else:
#     print("You are obese.")

#Challenge 6 — Electricity Bill Calculator
# units_consumed = float(input("Enter the number of units consumed: "))
# bill_amount = 0
# if units_consumed <= 100:
#     bill_amount = units_consumed * 5
# elif units_consumed <= 200:
#     bill_amount = (100 * 5) + (units_consumed - 100) * 7
# else:
#     bill_amount = (100 * 5) + (100 * 7) + (units_consumed - 200) * 10
# print("Total electricity bill: Rs.", bill_amount)

#Challenge 7 — Login Validator
username = input("Enter username: ")
password = input("Enter password: ")
if username == "admin" and password == "password123":
    print("Login successful.")
else:
    print("Invalid username or password.")