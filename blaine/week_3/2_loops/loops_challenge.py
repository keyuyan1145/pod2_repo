
from multiprocessing.sharedctypes import Value


days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

# QUESTION 1: For loops with list

# Let's start simple, and build up from there.
# 1.1: Write a for loop that prints out each day in the `days` variable above.

# loop through list of days and print d
for day in days:
    print(day)

# 1.2: Now, instead of printing out the day, let's ask the user what their favorite thing
# to do is on that day of the week. (Make sure to use an f-string so that the user knows which
# day they're being asked about.)
users_fav_activity = []

for day in days:
    fav_thing = input(f'What is your favorite thing to do on {day}?')
    users_fav_activity.append(fav_thing)


# 1.3: We should keep track of the user's favorite things to do so that we can print them out all together.
# ABOVE your for loop, create a new empty list to hold the user's favorite activities.


# 1.4: Now, back in your for loop, append each of the user's answers into your new list.
# Print out the list after your loop to check if it got populated correctly.
print(users_fav_activity)



# 1.5: After your first loop, let's create a new one. As an example, let's say the user's favorite thing to
# do on mondays is plan their week. This time, we want the output to be something like this:
# 'On Mondays, your favorite activity is to plan your week.'
# We need information from both lists! Let's use the `range` function to loop through the indexes
# of the items in the lists (this will work because the lists are the same length).
# Each time through this new loop, use the index number to index into each of your lists for the data
# you need to print out.

# Loop through range based on length of list
for index in range(len(days)):
    print(f'On {days[index]}, your favorite activity is {users_fav_activity[index]}.')


# Take a look back at the code you just wrote. Look at how much it does!
# Often, programmers will be given large tasks, and it's our responsibility to be able to break it down into
# smaller pieces. We did the above piece by piece, but think about what the prompt might have been
# to get us there.

# Maybe: Write a program that asks the user about their favorite thing to do each day of the week.
# Afterward, print out for the user each of their favorite daily activities.

# Loop through each day
for day in days:
    # get user input
    fav_thing = input(f'What is your favorite thing to do on {day}?')
    print(f'On {day}, your favorite activity is {fav_thing}.')


# Would this larger task have felt doable without breaking it down into steps?
# Is it clear what needs to be done?

# Try to break down the steps required for this second loop challenge.

# QUESTION 2: For loops with list, again

# Write a program that loops through the days in the week. Each day, ask the user what the temperature
# is. If the temperature is below 50, tell the user to put on a jacket. Or, if the temperature is
# between 50 and 65, tell the user to put on a sweater. Finally, if the temperature is above 65,
# tell the user to put on some sunscreen.

for day in days:
    #Try to get input from user and if given none, catch the error 
    try:
        temp = int(input(f'On {day}, what will the temperature be?'))
        if temp < 50:
            print("You should wear a jacket")
        elif 50 <= temp <= 65:
            print("You should wear a sweater")
        elif temp > 65:
            print("You should put on some sunscreen")  
    except ValueError:
        print("You didn't enter a value")



# QUESTION 3: For loops with the range function

# Write a program that asks the user how many times they would like to be wished happy birthday.
# Then, print out happy birthday that number of times.

#Try to get input from user and if given none, catch the error 
try:
    happy_bdays = int(input('How many times should I wish you Happy Birthday?'))
    for happy_bday in range(happy_bdays):
        print('Happy Birthday!')
except ValueError:
    print("I needed a number but you gave me nothing")



# QUESTION 4: While loops

# Write a program that asks the user what temperature it is outside. While the temperature is below 65,
# tell the user to wear a sweater. Once the temperature is over 65, stop looping, and tell the user that
# Spring has sprung!

while True:
    # Get temp input from user
    temp = int(input('What is the temperature outside?'))
    # IF temp is over 65.. break loop
    if temp > 65: break
    # print
    print('You should wear a sweater')
print('Spring has sprung!')


# NOTE: remember, if you accidentally create an infinite while loop, it's ok! Go into the command line and
# a) on a mac: hit command + C to stop your program, or b) on a pc: hit control + C to stop the program.
# No harm done to your computer (:
