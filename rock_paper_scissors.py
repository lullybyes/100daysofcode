import random

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

#Write your code below this line 👇
game_images = [rock, paper, scissors]
player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if player >= 3 or player < 0:
  print("You typed an invalid number, you lose!")
else:
  print(game_images[player])

  computer = random.randint(0,2)
  print(f"The computer chose:")
  print(game_images[computer])
  
  if player == computer:
    print("It's a draw")
  elif (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player == 2 and computer == 1):
    print("You win")
  else:
    print("You lose")
