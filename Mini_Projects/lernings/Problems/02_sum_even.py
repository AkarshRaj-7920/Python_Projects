# Problem 2
# Sum of all Even Numbers

print("Find Sum of Positive Even Numbers \n")

while True:
    evn_num = input("Enter a Number: ")
    if evn_num.isdigit():
        evn_num = int(evn_num)
        break
    else:
        print("\n\t---|Enter Positive Integers|---")
    
numbers = 0
for i in range(2, evn_num + 1, 2):
    numbers += i

print(f"Sum = {numbers}")
