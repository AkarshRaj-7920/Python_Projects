# Problem 6 
# Grade Calculator

grade = input("Enter your marks obtained: ")

# Input condition
while not grade.isdigit() or not (0 <= int(grade) <= 100):
    print("Invalid Input \nEnter values in digits")
    grade = input("Enter your marks obtained: ")

# Condition
a = int(grade)
if a in range (0, 50):
    result = "F \nFeedback: \'Failed, Try again\'"
elif a in range (50, 60):
    result = "D \nFeedback: \'Just Passed\'"
elif a in range (60, 70):
    result = "C \nFeedback: \'Good, But can do better\'"
elif a in range (70, 80):
    result = "B \nFeedback: \'Very Good\'"
elif a in range (80, 90):
    result = "A \nFeedback: \'Excellent\'"
elif a in range (90, 101):
    result = "A+ \nFeedback: \'Outstanding\'"

print(f"Marks: {grade} \nGrade: {result}")