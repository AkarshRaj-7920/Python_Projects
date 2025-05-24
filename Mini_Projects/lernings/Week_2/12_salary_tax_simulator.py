# Salary Tax Calculator 

print("Salary Tax Calculator")
salary_ = input("\nEnter your salary: ")

while not salary_.isdigit():
    print("Enter values in digits")
    salary_ = input("Enter your salary: ")

# Tax calculator calculator
def salary_tax(x):
    '''
    If salary is less than 250000 tax is 0%
    If salary is more than 250000 and less than 500000 tax is 5%
    If salary is more than 500000 and less than 1000000 tax is 10%
    If salary is more than 1000000 tax is 20%
    '''
    if x <= 250000:
        y = 0
    elif 250000 < x <= 500000:
        y = 5
    elif 500000 < x <= 1000000:
        y = 10
    else:
        y = 20
    p = x * (y/100)
    return p

print(f"The Ammount of tax you have to pay is {salary_tax(int(salary_))}")
print(f"Salary left after paying tax is {int(salary_) - salary_tax(int(salary_))}\n")
z = salary_tax.__doc__
print(f"Tax for every slab is given below:- {z}")


