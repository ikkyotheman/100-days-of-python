rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]
import random
random_int = random.randint(0,2)
your_hand = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
if your_hand >= 0 and your_hand <=2:
    print(game_images[your_hand])
print("Computer chose:")
print(game_images [random_int])
if your_hand == random_int:
    print("It's a draw!")
if (your_hand == 0 and random_int == 1) or (your_hand == 1 and random_int == 2) or (your_hand == 2 and random_int == 0):
    print("You Lose")
elif (your_hand == 0 and random_int == 2) or (your_hand == 1 and random_int == 0) or (your_hand == 2 and random_int == 1):
        print("You win")
elif your_hand > 2:
    print("You Typed an invalid number, you lose")
