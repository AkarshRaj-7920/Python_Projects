# Task 11: Dev utility toolkit

import datetime
import myutilities
import pyjokes

# Showing Date and Time
ext_date = datetime.datetime.now()
current_time = ext_date.strftime("%y/%m/%d %H:%M:%S %p")
print(f"\n[Utility Toolkit started - {current_time}]")

# Greeting
Intro = myutilities.greet("Akarsh")
fact_ = myutilities.fact_torial(12)
print(f"{Intro} \nThe factorial of 12 is {fact_}\n")

# Joke
print(f"---|Joke of is asfollows|---\n{pyjokes.get_joke()}")
