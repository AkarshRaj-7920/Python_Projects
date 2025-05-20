# A Day Translator using month

month_num = int(input("Enter a number between 1 to 12: "))
day_num = int(input("Enter a number between 1 to 7: "))

print ("\nYour day and month are:-")
match month_num:
    case 1:
        print ("Month: January")
    case 2:
        print ("Month: Febuary")
    case 3:
        print ("Month: March")
    case 4:
        print ("Month: April")
    case 5:
        print ("Month: May")
    case 6:
        print ("Month: June")
    case 7:
        print ("Month: July")
    case 8:
        print ("Month: August")
    case 9:
        print ("Month: September")
    case 10:
        print ("Month: October")
    case 11:
        print ("Month: November")
    case 12:
        print ("Month: December")
    case _:
        print ("Enter valid number between 1 to 12")

match day_num:
    case 1:
        print ("Day: Monday")
    case 2:
        print ("Day: Tuesday")
    case 3:
        print ("Day: Wednesday")
    case 4:
        print ("Day: Thrusday")
    case 5:
        print ("Day: Friday")
    case 6:
        print ("Day: Saturday")
    case 7:
        print ("Day: Sunday")
    case _:
        print ("Enter valid number between 1 to 7")

#------------------------------------THE END----------------------------------------------