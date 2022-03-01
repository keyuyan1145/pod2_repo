# READ THE INSTRUCTIONS FILE (nba_challenge_instructions.md) FIRST
# EXTRA: This challenge is not required for a grade!

#print("Challenge 2.1:")
jamal_murray_3pts_made = 46
Fred_VanVleet_3pts_made = 43
James_Harden_3pts_made = 37

print("Challenge 2.2:")
print(f"In the 2020 NBA playoffs, Jamal Murray made {jamal_murray_3pts_made} 3-point shots")
print(f"In the 2020 NBA Playoffs, Fred VanVleet made {Fred_VanVleet_3pts_made} 3-point shots")
print(f"In the 2020 NBA playoffs, James Harden made {James_Harden_3pts_made} 3-point shots")
print()

print("Challenge 2.3: Store the number of three point shot attempts in variables for each player")
Jamal_Murray_3pts_attempts = 93
Fred_VanVleet_3pts_attempts = 110
James_Harden_3pts_attempts = 109
print()

print("Challenge 2.4: Build on your print statement")
# TODO: Copy the three print statements you wrote in Challenge 2.2 and extend them to also print
# the number of three point shots for each player. E.g., output should be similar to
# "In the 2020 NBA playoffs, player X made Y 3-point shots out of Z 3-point shot attempts."
print(f"In the 2020 NBA playoff, Jamal Murray attempted {Jamal_Murray_3pts_attempts} 3-point shots")
print(f"In the 2020 NBA playoffd, Fred Vanvleet attempted {Fred_VanVleet_3pts_attempts} 3-point shots")
print(f"In the 2020 NBA playoffs, James Harden attempted {James_Harden_3pts_attempts} 3-point shots")

print("Challenge 2.5: Calculate, store, and print the three point percentage for each player")
# TODO: Calculate the three point percentage, which is given by `three points made/three point attempts`
# TODO: Calculate and print the 3-point percentage for Jamal Murray
# TODO: Calculate and print the 3-point percentage for Fred VanVleet
# TODO: Calculate and print the 3-point percentage for James Harden

jamalpercentage = jamal_murray_3pts_made/Jamal_Murray_3pts_attempts
fredpercentage = Fred_VanVleet_3pts_made/Fred_VanVleet_3pts_attempts
jamespercentage = James_Harden_3pts_made/James_Harden_3pts_attempts

print(jamalpercentage)
print(fredpercentage)
print(jamespercentage)

print('Challenge 3.1: Print out the paragraph but with only 1 sentence per line')
# TODO: Print the giant chunk of text out using escape characters so each sentence comes out on a new line

print('Challenge 3.2: Print out the paragraph but with only 1 sentence per line')
# TODO: As above, print out the paragraph with only 1 sentence per line, and all in upper case

print('Challenge 3.3: Make a boolean variable indicating whether you think the Lakers are the best NBA team')
# TODO: make a variable called `lakers_are_best` to indicate this
# TODO: print out the variable in an f-string to convey your opinion on the lakers

print('Challenge 3.4: Type Conversion')
# TODO: Convert your `lakers_are_best` variable to an integer, and print it out.
# TODO: Convert your `lakers_are best` variable to a float, and print it out

print('Challenge 3.5: Type Conversion Part 2')
# TODO: Take each player's three point percentage (from part 2.5) and convert it to a string, then print it out.
# TODO: Take each player's three point percentage (from part 2.5) and convert it to an integer, then print it out.
