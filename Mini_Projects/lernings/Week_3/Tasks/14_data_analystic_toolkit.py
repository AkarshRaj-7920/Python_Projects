# Task 14
# Data Analystic Toolkit

# Creating empty list of (Names), (Age) and (City)
name_list = []
score_list = []
city_list = []

# Asking User Names
print(format("|Names|", "-^60"))
while True:
    name = input("Enter a your Full-Name: ")
    if name.lower() == "end":
        break
    elif name.replace(" ", "").isalpha():
        name_list.append(name.title())
        print(f"|{format('-', '-<5')} [Enter another Name] {format('-', '-<10')} [Type 'End' to stop writing Name] {format('-', '-<5')}|")
    else:
        print(f"\nInvalid Input \n|{format('-', '-<5')}Enter your Name in letters{format('-', '-<5')}|")

# Scores of the Names entered
a = format("|Scores of Entered Names|", "-^60")
print(f"\n{a}")

def get_names_score(values): # Defining Loop as a Function
    while True:
        score = input(f"Enter {values} obtained score out of 100: ")
        if score.strip().isdigit():
            if int(score) <= 100:
                return score
            else:
                print(f"\nInvalid Input \n|{format('-', '-<5')}Enter Score in Digits and less than 100{format('-', '-<5')}|")
        else:
            print(f"\nInvalid Input \n|{format('-', '-<5')}Enter Score in Digits and less than 100{format('-', '-<5')}|")

# Looping and storing values
for values in name_list:
    score_list.append(int(get_names_score(values))) # Getting the function

# City of entered names
b = format("|Cities of Entered Names|", "-^60")
print(f"\n{b}")

def get_names_city(name):
    while True:
        city = input(f"Enter the City where {name} lives: ")
        if city.replace(" ", "").isalpha():
            return city
        else:
            print(f"\nInvalid Input \n|{format('-', '-<5')}Enter {name} City in letters{format('-', '-<5')}|")

# Looping and storing values
for name in name_list:
    city_list.append(get_names_city(name).title()) # Getting the function

# Creating Dictionaries
#       Dictionary of Names and Scores
dict_name_score = dict(zip(name_list, score_list))

#       Dictionary of Cities and Names
dict_city_names = {}
for names, city in zip(name_list, city_list):
    if city not in dict_city_names:
        dict_city_names[city] = []
    dict_city_names[city].append(names)

#       Dictionary of Scores and Names
dict_reversed_namescore = dict(zip(score_list, name_list))

# Sets of each Names, Ages and Cities
name_set = set(name_list)
score_set = set(score_list)
city_set = set(city_list)

# Data Analytics Panel
l1 = format(" ", "->40")
l2 = format("DATA ANALYTICS PANEL", "^37")

l3 = format("Total Unique Names", "<27")
l4 = format("Total Unique Cities", "<27")
l5 = format("Average Score", "<27")
sum_scores = 0
for i in score_list:
    sum_scores += i

avg = round(sum_scores/(len(score_list)), 2)

l6 = format("Highest Score", "<27")
score_list.sort()
l7 = format("Lowest Score", "<27")
l8 = format("Top 3 Scorers", "<27")
if len(score_list) == 1:
    name1 = dict_reversed_namescore[score_list[-1]]
    a = f"{name1}  =  {score_list[-1]} (1st Place)"
elif len(score_list) == 2:
    name1 = dict_reversed_namescore[score_list[-1]]
    name2 = dict_reversed_namescore[score_list[-2]]
    a = f"{name1} = {score_list[-1]} (1st Place) \n{format(f" ", "<27")}:  {name2} = {score_list[-2]} (2nd Place)"
elif len(score_list) >= 3:
    name1 = dict_reversed_namescore[score_list[-1]]
    name2 = dict_reversed_namescore[score_list[-2]]
    name3 = dict_reversed_namescore[score_list[-3]]
    a = f"{name1} = {score_list[-1]} (1st Place) \n{format(f" ", "<27")}:  {name2} = {score_list[-2]} (2nd Place) \n{format(f" ", "<27")}:  {name3} = {score_list[-3]} (3rd Place)"
else:
    None

print(f"\n{l1} \n|{l2}| \n{l1} \n{l3}:  {len(name_set)} \n{l4}:  {len(city_set)} \n{l5}:  {avg} \n{l6}:  {score_list[-1]} \n{l7}:  {score_list[0]}")
print(f"{l8}:  {a} \n{l1}")
# print(f"City wise names {dict_city_names}")