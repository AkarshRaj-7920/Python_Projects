# Problem 5
# Username Extractor

email = input("Enter your Email(@gmail.com): ")

while "@" not in email or email.count("@") != 1:
    print("Invalid Input \nEnter valid input according to instructions")
    email = input("Enter your Email(@gmail.com): ")

# Logic
at_index = email.index("@")
username = email.lower()[:at_index]
domain = email[at_index + 1:]

print("---|Username Extracter Initiated|---")
print(f"Username: {username} \nDomain: {domain}")