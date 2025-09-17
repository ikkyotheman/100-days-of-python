word_list = ["aardvark", "baboon", "camel"]
import random
chosen_word = random.choice(word_list)
print(chosen_word)
chosen_length = len(chosen_word)
guess = input("Guess a letter").lower()
for each_letter in chosen_word:
    if each_letter == guess:
        print("Right")
    else:
        print("Wrong")


# if guess == chosen_word[chosen_length-1]:
#     print("Correct!")

# You got this but confused why the string works like a list. Look that up..up hint 2 says you can do that.


# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
#  is, "Wrong" if it's not.
