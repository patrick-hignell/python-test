def is_valid_decimal(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

input_sum = input("what math problem would you like me to solve?: ").replace(" ", "")

char_list = list(input_sum)
num_count = 0
string_list = [""]
print(char_list)

for i in range(len(char_list)):
  if (char_list[i].isnumeric()):
    string_list[len(string_list) -1] += char_list[i]
  else:
    string_list.append(char_list[i])
    string_list.append("")

print(string_list)

error = ""
list_length = len(string_list)
skip = False

while (len(string_list) > 1):
  skip = False

  for i in range(len(string_list)):
    if string_list[i] == "/":
      if i <= 0 or i >= len(string_list)-1:
        error = "/ at start or end!"
        break
      if not is_valid_decimal(string_list[i-1]) or not is_valid_decimal(string_list[i+1]):
        error = f"{string_list[i-1]} or {string_list[i+1]} is not numeric!"
        break
      string_list[i-1] = float(string_list[i-1]) / float(string_list[i+1])
      string_list.pop(i)
      string_list.pop(i)
      skip = True
      break
  if skip:
    print(string_list)
    continue

  for i in range(len(string_list)):
    if string_list[i] == "*":
      if i <= 0 or i >= len(string_list)-1:
        error = "* at start or end!"
        break
      if not is_valid_decimal(string_list[i-1]) or not is_valid_decimal(string_list[i+1]):
        error = f"{string_list[i-1]} or {string_list[i+1]} is not numeric!"
        break
      string_list[i-1] = float(string_list[i-1]) * float(string_list[i+1])
      string_list.pop(i)
      string_list.pop(i)
      skip = True
      break
  if skip:
    print(string_list)
    continue

  for i in range(len(string_list)):
    if string_list[i] == "+":
      if i <= 0 or i >= len(string_list)-1:
        error = "+ at start or end!"
        break
      if not is_valid_decimal(string_list[i-1]) or not is_valid_decimal(string_list[i+1]):
        error = f"{string_list[i-1]} or {string_list[i+1]} is not numeric!"
        break
      string_list[i-1] = float(string_list[i-1]) + float(string_list[i+1])
      string_list.pop(i)
      string_list.pop(i)
      skip = True
      break
  if skip:
    print(string_list)
    continue

  for i in range(len(string_list)):
    if string_list[i] == "-":
      if i <= 0 or i >= len(string_list)-1:
        error = "- at start or end!"
        break
      if not is_valid_decimal(string_list[i-1]) or not is_valid_decimal(string_list[i+1]):
        error = f"{string_list[i-1]} or {string_list[i+1]} is not numeric!"
        break
      string_list[i-1] = float(string_list[i-1]) - float(string_list[i+1])
      string_list.pop(i)
      string_list.pop(i)
      skip = True
      break
  if skip:
    print(string_list)
    continue
    
  if len(string_list) == list_length:
    error = "list length has not changed!"
    break
  else:
    list_length = len(string_list)

print(string_list)
if not error == "":
  print(error)
else:
  print(string_list[0])