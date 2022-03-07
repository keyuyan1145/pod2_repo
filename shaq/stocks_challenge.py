print("Challenge 3.2: Playing with the stock market")

print()

# Creating variables to store the current (approximate) market price of these 5 companies - Amazon, Apple, Facebook, Google and Microsoft.

amazon = 3000
apple = 100
fb = 250
google = 1400
msft = 200

print("Challenge 3.2.1: Taking user input")
# TODO: Write code to ask the client his name and save it to a variable.
name = input("whats your name?\n")
# TODO: Write code to ask the client his savings and save it to another variable.
savings = (int(input("whats your savings?\n")))
# TODO: Write code to ask the client the stock he is interested in and save it to another variable, as shown below.
stock = input("Which stock are you interested in? Type 'amzn' for Amazon, 'aapl' for Apple, 'fb' for Facebook, 'goog' for Google and 'msft' for Microsoft.\n")
print()

print("Challenge 3.2.2: Perform user-specific calculations")
# TODO: You have all 3 user inputs stores in variables. Based on that, write conditional (if-elif-else) statements to find out the number of stocks of the company that can be purchased with the savings amount.


#Your code should look like this:

if stock == "amzn":
    stocks = (savings / amazon)
    
elif stock == "aapl":
    stocks = (savings / apple)

elif stock == "fb":
    stocks = (savings / fb)

elif stock == "goog":
    stocks = (savings / google)

elif stock == "msft":
    stocks = (savings / msft)


print(stocks)

print("Challenge 3.2.3: Output for the user the result")
# TODO: Once you have calculated the number of stocks that can be purchased, print the result for the client. Result should be in a format like this:
print(f"{name} has ${savings} in savings and can buy {int(stocks)} shares of {stock} at the current price of ${stocks}.")
# Alex has $5000 in savings and he can buy 50 shares of Apple at the current price of $100.

print()
