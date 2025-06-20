# Student Task

''' Iterables '''
student_no = 0
lis_roll_nos = []
lis_names = []
lis_class = []
lis_maths_marks = []
lis_science_marks = []
lis_english_marks = []

''' Input '''
while True:
    a = f"{format("", "-^64")}"
    print(f"{a}")

    b = f" ○ Type \'add\' to add a Students Information \n ○ Type \'done\' to complete adding Students Information"
    ask_usr = input(f"{b} \n • Typo{format(":", ">16")} ")
    if ask_usr.lower() == 'add':
        print(f"\n\t\t|{format("Student Information", "-^29")}|")
        student_no += 1

        while True:
            print(f"  > Student {student_no}:-")
            roll_number = input(f"  ☼ Roll Number{format(": ", ">9")}")
            if roll_number.isdigit():
                lis_roll_nos.append(roll_number)

                while True:
                    name = input(f"  ☼ Name{format(": ", ">16")}")
                    if name.replace(" ", "").isalpha():
                        lis_names.append(name)
                        
                        while True:
                            class_ = input(f"  ☼ Class{format(": ", ">15")}")
                            if class_.isdigit():
                                class_int = int(class_)
                                if 1 <= class_int <=10 :
                                    lis_class.append(class_int)

                                    while True:
                                        maths = input(f"  ☼ Maths Marks{format(": ", ">9")}")
                                        if maths.isdigit():
                                            maths_int = int(maths)
                                            if 0 <= maths_int <= 100:
                                                lis_maths_marks.append(maths_int)

                                                while True:
                                                    science = input(f"  ☼ Science Marks{format(": ", ">7")}")
                                                    if science.isdigit():
                                                        science_int = int(science)
                                                        if 0 <= science_int <= 100:
                                                            lis_science_marks.append(science_int)
                                                            
                                                            while True:
                                                                english = input(f"  ☼ English Marks{format(": ", ">7")}")
                                                                if english.isdigit():
                                                                    english_int = int(english)
                                                                    if 0 <= english_int <= 100:
                                                                        lis_english_marks.append(english)
                                                                        print(f"{a}\n")

                                                                        break

                                                                    else:
                                                                        print(f"\n\t\t|{format("Invalid Input", "-^20")}|")
                                                                        print(f"   -→ [Enter English Marks between 0 to 100]")
                                                                        print(f"   -→ [Renter English Marks of \'Student {student_no}\'] again...\n")
                                                                        # Format (How to Show output after the error occured)
                                                                        print(f"\t\t|{format("Student Information", "-^29")}|")
                                                                        print(f"  > Student {student_no}:-")
                                                                        print(f"  ☼ Roll Number{format(":", ">8")} {roll_number}")
                                                                        print(f"  ☼ Name{format(":", ">15")} {name}")
                                                                        print(f"  ☼ Class{format(":", ">14")} {class_}")
                                                                        print(f"  ☼ Maths Marks{format(":", ">8")} {maths}")
                                                                        print(f"  ☼ Science Marks{format(":", ">6")} {science}")
                                                                        continue
                                                                    
                                                                else:
                                                                    print(f"\n\t\t|{format("Invalid Input", "-^20")}|")
                                                                    print(f"   -→ [Enter English Marks in Digits]")
                                                                    print(f"   -→ [Renter English Marks of \'Student {student_no}\'] again...\n")
                                                                    # Format (How to Show output after the error occured)
                                                                    print(f"\t\t|{format("Student Information", "-^29")}|")
                                                                    print(f"  > Student {student_no}:-")
                                                                    print(f"  ☼ Roll Number{format(":", ">8")} {roll_number}")
                                                                    print(f"  ☼ Name{format(":", ">15")} {name}")
                                                                    print(f"  ☼ Class{format(":", ">14")} {class_}")
                                                                    print(f"  ☼ Maths Marks{format(":", ">8")} {maths}")
                                                                    print(f"  ☼ Science Marks{format(":", ">6")} {science}")
                                                                    continue

                                                            break

                                                        else:
                                                            print(f"\n\t\t|{format("Invalid Input", "-^20")}|")
                                                            print(f"   -→ [Enter Science Marks in between 0 to 100]")
                                                            print(f"   -→ [Renter Science Marks of \'Student {student_no}\'] again...\n")
                                                            # Format (How to Show output after the error occured)
                                                            print(f"\t\t|{format("Student Information", "-^29")}|")
                                                            print(f"  > Student {student_no}:-")
                                                            print(f"  ☼ Roll Number{format(":", ">8")} {roll_number}")
                                                            print(f"  ☼ Name{format(":", ">15")} {name}")
                                                            print(f"  ☼ Class{format(":", ">14")} {class_}")
                                                            print(f"  ☼ Maths Marks{format(":", ">8")} {maths}")
                                                            continue
                                                    
                                                    else:
                                                        print(f"\n\t\t|{format("Invalid Input", "-^20")}|")
                                                        print(f"   -→ [Enter Science Marks in Digits]")
                                                        print(f"   -→ [Renter Science Marks of \'Student {student_no}\'] again...\n")
                                                        # Format (How to Show output after the error occured)
                                                        print(f"\t\t|{format("Student Information", "-^29")}|")
                                                        print(f"  > Student {student_no}:-")
                                                        print(f"  ☼ Roll Number{format(":", ">8")} {roll_number}")
                                                        print(f"  ☼ Name{format(":", ">15")} {name}")
                                                        print(f"  ☼ Class{format(":", ">14")} {class_}")
                                                        print(f"  ☼ Maths Marks{format(":", ">8")} {maths}")
                                                        continue

                                                break
                                            
                                            else:
                                                print(f"\n\t\t|{format("Invalid Input", "-^20")}|")
                                                print(f"   -→ [Enter Maths Marks in between 0 to 100]")
                                                print(f"   -→ [Renter Maths Marks of \'Student {student_no}\'] again...\n")
                                                # Format (How to Show output after the error occured)
                                                print(f"\t\t|{format("Student Information", "-^29")}|")
                                                print(f"  > Student {student_no}:-")
                                                print(f"  ☼ Roll Number{format(":", ">8")} {roll_number}")
                                                print(f"  ☼ Name{format(":", ">15")} {name}")
                                                print(f"  ☼ Class{format(":", ">14")} {class_}")
                                                continue

                                        else:
                                            print(f"\n\t\t|{format("Invalid Input", "-^20")}|")
                                            print(f"   -→ [Enter Maths Marks in Digits]")
                                            print(f"   -→ [Renter Maths Marks of \'Student {student_no}\'] again...\n")
                                            # Format (How to Show output after the error occured)
                                            print(f"\t\t|{format("Student Information", "-^29")}|")
                                            print(f"  > Student {student_no}:-")
                                            print(f"  ☼ Roll Number{format(":", ">8")} {roll_number}")
                                            print(f"  ☼ Name{format(":", ">15")} {name}")
                                            print(f"  ☼ Class{format(":", ">14")} {class_}")
                                            continue

                                    break

                                else:
                                    print(f"\n\t\t|{format("Invalid Input", "-^20")}|")
                                    print(f"   -→ [Enter Class between 1 to 10]")
                                    print(f"   -→ [Renter Class of \'Student {student_no}\'] again...\n")
                                    # Format (How to Show output after the error occured)
                                    print(f"\t\t|{format("Student Information", "-^29")}|")
                                    print(f"  > Student {student_no}:-")
                                    print(f"  ☼ Roll Number{format(":", ">8")} {roll_number}")
                                    print(f"  ☼ Name{format(":", ">15")} {name}")
                                    continue
                                    
                            else:
                                print(f"\n\t\t|{format("Invalid Input", "-^20")}|")
                                print(f"   -→ [Enter Class in Digits]")
                                print(f"   -→ [Renter Class of \'Student {student_no}\'] again...\n")
                                # Format (How to Show output after the error occured)
                                print(f"\t\t|{format("Student Information", "-^29")}|")
                                print(f"  > Student {student_no}:-")
                                print(f"  ☼ Roll Number{format(":", ">8")} {roll_number}")
                                print(f"  ☼ Name{format(":", ">15")} {name}")
                                continue
                        
                        break
                    
                    else:
                        print(f"\n\t\t|{format("Invalid Input", "-^20")}|")
                        print(f"   -→ [Enter Name in Letters]")
                        print(f"   -→ [Renter Name of \'Student {student_no}\'] again...\n")
                        # Format (How to Show output after the error occured)
                        print(f"\t\t|{format("Student Information", "-^29")}|")
                        print(f"  > Student {student_no}:-")
                        print(f"  ☼ Roll Number{format(":", ">8")} {roll_number}")
                        continue
                
                break
            
            else:
                print(f"\n\t\t|{format("Invalid Input", "-^20")}|")
                print(f"   -→ [Enter Roll Number in Digits]")
                print(f"   -→ [Renter Roll Number of \'Student {student_no}\'] again...\n")
                # Format (How to Show output after the error occured)
                print(f"\t\t|{format("Student Information", "-^29")}|")
                continue

    elif ask_usr.lower() == 'done':
        print(f"{a}")
        break

    else:
        print(f"\n\t\t|{format("Invalid Input", "-^20")}|\n")
        print(f" -→ Type \'add\' or \'done\' anything else will not be accepted \n{a}\n ")


if len(lis_roll_nos) == 0:
    print(f"\t ○ No Roll Numbers were added")
    exit()