#Challenge 1 - Lists
# expenses = [120, 450, 75, 300, 90]
# first_expense = expenses[0]
# last_expense = expenses[-1]
# print("First expense:", first_expense)
# print("Last expense:", last_expense)
# for expense in expenses:
#     if expense == 75:
#         expenses[expenses.index(expense)] = 100
# print("Updated expenses:", expenses)

#Challenge 2 - List Operations
# expenses.append(600)
# expenses.insert(0, 50)
# expenses.remove(75)
# expenses.pop()
# print("Updated expenses:", expenses)

#Challenge 3 — Lists + Loops
# expenses = [120, 450, 75, 300, 90, 600, 50, 250]
# count = 0
# expenses_above_200 = []
# for expense in expenses:
#     if expense > 200:
#         expenses_above_200.append(expense)
#         count +=1
# print("Expenses above Rs. 200:", expenses_above_200)
# print("Count:", count)

#Challenge 4 — Tuples
# employee = (101, "AI", "Pune")
# print("Employee: ", employee)
# print("Employee ID:", employee[0])
# print("Department:", employee[1])
# employee[1] = "ML"  # This will raise an error because tuples are immutable


#Challenge 5 — Dictionaries
# employee = {'name': "Amulya", 'role': "SDE2", 'experience': 6, 'department': "AI"}
# print("Employee: ", employee)
# print("Name:", employee['name'])
# print("Role:", employee['role'])
# employee['role'] = "AI Engineer"  # Update role
# employee['location'] = "Pune"  # Add new key-value pair
# print("Updated Employee: ", employee)

#Challenge 6 — Dictionary + Loop
# employees = {
#     "Amulya": 85000,
#     "Rahul": 72000,
#     "Priya": 95000,
#     "Sneha": 68000
# }
# count_salary_above_80000 = 0
# total_salary = 0
# for name, salary in employees.items():
#     print(f"{name}: Rs. {salary}")
#     total_salary += salary
#     if salary > 80000:
#         count_salary_above_80000 += 1

# print(f"Employees earning above Rs. 80000: {count_salary_above_80000}")
# print(f"Total salary: Rs. {total_salary}")

#Challenge 7 — Nested Dictionaries
# employee = {'name': "Amulya", 'role': "AI Engineer", 'skills': {'Python': "Advanced", 'SQL': "Advanced", 'Snowflake': "Intermediate"}}
# print("Employee:", employee['name'])
# print("Role:", employee['role'])
# for skill, level in employee['skills'].items():
#     if skill in ("Python", "Snowflake"):
#         print(f"{skill}: {level}")
# employee['skills']['Snowflake'] = "Advanced"  # Update skill level
# employee['skills']['AWS'] = "Beginner"  # Add new skill
# print("Updated Employee:", employee)

#Challenge 8 — Sets
categories = {"Food", "Travel", "Food", "Shopping", "Travel", "Bills", "Food"}
print("Set:", categories)
categories.add("Entertainment")  # Add new category
categories.add("Food")  # Add a category
print("Updated Set:", categories)
print("Number of unique categories:", len(categories))