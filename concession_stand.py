concessions = {
  "popcorn" : 1.00,
  "hot dog" : 2.00,
  "giant pretzel" : 2.00,
  "candy" : 1.00,
  "soda" : 1.00,
  "bottled water" : 1.00
}

purchases = {}

cost = 0.00

def is_int(value):
  try:
    int(value)
    return True
  except:
    return False

quit = False
summary = False

print('Welcome to the concession stand. Enter "q" to quit at any time')
for key , value in concessions.items():
  print(f"{key:15} : ${value:.2f}")

while True:
  concession  = input("What did the customer order?: ").lower()
  if concession == "q":
    break
  if not concession in concessions:
    print("Please enter a valid concession")
    continue
  else:
    while True:
      quantity = input("how many did they order? : ")
      if quantity == "q":
        quit = True
        break
      if not is_int(quantity):
        print("Please enter a valid number")
        continue
      elif int(quantity) <= 0:
        print("Please enter a number greater than 0")
        continue
      else:
        cost += concessions.get(concession) * int(quantity)
        print(f"Total: ${cost:.2f}")
        if concession in purchases:
           purchases[concession] += int(quantity)
        else:
          purchases.update({concession : int(quantity)})
        while True:
          response = input("Add another item? (y/n): ").lower()
          if response == "q":
            quit = True
            break
          elif response == "y":
            break
          elif response == "n":
            summary = True
            break
          else:
            print("Please enter y or n")
            continue
      break

    if quit == True:
      break
    if summary == True:
      print("===========================================")
      print("Summary: ")
      for key, value in purchases.items():
        print(f"{key} x {value} = ${value * concessions.get(key):.2f}")
      print(f"Total: ${cost:.2f}")
      break

