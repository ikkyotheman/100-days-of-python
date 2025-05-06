# Range function with For Loop
# Gauss Challenge
# new_number = 0
# for number in range(1, 101):
#     new_number += number
# print(new_number)

# FizzBuzz Challenge
for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
