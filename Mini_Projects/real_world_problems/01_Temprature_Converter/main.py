# 04 Mini Problem
# Temprature Converter

''' Input '''
temp_value = input(f"{format("| Start |", "-^40")} \nEnter the value: ")
while not temp_value.replace(".", "").replace("-", "").isdigit():
    print("Invalid Input \nEnter Values in Digits or Decimal\n")
    temp_value = input(f"{format("| Start |", "-^40")} \nEnter the value: ")

int_temp_value = float(temp_value)
units = ('c', 'k', 'f')
a, b, c = units

while True:
    from_unit_value = input("Unit of entered value: ")
    lowfrom_unit_value = from_unit_value.lower()    # Conversion
    if len(lowfrom_unit_value) != 1:
        print("\nEnter One letter only")
    if lowfrom_unit_value == a:
        break
    elif lowfrom_unit_value == b:
        break
    elif lowfrom_unit_value == c:
        break
    else:
        print("Enter Unit between c, k and f \n")

while True:
    to_unit_value = input("Unit to convert value: ")
    lowto_unit_value = to_unit_value.lower()    # Conversion
    if len(lowto_unit_value) != 1:
        print("\nEnter One letter only")
    if lowto_unit_value == a:
        break
    elif lowto_unit_value == b:
        break
    elif lowto_unit_value == c:
        break
    else:
        print("Enter Unit between c, k and f \n")

def temp_converter(Value, from_unit, to_unit):
    '''Conversion'''
    str_from_unit = str(from_unit)
    str_to_unit = str(to_unit)

    '''Logic for value'''
    if str_from_unit == str_to_unit:
        return "No need of conversion \'Same Units\' "
    
    if str_from_unit == 'c':
        if Value < -(273.15):
            return f"Temprature in Celcius cannot be less than -273.15°C \n{format("| END |", "-^40")}"
        
        if str_to_unit == 'k':
            '''Celcius converted to Kelvin'''
            kelvin1 = 273.15 + Value
            return f"{format("", "->30")} \nCelcius converted to Kelvin \nKelvin Value : {round(kelvin1, 2)} \n{format("| END |", "-^40")}"
        elif str_to_unit == 'f':
            '''Celcius converted to Fahrenheit'''
            fahrenheit1 = (Value*(9/5)) + 32
            return f"{format("", "->30")} \nCelcius converted to Fahrenheit\nFahrenheit Value : {round(fahrenheit1, 2)} \n{format("| END |", "-^40")}"

    elif str_from_unit == 'k':
        if Value < 0:
            return f"Tempraute in Kelvin cannot be less than 0 K \n{format("| END |", "-^40")}"
        
        if str_to_unit == 'c':
            '''Kelvin converted to Celcius'''
            celcius1 = int_temp_value - 273.15
            return f"{format("", "->30")} \nKelvin converted to Celcius\nCelcius Value : {round(celcius1, 2)}°C \n{format("| END |", "-^40")}"
        elif str_to_unit == 'f':
            '''Kelvin converted to Fahrenheit'''
            fahrenheit2 = ((Value - 273.15)*(9/5)) + 32
            return f"{format("", "->30")} \nKelvin converted to Fahrenheit\nFahrenheit Value : {round(fahrenheit2, 2)}°F \n{format("| END |", "-^40")}"

    elif str_from_unit == 'f':
        if Value < -(459.67):
            return f"Tempraute in Fahrenheit cannot be less than -459.67°F \n{format("| END |", "-^40")}"
        
        if str_to_unit == 'k':
            '''Fahrenheit converted to Kelvin'''
            kelvin2 = (((Value - 32)*(5/9)) + 273.15)
            return f"{format("", "->30")} \nFahrenheit converted to Kelvin\nKelvin Value : {round(kelvin2, 2)}K \n{format("| END |", "-^40")}"
        elif str_to_unit == 'c':
            '''Fahrenheit converted to Celcius'''
            celcius2 = ((Value - 32)*(5/9))
            return f"{format("", "->30")} \nFahrenheit converted to Celcius\nCelcius Value : {round(celcius2, 2)}°C \n{format("| END |", "-^40")}"

a = temp_converter(Value = int_temp_value, from_unit = lowfrom_unit_value, to_unit = lowto_unit_value)
print(a)