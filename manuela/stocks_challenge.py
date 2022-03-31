print("Challenge 3.2: Playing with the stock market")

print()

# Creating variables to store the current (approximate) market price of these 5 companies - Amazon, Apple, Facebook, Google and Microsoft.

amzn = 3000
aapl = 100
fb = 250
goog = 1400
msft = 200

print("Challenge 3.2.1: Taking user input")
# TODO: Write code to ask the client his name and save it to a variable.
client = input("Enter your name: ")
print(client)

# TODO: Write code to ask the client his savings and save it to another variable.
investment_amount = input(
    "How much of your savings do want to invest?: ")  # write your input

investment_amount = (int(investment_amount))  # change string to int
print(type(investment_amount))  # checking the type of investment_amount input

# TODO: Write code to ask the client the stock he is interested in and save it to another variable, as shown below.
stock = input("Which stock are you interested in? Type 'amzn' for Amazon, 'aapl' for Apple, 'fb' for Facebook, 'goog' for Google and 'msft' for Microsoft.")
print()

print("Challenge 3.2.2: Perform user-specific calculations")
# TODO: You have all 3 user inputs stores in variables. Based on that, write conditional (if-elif-else) statements to find out the number of stocks of the company that can be purchased with the savings amount.

'''
Your code should look like this:

#if stock == "amzn":  #asking client which stock interested in
if stock == ('amzn'):   # == for exacly 'amzn'
    print('I am interested in Amazon stocks')
elif stock.startswith ('aapl'):     #need stock.startswith ' ':   in elif statement
    print('I am interested in Apple stocks')
elif stock.startswith ('fb'):
    print('I am interested in Facebook stocks')
elif stock.startswith ('goog'):
    print('I am interested in Google stocks')
else:                            #just else: then print statement
    #print(f'There has been an input error. ')
    
    print('There has been an input error. Please try again')
    print(f"{client} has ${investment_amount} in savings. And he can buy {shares} shares in {stock}.")
#repeat the if else to close the loop of input error  BONUS
print()

 if stock == ('amzn'):   # == for exacly 'amzn'
    print('I am interested in Amazon stocks')
elif stock.startswith ('aapl'):     #need stock.startswith ' ':   in elif statement
    print('I am interested in Apple stocks')
elif stock.startswith ('fb'):
    print('I am interested in Facebook stocks')
elif stock.startswith ('goog'):
    print('I am interested in Google stocks')
 
    ...
elif ...
else ...
'''

print()

print("Challenge 3.2.3: Output for the user the result")
# TODO: Once you have calculated the number of stocks that can be purchased, print the result for the client. Result should be in a format like this:

# Alex has $5000 in savings and he can buy 50 shares of Apple at the current price of $100.

if stock == ('amzn'):
    shares = f'{investment_amount/amzn}'
elif stock.startswith('aapl'):
    shares = f'{investment_amount/aapl}'
elif stock.startswith('fb'):
    shares = f'{investment_amount/fb}'
elif stock.startswith('goog'):
    shares = f'{investment_amount/goog}'
elif stock.startswith('msft'):
    shares = f'{investment_amount/msft}'
else:
    print('There has been an input error. Please try again')


print(f'{client} has ${investment_amount} in savings. And he can buy {shares} shares in {stock} stock. ')
