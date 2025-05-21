# Problem 1
# Finding the largest

print("""Enter three numbers to find the largest one\n""")

# Accepting Numbers

while True:
    num1 = input("Enter First Number: ")
    if num1.isdigit():
        num1 = int(num1)
        break
    else:
        print ("---|Enter valid Numbers|---")

while True:
    num2 = input("Enter Second Number: ")
    if num2.isdigit():
        num2 = int(num2)
        break
    else:
        print ("---|Enter valid Numbers|---")

while True:
    num3 = input("Enter Third Number: ")
    if num3.isdigit():
        num3 = int(num3)
        break
    else:
        print ("---|Enter valid Numbers|---")


# Logic 

if num1 > num2 and num1 > num3:
    if num2 > num3:
        print(f"Numbers in desending order: {num1} > {num2} > {num3}")
    elif num3 > num2:
        print(f"Numbers in desending order: {num1} > {num3} > {num2}")
    print ("The Largest number is:", num1)

elif num2 > num1 and num2 > num3:
    if num1 > num3:
        print(f"Numbers in desending order: {num2} > {num1} > {num3}")
    elif num3 > num1:
        print(f"Numbers in desending order: {num2} > {num3} > {num1}")
    print ("The Largest number is:", num2)

else:
    if num1 > num2:
        print(f"Numbers in desending order: {num3} > {num1} > {num2}")
    elif num2 > num1:
        print(f"Numbers in desending order: {num3} > {num2} > {num1}")
    print ("The Largest number is:", num3)
