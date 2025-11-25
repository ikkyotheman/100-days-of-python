# def format_name(f_name, l_name):
#     f_name = f_name.title()
#     l_name = l_name.title()
#     return f"{f_name} {l_name}"
# formatted_string = format_name("pEtEr", "vrTx")
# print(formatted_string)
#
#
# def function_1(text):
#     return text + text
# def function_2(text):
#     return text.title()
# output = function_2(function_1('hello'))
# print(output)

# def function(text):
#     return text + text
#
# print(function('Hello'))
"""
def function(text):  # Defines the blueprint. 'text' is the parameter (a local variable slot).
    return text + text  # Computes 'text' doubled (string concat), then returns that *value* to the caller.

# Nothing happens yet—this is just setup. The function doesn't run until called.
output = function('Hello')  # Calls the function: Passes "'Hello'" as the argument,
# which gets copied into the local 'text' param.
# Inside the function (temporarily):
#   text becomes 'Hello' (local scope).
#
# Inside the function (temporarily):
## text becomes 'Hello' (local scope).
# text + text evaluates to 'HelloHello'.
# return sends 'HelloHello' back out to this line.
#
#
# The function ends, locals vanish, and 'HelloHello' is assigned to
# output (now in the outer scope—reusable!).

"""

"""
def format_name(f_name, l_name):
    print(f_name.title(), l_name.title())
format_name('peTEr', 'kinDRAchuK')

"""
"""
def format_name(f_name, l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return (f"{formatted_f_name} {formatted_l_name}")

formatted_string = format_name('peTEr', 'kinDRAchuK') #This is how we bring the return outside of the local scope
print(formatted_string)

This code below sucked because the loop wasn't working properly. You can't loop back to reprompt for input because
f_name and l_name are fixed parameters passed from outside (via input() calls).

def format_name(f_name, l_name):
    myloop = False
    while myloop == False:
        if f_name == "" or l_name == "":
            return "You did not provide valid inputs"
        else:
            myloop = True
            formatted_f_name = f_name.title()
            formatted_l_name = l_name.title()
        return f"Result:{formatted_f_name} {formatted_l_name}"
print(format_name(input("What is your first name?"), input("What is your last name?")))

This will run the code correctly but was having trouble making it loop: 
def format_name():
    f_name = input("What is your first name? ")
    l_name = input("What is your last name? ")
    if f_name == "" or l_name == "":
        return "You did not provide valid inputs"
    else:
        formatted_f_name = f_name.title()
        formatted_l_name = l_name.title()
        return f"Result: {formatted_f_name} {formatted_l_name}"

print(format_name())
"""
def format_name():
    while True:  # Loop until valid inputs are provided
        f_name = input("What is your first name? ")
        l_name = input("What is your last name? ")
        if f_name == "" or l_name == "":
            print("You did not provide valid inputs. Please try again.")  # Print instead of return - key to stay
                                                                          # in the function instead of exiting.
        else:
            formatted_f_name = f_name.title()
            formatted_l_name = l_name.title()
            return f"Result: {formatted_f_name} {formatted_l_name}"

print(format_name())