# Functions Showcase

'''
Defining Functions
by Creating a average 
'''
def average(a, b, c):
    d = (a + b + c)/3.0
    return d

o1 = average(2, 3, 5)
print(o1)

'''---Arguments---'''

#Positional Argument
def multiply (a, b):
    return a*b
print (multiply(12, 3))

# Default Argument
def greet (name = "Guest"):
    return f"Hello {name}"
print(greet())
print(greet('Akarsh'))

# Keyword Argument
def Intro(name1, age):
    print (f"Hi I am {name1} and I am {age} years old")
Intro(name1 = "Akarsh Raj", age= 18)

'''---Lambda Function---'''
# Creating squares function using Lanbda

square = lambda x: x*x
print (square(2))

'''---Recursions---'''
# Fibonachi Series using recursions

def fibo(n):
    # Base of recursions
    if (n == 0 or n == 1):
        return n
    
    return fibo(n-2) + fibo(n-1)

print(fibo(6))