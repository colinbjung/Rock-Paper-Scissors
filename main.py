# Author: Colin 
# Python text-based rock paper scissors game 

import random
from art import logo
import os


def clear_console(): return os.system('clear')



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

print(logo)
#Function takes in and displays both the player and computer's choice, and then determines the winner


def rockpaperscissors():
  #utilize random feature of python to determine the computer's choice
  compchoice = random.randint(0, 2)
  #prompt the user for input to determine their choice
  playerchoice = input("Choose 1 for rock, 2 for paper, and 3 for scissors: ")
  while playerchoice != '1' and playerchoice != '2' and playerchoice != '3':
    playerchoice = (input("Invalid Input; Try Again. Choose 1 for rock, 2 for paper, and 3 for scissors: "))
  playerchoice = int(playerchoice)
  playerchoice -= 1
  #list1 contains the visual representations of rock, paper, and scissors
  list1 = [rock, paper, scissors]
  #list2 contains the 'labels' for rock, paper, and scissors
  list2 = ["rock", "paper", "scissors"]
  #incorporate the data from list1 and list2 to properly display the player and     computer's choice and corresponding visual representation
  print(f"Player chose: {list2[playerchoice]}\n{list1[playerchoice]}")
  print(f"Computer chose: {list2[compchoice]}\n{list1[compchoice]}")
  #use the numerical values assigned to rock, paper, and scissors to determine whether the player won, lost, or drew against the computer
  if (playerchoice == compchoice):
    print("Draw")
  elif (playerchoice == 0 and compchoice == 2) or (playerchoice == 1 and compchoice == 0) or (playerchoice == 2 and compchoice == 1):
    #based on the outcome, print the proper statement to the player
    print("You win")
  else:
    print("You lose")
  
#allows users to play as many times as they want
playAgain = True
while playAgain:
  rockpaperscissors()
  keepPlaying = input("Would you like to play again? (Y)es or (N)o: ")
  if keepPlaying == 'N':
    playAgain = False
  elif keepPlaying == 'Y':
    playAgain = True
  clear_console()
    

