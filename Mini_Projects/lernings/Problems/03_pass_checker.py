# Problem 3
# Creating a Password Checker
print ("Enter your password to check weather it is strong or not\n")
pass_ent = input("Enter password: ")
while len(pass_ent) < 8:
    print ("Password should contain alleat 8 characters")
    pass_ent = input("Enter password: ")
    
print ("Password accepted\n")

# Logic
uppr = ""
for i in pass_ent:
    if i.isupper():
        uppr += i

lwr = ""
for i in pass_ent:
    if i.islower():
        lwr += i

digi = ""
for i in pass_ent:
    if i.isdigit():
        digi += i

spcel_char = R"!@#$%^&*()_-+=|\"';?/.,<>`~"
spcl = ""
for i in pass_ent:
    if i in spcel_char:
        spcl += i

# Summary part
print ("-----|Summary of Password you created|-----")
print(f"Number of Upper case characters: {len(uppr)}")
print(f"Number of Lower case characters: {len(lwr)}")
print(f"Number of Digits used: {len(digi)}")
print(f"Number of Special Charaters: {len(spcl)}")

# Suggestions
print ("-----|Some Suggestions for the Password you created|-----")

if len(uppr) == 0:
    print ("Add atleast 1 Upper case character")

if len(lwr) == 0:
    print ("Add atleast 1 Lower case charater")

if len(digi) == 0:
    print ("Add atleast 1 Digit")

if len(spcl) == 0:
    print ("Add atleast 1 Special character")

if len(uppr)!=0 and len(lwr)!=0 and len(digi)!=0 and len(spcl)!=0:
    print ("Your Password is Good to Go")
