import random
import hangman_words
import hangman_art
# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py - DONE
chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)
lives = 6

# TODO-3: - Import the logo from hangman_art.py and print it at the start of the game. - DONE
print(hangman_art.logo)
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []
selected_letters = [" ", ""]
while not game_over:

    # TODO-6: - Update the code below to tell the user how many lives they have left.
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    # TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know. - DONE
    display = " "
    if guess in selected_letters:
        print("You've already guessed that letter.")
        print(placeholder)
        # correct_letters.append(guess) - Disabled this
        continue
        # FIRST USE OF CONTINUE CORRECTLY?
        # This is screwing up around here. It keeps jumping to win because display is set to " ". now it's counting down
        # if the same wrong letter is slected
        # Also not sure why correct_letters.append(guess) above..disabling?

    else:
        for letter in chosen_word:
            if letter == guess:
                display += letter
                correct_letters.append(guess)
            elif letter in correct_letters:
                display += letter
            else:
                display += "_"
    selected_letters.append(guess)
    print("Word to guess: " + display)

    # TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
    #  e.g. You guessed d, that's not in the word. You lose a life.

    if guess not in chosen_word and selected_letters:
        lives -= 1
        print(f"You guessed {guess}. That's not in the word, you lose a life.")
        selected_letters.append(guess)


        if lives == 0:
            game_over = True

            # TODO 7: - Update the print statement below to give the user the correct word they were trying to guess.
            print(f"***********************YOU LOSE**********************")
            print(f"The word was: {chosen_word}")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    # TODO-2: - Update the code below to use the stages List from the file hangman_art.py - DONE
    print(hangman_art.stages[lives])

