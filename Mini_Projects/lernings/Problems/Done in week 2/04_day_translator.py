# Problem 4
# Day Translator
    
day_num = input("Enter a value: ")

while not day_num.isdigit() or not (1 <= int(day_num) <= 7):
    print("Invalid Input \nEnter the number between 1 to 7")
    day_num = input("Enter a value: ")

match int(day_num):
    case 1:
        print("That's Monday.")
    case 2:
        print("That's Tuesday.")
    case 3:
        print("That's Wednesday.")
    case 4:
        print("That's Thursday.")
    case 5:
        print("That's Friday.")
    case 6:
        print("That's Saturday.")
    case 7:
        print("That's Sunday.")
