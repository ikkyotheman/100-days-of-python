
# def greet_with_name(name):
#     print(f"Hello {name}")
#     print("Welcome")
#     print(f"How are you {name}?")
#
# greet_with_name("Kevin")
#

def life_in_weeks(age):
    weeks = (age - 90) * 52
    print(f"you have {weeks} weeks left.")
age = int(input("How old are you?"))
life_in_weeks(age)