# Task 13
# List Toolkit

list1 = []
while True:
    num = input("Enter a Number: ")
    if num.replace("-", "").isdigit():
        num = int(num)
        list1.append(num)
        print("Enter another number OR \nType 'End' to get results\n")
    elif num.lower() == "end":
        print("\n-----|Your Results|-----\n")
        break
    else:
        print("Invalid Input")

# Original List
print(f"Original List: {list1}")

# Squares of all the numbers
list2 = [q**2 for q in list1]
print(f"Squares of Numbers = {list2}")

# Remove Duplitaces
print(f"The list without repeating numbers is {set(list1)}")

# Sorted List
list1.sort()
print(f"Sorted List:- {list1}")

# Highest and Lowest value
print(f"Highest Value {list1[-1]} \nSmallest Value {list1[0]}")

# Sum of all Numbers
num_sum = 0
for i in list1:
    num_sum += i
print(f"Sum of all Numbers = {num_sum}")