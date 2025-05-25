# Problem 3
# Age Gate Checker

def is_valid(value):
    try:
        return int(value)
    except ValueError:
        return None

age = input("Enter your age: ")

while is_valid(age) is None:
    print("\nInvalid age \nEnter values in digits")
    age = input("Enter your age: ")

if int(age) in range(0, 6):
    result = "You're just a baby grow up first"
elif int(age) in range(6, 13):
    result = "Go to playschool"
elif int(age) in range(13, 18):
    result = "There no such thing like puberty"
elif int(age) in range(18, 60):
    result = "Great buckle up for upcoming deasease, \nyou are going to suffer"
elif int(age) >= 60:
    result = "Now we are talking, get ready to go to Heaven in few years,\nIf bad luck then few months\nIf baddest luck just few days"
else:
    result = "Get to earth first then we will talk"

print(f"Statement according to your age: \n{result}")