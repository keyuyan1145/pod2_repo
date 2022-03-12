hello_world = 'Hello, world!'

# print variable
print(hello_world)

# print each letter
for letter in hello_world:
    print(letter)

# Print each word
for word in hello_world.split():
    print(word)

# print backward
for word in hello_world.split():
    print(word[::-1])

# print vowels
vowels = ['a','e','i','o','u']
for vowel in hello_world:
    if vowel in vowels:
        print(vowel)