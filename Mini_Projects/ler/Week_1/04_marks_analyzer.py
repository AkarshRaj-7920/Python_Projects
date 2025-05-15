'''
A student is calculating his overall result of VIth grade
There are 5 subject in total
English, II language, Mathematics, Science, Social Studies 
'''
# Total marks of each subject

_eng_ = 100
_2lang_ = 100
_math_ = 80
_sci_ = 80
_sst_ = 80


sub1_English = int(input("Enter your score in English out of 100: "))

if (0 <= sub1_English <= 100):
    print ("Alright now Subject 2")
    sub2_IInd_lang = int(input("Enter your score in IInd Language out of 100: "))

    if (0 <= sub2_IInd_lang <= 100):
        print("Now Subject 3")
        sub3_Maths = int(input("Enter your score in Mathematics out of 80: "))

        if (0 <= sub3_Maths <= 80):
            print("Now Subject 4")
            sub4_Science = int(input("Enter your score in Science out of 80: "))

            if (0 <= sub4_Science <= 80):
                print ("Now Subject 4")
                sub5_SST = int(input("Enter your score in Social Studies out of 80: "))
                if (0 <= sub5_SST <= 80):
                    print("Done calculating your total overview")
                else:
                    print ("Enter Correct Values and try again")
            else:
                print ("Enter Correct Values and try again")
        else:
            print ("Enter Correct Values and try again")
    else:
        print ("Enter correct Values and try again")
else:
    print ("Enter correct Values and try again")
    

