print('1.1: Create a variable called `meal`, and save a string describing what you had for lunch in it')
meal = 'Sandwich'

print('1.2: Print the meal variable')
print(meal)

print('1.3: Update the meal variable to be a string describing what you want for dinner. print it out again')
meal = 'Salad'
print(meal)

print('2: How old is Google?')
# 2.1: Google was founded in 1993. The current year is 2022. Create a variable called google_age, and use subraction
# to figure out how old Google is
# ex: my_age = current_year - birth_year
current_year = 2022
birth_year = 1993
my_age = current_year - birth_year

# 2.2: Print out a sentence about Google's age. Make sure to include your variable in the f-string!
print(my_age, 'years old')

# 2.3 How many _months_ old is Google? Create a new variable google_age_months, and use multiplication to figure it out,
# then print the info.
# (Assume 12 months for each year, you don't need to check which month they started)
age_months = my_age * 12
print(age_months, 'months')

print('3.1: The line of code below is commented out because it produces many SyntaxErrors.')
print('Fix the problem and turn the comment back into regular Python code')
completion_message = 'Completed the first Python challenge!' 

# 3.2 What were the syntax errors that you fixed? print out a quick explanation of each one.
print("1. I had to add a _ to the variable name because there can be no spaces in a variable name.")
print("2. I had the add a second qutation mark in the string to make it complete.")

print('3.3: Turn the comment below back into regular Python code')
print(completion_message)
