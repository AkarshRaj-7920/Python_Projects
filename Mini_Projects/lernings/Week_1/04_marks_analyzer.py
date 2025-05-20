'''
A student is calculating his overall result of VIth grade
There are 5 subject in total
English, II language, Mathematics, Science, Social Studies 
'''
# Total marks of each subject

print ("Marks Analyzer")

_eng_ = 100
_2lang_ = 100
_math_ = 80
_sci_ = 80
_sst_ = 80

test_marks_overall = _eng_ + _2lang_ + _math_ + _sci_ + _sst_


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
                    exit()
            else:
                print ("Enter Correct Values and try again")
                exit()
        else:
            print ("Enter Correct Values and try again")
            exit()
    else:
        print ("Enter correct Values and try again")
        exit()
else:
    print ("Enter correct Values and try again")
    exit()


print("\n----------Score Card----------")
'''
Score Card includes 
Total Marks, Average Marks, Percentage, Subjects passed, Overall result
'''

total_marks = sub1_English + sub2_IInd_lang + sub3_Maths + sub4_Science + sub5_SST
print ("\nTotal Marks Obtained: ", total_marks,"\\", test_marks_overall)

ovr_all_avg = total_marks/5
print ("Average in 5 subjects: ", ovr_all_avg)

per_centage = (total_marks/test_marks_overall) * 100
print ("Percentage scored: ", per_centage)

# Calculating over all result passed or failed

print("\n-----Passed or Failed-----")
if (sub1_English <= 35) and (sub2_IInd_lang <= 35) and (sub3_Maths <= 26) and (sub4_Science <= 26) and (sub5_SST <= 26):
    print("\nOver all Result Failed")
elif (35 < sub1_English <= 85) and (35 < sub2_IInd_lang <= 85) and (26 < sub3_Maths <= 65) and (26 < sub4_Science <= 65) and (26 < sub5_SST <= 65):
    print("\nOver all Result Passed")
elif (sub1_English > 85) and (sub2_IInd_lang > 85) and (sub3_Maths > 65) and (sub4_Science > 65) and (sub5_SST > 65):
    print ("\nPassed with Grade A")
else :
    print("\nFailed")

print ("\n-----Subectwise passed and Failed-----")
if (sub1_English >= 35):
    print("\nEnglish: Passed")
else:
    print("\nEnglish: Failed")
     
if (sub2_IInd_lang >= 35): 
    print("IInd Language: Passed")
else:
    print("IInd Language: Failed")
    
if (sub3_Maths >= 26):
    print("Maths: Passed")
else:
    print("Maths: Failed") 

if (sub4_Science >= 26):
    print("Science: Passed")
else:
    print("Science: Failed")

if (sub5_SST >= 26):
    print("Social Studies: Passed")
else:
    print("Social Studies: Failed")

# ------------------------------------------------------------THE END--------------------------------------------------------------------------

