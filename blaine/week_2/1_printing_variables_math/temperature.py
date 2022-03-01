
# -------------------------------------
def convert_to_celsius(fahrenheit):
    '''Converts a fahrenheit value to celsius'''

    return ((fahrenheit - 32) * 5/9)

# -------------------------------------
def convert_to_fahrenheit(celsius):
    '''Converts fahrenheit to celsius'''
    
    return (celsius * 9/5) + 32

# -------------------------------------
# variable to hold fahrenheit value
fahrenheit_value = 100
# use function to convert fahrenheit value to celsuis
celsius_100 = convert_to_celsius(fahrenheit_value)

# print the value returned by function
print(celsius_100)

# Answer to 'Is the resulting temperature you get an integer or float? How do you know?'
# Resulting temperature is a FLOAT because it is a decimal


# -------------------------------------
# variable to hold fahrenheit value
fahrenheit_value = 0
# use function to convert fahrenheit value to celsuis
celsius_0 = convert_to_celsius(fahrenheit_value)
# print value
print(celsius_0)

# print returned value from function
print(convert_to_celsius(34.2))

# -------------------------------------
# variable to hold celsius value
celsius_value = 5
# variable to hold value returned from function
fahrenheit_5 = convert_to_fahrenheit(celsius_value)
# print the value
print(fahrenheit_5)

# if/else statement to print which value is highers
if convert_to_fahrenheit(30.2)> 85.1:
    print('30.2 degrees celsius is hotter than 85.1 degee fahrenheit')
else:
    print('85.1 degees fahrenheit ios hotter than 30.2 degees celsius')

