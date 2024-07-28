print("This is v3 calculator script (addition, subtraction, and Multiplication)")
print("please choose an operation: ")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
choice = input("Enter a number selection --> ")

num1 = int(input("Enter your first number --> "))
num2 = int(input("Enter your second number --> "))
if choice == "1":
    print(f"{num1} + {num2} = {num1+num2}")
elif choice == "2":
    print(f"{num1} - {num2} = {num1-num2}")
elif choice == "3":
    print(f"{num1} * {num2} = {num1 * num2}")
else:
    print("No valid option selected.")