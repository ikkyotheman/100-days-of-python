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
your_hand = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors"))
if your_hand == 0:
    print(rock)
if your_hand == 1:
    print(paper)
if your_hand == 2:
    print(scissors)
import random
random_int = random.randint(0,2)
if random_int == 0:
    print(f"Computer chose: {rock}")
if random_int == 1:
    print(f"Computer chose: {paper}")
if random_int == 2:
    print(f"Computer chose: {scissors}")
if your_hand == random_int:
    print("Tie")
if (your_hand == 0 and random_int == 1) or (your_hand == 1 and random_int == 2) or (your_hand == 2 and random_int == 0):
    print("You Lose")
if (your_hand == 0 and random_int == 2) or (your_hand == 1 and random_int == 0) or (your_hand == 2 and random_int == 1):
    print("You win")
