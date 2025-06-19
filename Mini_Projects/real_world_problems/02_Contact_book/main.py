# 05 Mini Problem
# Contact Book Manager

print(f"{format("| Contact Book Manager |", "-^60")}")

''' Information '''
contact_index = 0
lis_unique_names = []
lis_names = []
lis_contacts = []
lis_email = []

''' Input '''
while True:
    a = f"○ Type \'add\' to Add a Contact List \n○ Type \'exit\' to Exit the Contact List"
    _ask_ = input(f"{a} \n○ Typo {format(":", ">26")} ")
    if _ask_.lower() == 'add':
        contact_index += 1
        while True:
            add_unique = input(f" • Give a Unique Name for {contact_index} {format(":", ">5")} ")
            if add_unique.replace(" ", "").isalnum():
                lis_unique_names.append(add_unique)
                while True:
                    name = input(f"  -> Name {format(":", ">23")} ")
                    if name.replace(" ", "").isalpha():
                        lis_names.append(name)
                        while True:
                            contact = input(f"  -> Contact Number {format(":", ">13")} ")
                            if contact.isdigit() and len(contact) == 10:
                                lis_contacts.append(contact)
                                while True:
                                    email = input(f"  -> Email {format(":", ">22")} ")
                                    if ("@" in email) and ((".com" in email) or (".in" in email)):
                                        lis_email.append(email)
                                        break
                                    else:
                                        print(f"\t|{format("Invalid Input", "-^21")}|")
                                        continue
                                break
                            else:
                                print(f"\t|{format("Invalid Input", "-^21")}|")
                                continue
                        break
                    else:
                        print(f"\t|{format("Invalid Input", "-^21")}|")
                        continue
                break
            else:
                print(f"\t|{format("Invalid Input", "-^21")}|")
                continue

    elif _ask_.lower() == 'exit':
        break
    else:
        print("Invalid Input \nEnter Values \n")
        continue
    
if len(lis_unique_names) == 0:
    print(f"No Contacts in your Contact Book")
    exit()


'''Conversion of Lists to nested Dictionary'''
print(f"{format("| Saved all the Contact Lists |", "-^60")}")
print("\n")
contact_book_manager = {Unique_name:{"Name" : name1, "Contact" : contact1, "Email" : email1} for Unique_name, name1, contact1, email1 in zip(lis_unique_names, lis_names, lis_contacts, lis_email)}

'''Asking user about which contact number'''
print(f"{format("", "<<20")}{"| Your all Contact Lists Name |"}{format("", ">>20")}")

for index, i in enumerate(lis_unique_names):
    print(f"{index}. {i}")

print(f"{format("", "<<34")}| |{format("", ">>34")}\n")

print(f"{format("", "=>75")}")
while True:
    user_ask = input(f" ○ Enter Contact Serial Number to Get Information: ") 
    
    if user_ask.isdigit():
        user_index = int(user_ask)
        if 0 <= user_index < len(lis_unique_names):
            print(f"\t• {lis_unique_names[int(user_ask)]}")

            key_name = lis_unique_names[int(user_ask)]
            for sub_key, values in contact_book_manager[key_name].items():
                print(f"\t ->{sub_key} : {values}")
            break
        
        else:
            print(f"\t|{format("Enter Number from your contact List", "-^45")}|") 
    else:
        print(f"\t|{format("Invalid Input", "-^21")}|")

print(f"{format("", "=>75")}")