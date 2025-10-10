import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
#My original version that worked was for position in chosen_word:  which yielded the same results.
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

# TODO-1: - Use a while loop to let the user guess again.
display = ""
while chosen_word != display:
    guess = input("Guess a letter: ").lower()



# TODO-2: Change the for loop so that you keep the previous correct letters in display.

    for letter in chosen_word:
        if letter == guess:
           display += letter
        else:
           display += "_"
    print(display)
