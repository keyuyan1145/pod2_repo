#1. Convert a temperature of 100 degrees fahrenheit to celsius
#    * Save this to a variable called `celsius_100`, and use `print()` to print out the value
 #   * Is the resulting temperature you get an integer or float? How do you know?
celsius_100 = (100-32) * 5/9
print(celsius_100)
#Because it has a decimal I know its a float and I can also use the type function to check
print(type(celsius_100))

#2. Convert a temperature of 0 degrees fahrenheit to celsius
 #   * Save this to a variable called `celsius_0`, and use `print()` to print out the value
celsius_0 = (0-32) * 5/9
print(celsius_0)


#3. Convert a temperature of 34.2 degrees fahrenheit to celsius #I dont have to assign any variables
#  * Do this one all in one print statement **without** saving any variables
print((34.2-32) * (5/9))

#4. Convert a temperature of 5 degrees celsius to fahrenheit? #I'm doing the opposite of the original equation
print((5 * 9/5) + (32)) 


#5. What is hotter, a temperature of 30.2 degrees celsius, or a temperature of 85.1 degrees fahrenheit?
celsius_2 = (85.1 - 32) * 5/9 #converting 85.1 fahrenheit
print(celsius_2)  #85.1 fahrenheit converted in to celsius eqauls 29.5 
#30.2 celsius is hotter than 85.1 fahrenheit.

