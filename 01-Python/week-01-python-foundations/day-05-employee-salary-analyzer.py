employees = {
    'name': ['Amulya', 'Rahul', 'Priya', 'Sneha', 'Amit'],
    'department': ['AI', 'Data', 'AI', 'Data', 'AI'],
    'salary': [85000, 72000, 95000, 68000, 90000]
}

def calculate_average_salary():
    total_salary = sum(employees['salary'])
    average_salary = total_salary / len(employees['salary'])
    return average_salary

def get_high_earners():
    high_earners = []
    for i in range(len(employees['name'])):
        if employees['salary'][i] > 80000:
            high_earners.append(employees['name'][i])
    return high_earners

def get_departments():
    return set(employees['department'])

print(f"Average Salary: Rs. {calculate_average_salary():.2f}")
print(f"High Earners: {get_high_earners()}")
print(f"Departments: {get_departments()}")