import time
import random

options = ("rock","paper","scissors")

print("lets play Rock, Paper, Scissors!")
time.sleep(1)
quit = False
end = False
score  = 0
round = 1

def check_win(player,enemy):
  if player == "rock":
    if enemy == "rock":
      return "draw"
    elif enemy == "paper":
      return "loss"
    else:
      return "win"
  if player == "paper":
    if enemy == "rock":
      return "win"
    elif enemy == "paper":
      return "draw"
    else:
      return "loss"
  if player == "scissors":
    if enemy == "rock":
      return "loss"
    elif enemy == "paper":
      return "win"
    else:
      return "draw"
    
while True:
  while True:
    weapon = input("pick your weapon: ").lower()
    if (weapon == "q"):
      quit = True
      break
    elif (not weapon in options):
      print("Please choose a valid weapon!")
      time.sleep(1)
      continue
    else:
      break

  if (quit == True):
    break

  for i in range(3,0,-1):
    print(i)
    time.sleep(1)
  print("Fight!")
  time.sleep(1)
  enemy_weapon = random.choice(options)
  print(f"you selected {weapon}, your enemy selected {enemy_weapon}")
  time.sleep(1)
  if check_win(weapon,enemy_weapon) == "win":
    print("You win!")
    score += 1
  elif check_win(weapon,enemy_weapon) == "loss":
    print("You lose!")  
  else:
    print("It's a draw!")
    score += 0.5
  time.sleep(1)
  print(f"score: {score}/{round}")

  while True:
    response = input("Play again? (y/n): ")  
    if response == "q":
      quit = True
      break
    elif not response == "y" and not response == "n":
      print("Please answer y or n")
      continue
    elif response == "n":
      end = True
    break

  if quit == True:
    break

  if end == True:
    print("---------- Game Summary ----------")
    time.sleep(1)
    print(f"Total Games: {round}")
    time.sleep(1)
    print(f"Total Wins: {score}")
    time.sleep(1)
    print(f"Total Losses: {round - score}")
    time.sleep(1)
    percentage = (score/round)*100
    print(f"Percentage: {percentage:.2f}%")
    if (percentage == 0.0):
      print("it is almost statistically impossible to be this bad!")
    elif (percentage < 25.0):
      print("You are a loser!")
    elif (percentage <50.0):
      print("Better luck next time!")
    elif (percentage <75.0):
      print("Well done!")
    else:
      print("The cheating police have been called, you are going to cheating jail!")
    break
  round += 1