def ast():
  print("*********************")

def is_valid_decimal(s):
  try:
      float(s)
      return True
  except ValueError:
      return False
  
balance = 0.00
while True:
  exit = False
  menu = False
  ast()
  print(f"Your balance is ${balance:.2f}")
  ast()
  ast()
  print("   Banking Program   ")
  ast()
  print("1.Show Balance")
  print("2.Deposit")
  print("3.Withdraw")
  print("4.Exit")

  while True:
    ast()
    response = input("Enter your choice (1-4):").lower()
    if response == "4" or response == "exit":
      exit = True
      break
    elif response == "1" or response =="show balance":
      break
    elif response == "2" or response == "deposit":
      while True:
        ast()
        deposit_response = input("How much would you like to deposit?:")
        if not is_valid_decimal(deposit_response):
          print("Please enter a valid amount")
          continue
        else:
          balance += float(deposit_response)
          menu = True
          break
    elif response == "3" or response == "withdraw":
      while True:
        ast()
        withdraw_response = input("How much would you like to withdraw?:")
        if not is_valid_decimal(withdraw_response):
          print("Please enter a valid amount")
          continue
        elif balance - float(withdraw_response) < 0:
          print("You do not have the funds to withdraw that amount")
          break
        else:
          balance -= float(withdraw_response)
          menu = True
          break
    else:
      ast()
      print("Please enter a valid choice")
    
    if menu:
      break

  if exit:
    break
