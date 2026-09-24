employees = {
    "name": ["Amulya", "Rahul", "Priya", "Sneha", "Amit"],
    "department": ["AI", "Data", "AI", "Data", "AI"],
    "salary": [85000, 72000, 95000, 68000, 90000]
}
total_salary = 0
earning_above_80000 = 0
for i in range(len(employees["name"])):
    total_salary += employees['salary'][i]
    if employees['salary'][i] > 80000:
        earning_above_80000 += 1
    print(f"{employees['name'][i]} | {employees['department'][i]} | {employees['salary'][i]}")

print(f"Total Salary: Rs. {total_salary}")
print(f"Average Salary: Rs. {total_salary / len(employees['name']):.2f}")
print(f"Employees earning above Rs. 80000: {earning_above_80000}")
print("Unique Departments:", set(employees['department']))
