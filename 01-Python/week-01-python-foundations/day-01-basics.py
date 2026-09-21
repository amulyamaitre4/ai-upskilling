#Challenge 1 - Variables & Data Types
name = 'Amulya'
age = 28
years_of_experience = 5
currently_learning_python = True

print("Name:", name)
print("Age:", age)
print("Experience:", years_of_experience, "years")
print("Learning Python:", currently_learning_python)

#Challenge 2 - Input + Type Conversion
age = int(input("Enter your age: ")) # Convert the input to an integer
print("Age:", age)
print("Type:", type(age))  # Print the type of the variable
print("Age in 5 years:", age + 5)

#Challenge 3 - Operators & Calculations
bill = float(input("Food bill: "))  # Convert the input to an integer
number_of_people = int(input("Number of people: "))  # Convert the input to an integer
tip_percentage = float(input("Tip percentage: "))  # Convert the input to an integer
tip_amount = (bill * tip_percentage) / 100
total_amount = bill + tip_amount
amount_per_person = total_amount / number_of_people
print("Food bill: Rs.", bill)
print("Tip: Rs.", tip_amount)
print("Total bill: Rs.", total_amount)
print("Amount per person: Rs.", amount_per_person)


#Challenge 4 - Temperature Converter
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(celsius, "°C = ", fahrenheit, "°F")

fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print(fahrenheit, "°F =", celsius, "°C")

#Challenge 5 — Simple Calculator
first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))
operation = input("Enter operation: ")
if operation == "+":
    print("Result:", first_number + second_number)
elif operation == "-":
    print("Result:", first_number - second_number)
elif operation == "*":
    print("Result:", first_number * second_number)
elif operation == "/":
    if second_number != 0:
        print("Result:", first_number / second_number)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation")