# Countdown using While Loop

'''
This is a part of Missile launch program
'''

print("Your Missile launches in")

ent_num = int(input("Set time to launch (in seconds): "))

if ent_num < 0:
    print("""Enter the time correct or else 
        MISSILE will BLAST off on your own heads before sending it to enimies.
        You will dig your own grave and coffin will be above you""")
    exit()

print ("\nCountdown begun sending your coffins in: ")

while (0 <= ent_num < (ent_num+1)):
    print(ent_num)
    ent_num = ent_num - 1

print ("BOOMMMMM !!!")
print("""\n A good man said I will repeat:- 
 I have sucessfully privitized world peace.
      Thank You""")

