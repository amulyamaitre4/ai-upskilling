monthly_salary = float(input("Monthly salary: "))
annual_bonus = float(input("Annual bonus: "))
annual_salary = (monthly_salary * 12)
print("Annual salary: Rs.", annual_salary)
total_annual_compensation = annual_salary + annual_bonus
print("Total annual compensation: Rs.", total_annual_compensation)
monthly_equivalent = total_annual_compensation / 12
print(f"Monthly equivalent: Rs. {monthly_equivalent:.2f}")