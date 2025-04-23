import random

# random_integer = random.randint(1, 10)
# print(random_integer)
# random_number_0_to_1 = random.random() * 10
# print(random_number_0_to_1)

# random_float = random.uniform(1,10)
# print(random_float)

random_integer = random.randint(0,1)
if random_integer == 1:
    print("Heads")
else:
    print("Tails")