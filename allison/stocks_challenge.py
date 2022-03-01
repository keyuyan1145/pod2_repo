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
client_name=input('What is your name?')
# TODO: Write code to ask the client his savings and save it to another variable.
client_savings=int(input('How much are your savings?'))
# TODO: Write code to ask the client the stock he is interested in and save it to another variable, as shown below.
stock = input("Which stock are you interested in? Type 'amzn' for Amazon, 'aapl' for Apple, 'fb' for Facebook, 'goog' for Google and 'msft' for Microsoft.")
print()

print("Challenge 3.2.2: Perform user-specific calculations")
# TODO: You have all 3 user inputs stores in variables. Based on that, write conditional (if-elif-else) statements to find out the number of stocks of the company that can be purchased with the savings amount.
if stock=='amzn':
    num_stocks=client_savings//amazon
    stock_name='Amazon'
    stock_price=amazon
elif stock=='aapl':
    num_stocks=client_savings//apple
    stock_name='Apple'
    stock_price=apple
elif stock=='fb':
    num_stocks=client_savings//fb
    stock_name='Facebook'
    stock_price=fb
elif stock=='goog':
    num_stocks=client_savings//google
    stock_name='Google'
    stock_price=google
else:
    num_stocks=client_savings//msft
    stock_name='Microsoft.amzn'
    stock_price=msft

'''
Your code should look like this:

if stock == "amzn":
    ...
elif ...
else ...
'''

print()

print("Challenge 3.2.3: Output for the user the result")
# TODO: Once you have calculated the number of stocks that can be purchased, print the result for the client. Result should be in a format like this:
print(f'{client_name} has ${client_savings} in savings and can buy {num_stocks} shares of {stock_name} at the current price of ${stock_price}.')
# Alex has $5000 in savings and he can buy 50 shares of Apple at the current price of $100.

print()
