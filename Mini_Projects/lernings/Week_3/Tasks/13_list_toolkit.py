# Task 13
# List Toolkit

list1 = []
while True:
    num = input("Enter a Number: ")
    if num.replace("-", "").isdigit():
        num = int(num)
        list1.append(num)
        print("Enter another number OR \nType 'End' to get results\n")
    elif num == "End":
        print("\n-----|Your Results|-----\n")
        break
    else:
        print("Invalid Input")

# Sorted List
list1.sort()
print(f"Sorted List:- {list1}")

# Sum of all Numbers
num_sum = 0
for i in list1:
    num_sum += i
print(f"Sum of all Numbers = {num_sum}")



