print("Challenge: Favourite Restaurants")

print()

print("Question 1")

'''
Below is a dictionary consisting of details of 1 restaurant fetched from Yelp.

Go through the dictionary and print out the following 3 pieces of information about the restaurant:
1. The latitude and longitude of Four Barrel Coffee
2. The complete address of Four Barrel Coffee, formatted as a string - it should include the address, city, state and the zip code.
3. The website of Four Barrel Coffee
'''


restaurant = {
    "name": "Four Barrel Coffee",
    "url": "https://www.yelp.com/biz/four-barrel-coffee-san-francisco",
    "latitude": 37.7670169511878,
    "longitude": -122.42184275,
    "city": "San Francisco",
    "country": "US",
    "address2": "",
    "address3": "",
    "state": "CA",
    "address1": "375 Valencia St",
    "zip_code": "94103",
    "distance": 1604.23,
    "transactions": ["pickup", "delivery"]
}

print(restaurant)

# TODO: Write code to print the latitude and longitude of Four Barrel Coffee.
print(restaurant['latitude'])
print(restaurant['longitude'])
# TODO: Write code to print the complete address of the Four Barrel Coffee, formatted as a string - it should include the address, city, state and the zip code.
address=restaurant['address1']
city=restaurant['city']
state=restaurant['state']
zip_code=restaurant['zip_code']
print(f'{address}, {city}, {state}, {zip_code}')

# TODO: Write code to print the URL of the website of Four Barrel Coffee.
print(restaurant['url'])


print()

print("Question 2")

# TODO: Choose 3 of your most favourite restaurants in NYC, and create a dictionary for each of them with the following key-value pairs:
#         1. name : name of the resturant (string)
#         2. address: address of the restaurant (string)
#         3. favourite_dish: your favourite thing to order at the restaurant (string)

devils_alley={'name': 'Devils Alley Bar and Grill',
    'address': '1907 Chestnut Ave, Philadelphia, PA 19103',
    'favorite_dish': 'Jerk chicken tacos'
}

vernik={'name': 'Vernik Food and Drink',
    'address': '2031 Walnut St., Philadelphia, PA, 19103',
    'favorite_dish': 'Arctic char crudo'
}

green_eggs={'name': 'Green Eggs Cafe',
    'address': '212 S 13th St., Philadelphia, PA, 19107',
    'favorite_dish': 'Short rib benedict'
}
# TODO: Print each dictionary
print(devils_alley)
print(vernik)
print(green_eggs)

# The dictionary for each restaurant should look something like this

'''
restaurant_1  = {
    "name": "Subway",
    "address" : "116th & Broadway, NY 10016",
    "favourite_dish" : "Chicken BLT Sandwich"
}
'''

print()

print("Question 3")
'''
Imagine that any 1 of your most favourite restaurants stopped serving your favourite dish there.
Remove the 'favourite_dish' key value pair from that restaurant's dictionary
'''

# TODO: Remove the 'favourite_dish' key-value pair from one of your 3 restaurants
# TODO: Print the new dictionary. The new dictionary should only contain 'name' and 'address' for that restaurant
devils_alley.pop('favorite_dish')
print(devils_alley)
print()

print("Question 4")
'''
Imagine that another one of your most favourite restaurants modified its address.
Update just this value in that restaurant's dictionary
'''

# TODO: Update the address field of 1 restaurant
green_eggs["address"]='33 S 18th St., Philadelphia, PA, 19103'
# TODO: Print the new address of the restaurant by accessing that field of the restaurant's dictionary
print(green_eggs["address"])
# TODO: Print the updated dictionary.
print(green_eggs)

print()


print("Question 5")
'''
Printing out all 3 of our restaurants every time is getting annoying. Let's clean up our code!
'''

# TODO: Put your 3 restaurant dictionaries into a list called `restaurants`
restaurants=[devils_alley, vernik, green_eggs]
# TODO: Loop through your list and print out the name and address of each restaurant
for info in restaurants:
    print(info['name'])
    print(info['address'])