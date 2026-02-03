width = input("width: ")
height = input("height: ")

def generate_rectangle(w, h):
  try:
    w = int(w)
  except:
    return "width is not a valid integer"
  try:
    h = int(h)
  except:
    return "height is not a valid integer"
  for i in range(h):
    for j in range(w):
      print("\u25A0",end="")
    print("")
  return "your rectangle is complete!"

print(generate_rectangle(width, height))