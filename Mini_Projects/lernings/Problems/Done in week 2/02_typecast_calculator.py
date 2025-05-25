# Problem 2
# Typecast Calculator

def is_valid(value):
    try:
        return float(value)
    except ValueError:
        return None

num1 = input("Enter first number: ").strip()
num2 = input("Enter second number: ").strip()
operations = input("Enter operation (+, -, *, /): ").strip()

while is_valid(num1) is None:
    print("\nInvalid Input \nEnter a valid number in digits")
    num1 = input("Enter first number: ").strip()

while is_valid(num2) is None:
    print("\nInvalid Input \nEnter a valid number in digits")
    num2 = input("Enter second number: ").strip()


signs = "+-*/"
while operations not in signs or len(operations) != 1:
    print ("Enter valid operation")
    operations = input("Enter operation (+, -, *, /): ")

if operations == "+":
    result = float(num1) + float(num2)
elif operations == "-":
    result = float(num1) - float(num2)
elif operations == "*":
    result = float(num1) * float(num2)
elif operations == "/":
    result = float(num1) / float(num2) if float(num2) != 0 else "Error: Cannot divide by 0"

print(f"Result: {num1} {operations} {num2} = {result}")
