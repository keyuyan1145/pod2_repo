
# what is a function
# a block of code
# can take in data/content
# it does something to that data/content
# it pops that altered data out

# define our function
def multiply(a, b): # take in data
#   multiplied_number = a * b # do something to that data
#   return multiplied_number

    def calculate_exponent(base, exponent):
        result = 1  # 10

        for i in range(exponent):
             result = result * base # 1st time through loop: 1 * 10 == 10
                               # 2nd time through loop: 10 * 10 == 100
                               # 3rd time through loop: 100 * 10 == 1000
        return result

    num_10 = calculate_exponent(10, 3)
    num_2 = calculate_exponent(2, 4)
    num_3 = calculate_exponent(3, 5)

# print(multiply(5, 6))  # 30



def get_user_num():
    num = input('please enter a number: ')

    try:
        int_num = int(num)
    except ValueError:
        print('that was not a valid number. please try again.')




    print(f'the number you input is {int_num}.')
    print(f'{int_num} * 5 is {int_num * 5}')

get_user_num()


