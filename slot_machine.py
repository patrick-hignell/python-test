import time
import random

#low- 🍒🍋🍇🍉

#medium- 🔔❤️

#high- 💎

def ast(): print("****************")

def payout(multiplier, bet):
  return multiplier * bet * 28

def is_valid_decimal(s):
    try:
        float(s)
        if float(s) <= 0:
           return False
        elif not "." in s:
           return True
        else:
           if len(s.split(".")[1]) > 2:
              return False
           else:
              return True
    except ValueError:
        return False
    
def is_valid_integer(s):
    try:
        int(s)
        if int(s) <= 0:
           return False
        else:
          return True
    except ValueError:
        return False
    
def menu():
   while True:
    ast()
    print("Main Menu")
    print("1. Add to balance")
    print("2. Spin")
    print("3. Spin Simulator")
    print("4. Exit")
    response = input("Please select an option (1-4): ").lower()
    ast()
    if not response == "1" and not response == "2" and not response == "3" and not response == "4":
       print("Please enter a valid option")
       continue
    else:
       return response

def deposit():
  while True:
    response = input("How much money do you want to add to your balance?: ")
    ast()
    if not is_valid_decimal(response):
      print("Please enter a valid amount")
      continue
    else:
       return float(response)

def spin(balance):
  icons = [
    {"icon":"🍒", "value":1},
    {"icon":"🍋", "value":1},
    {"icon":"🍇", "value":1},
    {"icon":"🍉", "value":1},
    {"icon":"🔔", "value":2},
    {"icon":"❤️", "value":2},
    {"icon":"💎", "value":3}
  ]

  first_spin = True

  while True:
      if balance == 0:
        print("You have no money. Please add to your balance")
        return balance
      
      response = "y" if first_spin else input("Do you want to spin again? (Y/N): ").lower()
      first_spin = False
      if not response == "y" and not response == "n":
        print("Please enter a valid response")
        continue
      elif response == "n":
        return balance
      else:
        while True:
          print(f"Current balance: ${balance:.2f}")
          response = input("Place your bet amount: ")
          if not is_valid_decimal(response):
            print("Please enter a valid amount")
            continue
          elif balance - float(response) < 0:
            print("You do not have the funds for that bet")
            continue
          else:
            icon1 = random.choice(icons)
            icon2 = random.choice(icons)
            icon3 = random.choice(icons)
            print("Spinning...")
            ast()
            time.sleep(1)
            print(icon1["icon"], end="")
            print("  |  ", end="")
            time.sleep(1)
            print(icon2["icon"], end="")
            print("  |  ", end="")
            time.sleep(1)
            print(icon3["icon"])
            ast()
            time.sleep(1)

            if (icon1 == icon2 and icon1 == icon3):
              print(f"Congratulations! You have won ${payout(icon1["value"],float(response)):.2f}!")
              balance += payout(icon1["value"],float(response))
              break
            else:
              print("Sorry you lost this round")
              balance -= float(response)
              break
            
def spin_simulator():
  icons = [
    {"icon":"🍒", "value":1},
    {"icon":"🍋", "value":1},
    {"icon":"🍇", "value":1},
    {"icon":"🍉", "value":1},
    {"icon":"🔔", "value":2},
    {"icon":"❤️", "value":2},
    {"icon":"💎", "value":3}
  ]
  while True:
    balance_response = input("What is the initial balance?: ")
    if not is_valid_decimal(balance_response):
      print("Please enter a valid decimal")
      continue
    else:
      break
    
  while True:
    spin_response = input("How many spins do you want to simulate?: ")
    if not is_valid_integer(spin_response):
      print("Please enter a valid integer")
      continue
    else:
      break

  while True:
    value_response = input("How much do you want to bet?: ")
    if not is_valid_decimal(value_response):
      print("Please enter a valid decimal")
      continue
    else:
      break

  balance_response = float(balance_response)
  spin_response = int(spin_response)
  value_response = float(value_response)

  for i in range(spin_response):
    icon1 = random.choice(icons)
    icon2 = random.choice(icons)
    icon3 = random.choice(icons)
    ast()
    print(icon1["icon"], end="")
    print("  |  ", end="")
    print(icon2["icon"], end="")
    print("  |  ", end="")
    if (icon1 == icon2 and icon1 == icon3):
        balance_response += payout(icon1["value"],float(value_response))
        print(f"{icon3["icon"]}    Congratulations! You have won ${payout(icon1["value"],float(value_response)):.2f}!")
    else:
      print(icon3["icon"])
      balance_response -= float(value_response)
  
  ast()
  print(f"final balance is ${balance_response:.2f}")
        




def main():
  ast()
  print("Welcome to Python Slots")
  print("Symbols: 🍒 🍋 🍇 🍉 🔔 ❤️ 💎")
  ast()

  balance = 0

  while True:
    print(f"Current balance: ${balance:.2f}")
    menu_response = menu()
    if menu_response == "1":
       balance += deposit()
    elif menu_response == "2":
      balance = spin(balance)
    elif menu_response == "3":
      spin_simulator()
    else:
      print(f"Thankyou for playing! Your final balance is ${balance:.2f}")
      ast()
      break    


if __name__ == '__main__':
 main()


