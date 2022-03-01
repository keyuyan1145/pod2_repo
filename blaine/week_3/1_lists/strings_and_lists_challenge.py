# You run a startup media company called Ripple Media
# It's typical when you hire a new employee in your company, to setup an email id for them

from ntpath import join


employee_name = 'Ash Rahman'

# You have decided the format of the email should be: Ash Rahman -> ash.rahman@ripplemedia.com
# Let's write some code that converts a name into an email id that matches this format
# 1.1 TODO: Let's save the lowercase version of the employee_name in a new variable 'lower_name' (use a string method to lower the name)

# --------- USE STRING METHOD LOWER() TO CONVERT STRING TO LOWER CASE
lower_name = employee_name.lower()
print(lower_name)

# 1.2 TODO: We want to separate the first name and last name and save it in a variable 'names_list' (use a string method to split the string into a list)

# --------- SPLIT THE LOWER CASED VARIABLE TO CREATE LIST
names_list = lower_name.split()
print(names_list)

# 1.3 TODO: We want to join the first name and last name with a '.' and save it in a variable called 'joined_names' (use a string method to join the list into a new string)

# JOIN THE LOWER CASED LIST WITH A '.'
joined_names = ".".join(names_list)
print(joined_names)

# 1.4 TODO: We want to add '@ripplemedia.com' to the end of the string inside joined_names and save it in a variable 'email' (use an f-string to combine the username with the email domain)

# ADD '@ripplemedia.com' TO NEW STRING
email = joined_names + '@ripplemedia.com'
print(email)