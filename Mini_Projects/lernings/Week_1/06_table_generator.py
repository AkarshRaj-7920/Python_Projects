# Table generator 

print ("\nProgram name: \"Generate a Table you don't know\"")

enter_num1 = int(input("Enter your Table Number: "))
enter_num2 = int(input("Enter number till your Table is to multiply: "))

print("\nThe Generated Table is:")
for i in range (0, (enter_num2 + 1)):
    print (enter_num1, "X", i,"=", enter_num1*i)

print('''Tip: Learn tables by yourself u will not get this program in school exams''')