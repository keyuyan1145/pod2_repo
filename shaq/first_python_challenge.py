#print('1.1: Create a variable called `meal`, and save a string describing what you had for lunch in it')
meal = "steak"

#print('1.2: Print the meal variable')
print(meal) 

#print('1.3: Update the meal variable to be a string describing what you want for dinner. print it out again')
meal = "lamb chops"
print(meal)

#print('2: How old is Google?')
# 2.1: Google was founded in 1993. The current year is 2022. Create a variable called google_age, and use subraction
# to figure out how old Google is
# ex: my_age = current_year - birth_year

current_year = 2022
birth_year = 1993
googles_age = current_year - birth_year 

print(googles_age)




# 2.2: Print out a sentence about Google's age. Make sure to include your variable in the f-string!
print(f" {current_year} - {birth_year} = {googles_age}")


# 2.3 How many _months_ old is Google? Create a new variable google_age_months, and use multiplication to figure it out,
# then print the info.
# (Assume 12 months for each year, you don't need to check which month they started)
google_age_months = googles_age * 12

print(f"{google_age_months}")


#print('3.1: The line of code below is commented out because it produces many SyntaxErrors.')
#print('Fix the problem and turn the comment back into regular Python code')
google_age_months = googles_age * 12

print(f"{google_age_months}")


#print('3.1: The line of code below is commented out because it produces many SyntaxErrors.')
#print('Fix the problem and turn the comment back into regular Python code')
print("Completed the first Python challenge!")
