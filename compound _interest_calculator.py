# compound interest calculator

principle = 0
rate = 0
time = 0

while True:
  try:
    principle = float(input("Enter the principle amount: "))
  except:
    print ("Amount must be a number")
    continue
  if principle < 0:
    print ("principle can't be less than zero")
  else:
    break

while True:
  try:
    rate = float(input("Enter the rate amount: "))
  except:
    print ("Amount must be a number")
    continue
  if rate < 0:
    print ("rate can't be less than zero")
  else:
    break

while True:
  try:
    time = float(input("Enter the time amount: "))
  except:
    print ("Amount must be a number")
    continue
  if time < 0:
    print ("time can't be less than zero")
  else:
    break

total = principle * pow((1+ rate / 100), time)

print (f"Balance after {time:g} year/s: ${total:.2f}")