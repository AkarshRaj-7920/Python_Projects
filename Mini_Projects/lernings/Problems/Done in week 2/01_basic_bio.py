# Problem 1 
# Basic Bio Generator

# Input
name = input("Enter your name: ")
age = input("Enter your age: ")
gender = input("Enter your gender: ")
city_live = input("Enter city where you live: ")
job_title = input("Enter your Dream Job: ")

while not name.replace(" ", "").isalpha():
    print("\nInvalid name \nEnter values in letters")
    name = input("Enter your name: ")

while not age.replace(" ", "").isdigit():
    print("\nInvalid age \nEnter values in digits")
    age = input("Enter your age: ")
    
while not gender.replace(" ", "").isalpha():
    print("\nInvalid gender \nEnter values in letters")
    gender = input("Enter your gender: ")

while not city_live.replace(" ", "").isalpha():
    print("\nInvalid City Name Enter values in letters")
    city_live = input("Enter city where you live: ")

while not job_title.replace(" ", "").isalpha():
    print("\nInvalid Dream Job \nEnter values in letters")
    job_title = input("Enter your Dream Job: ")

# Condition
if gender == "Male":
    b = "He"
    a = "Boy"
elif gender == "Female":
    b = "She"
    a = "Girl"
else:
    a = "[Gender not stated]"
    b = "[Gender not stated]"

print(f"""\nMeet {name}, an {age}-year-old talented {a}(not talented that me who made this program).
{b} is from {city_live} who dreams to become a {job_title} someday(which I am sure {b} will not).""")