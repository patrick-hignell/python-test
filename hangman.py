import time
import random

hangman_art = {0: ("",
                   "",
                   "",
                   "",
                   ""),
              1: ("",
                   "",
                   "",
                   "",
                   "⊥    "),
              2: ( "",
                   "|   ",
                   "|   ",
                   "|   ",
                   "⊥    "),
              3: ("⌈¯¯¯",
                   "|   ",
                   "|   ",
                   "|   ",
                   "⊥    "),
              4: ("⌈¯¯¯⌉",
                   "|   ",
                   "|   ",
                   "|   ",
                   "⊥    "),
              5: ( "⌈¯¯¯⌉",
                   "|   O",
                   "|   ",
                   "|   ",
                   "⊥    "),
              6: ("⌈¯¯¯⌉",
                   "|   O",
                   "|   +",
                   "|   ",
                   "⊥    "),
              7: ("⌈¯¯¯⌉",
                   "|   O",
                   "|   +",
                   "|   ⩑",
                   "⊥    ")}


# for key in hangman_art:
#   for line in hangman_art[key]:
#     print(line)
#   time.sleep(1)



# for line in hangman_art[0]:
#   print(line)

# for line in hangman_art[1]:
#   print(line)

word_list = ("art","basin","writing","representative","feeling","spark","seat","babies","sponge","key","news","can","toad","health","mitten","way","button","spark","beginner","scissors","attraction","approval","territory","range","decision","wren","letters","wound","tomatoes","pump","dinosaurs","shake","gold","drain","pest","chance","toy","downtown","join","light","crook","direction","stew","children","skate","branch","shoe","statement","insurance")

def hangman():
  random_word = random.choice(word_list)
  hidden_word = ["_" for c in random_word]
  hidden_word = "".join(hidden_word)
  guessed_letters = list()
  # print(random_word)
  stage = 0
  while True:
    print(hidden_word)
    for line in hangman_art[stage]:
      print(line)
    if len(guessed_letters) > 0:
      print(f"Guessed letters: {",".join(guessed_letters)}")
    letter = input("Guess a letter: ")
    if not letter.isalpha() or not len(letter) == 1:
      print("Please pick a single valid letter")
      continue
    else:
      if letter in guessed_letters:
        print("you have already guessed that!")
        continue
      else:
        guessed_letters.append(letter)
        if letter not in random_word:
          stage += 1
          if stage < 7:
            print("Guess again!")
            continue
          else:
            for line in hangman_art[7]:
              print(line)
            print("Oh dang, you done got hung!")
            print(f"The word was: {random_word}")
            return False
        else:
          print("Correct!")
          for i in range(len(random_word)):
            if random_word[i] == letter:
              hidden_word = hidden_word[:i] + letter + hidden_word[i+1:]
          if "_" not in hidden_word:
            print(f"Congrats! you won!")
            print(f"The word was: {random_word}")
            return True
          else:
            continue

def main():
  best_streak = 0
  current_streak = 0
  quit = False
  first = True
  while True:
    response = input(f"would you like to play hangman{" again" if first == False else ""}? (y/n): ").lower()
    first = False
    if not response == "n" and not response == "y":
      print("Please respond y or n")
      continue
    if response == "n":
      quit = True
      break
    else:
      won = hangman()
      if won:
        current_streak += 1
        if current_streak > best_streak:
          best_streak = current_streak
      else:
        current_streak = 0
      print(f"Current streak: {current_streak}")
      print(f"Best streak: {best_streak}")
  
  if quit:
    if best_streak == 0:
      print("Better luck next time")
    else:
      print(f"Well played! your best streak was: {best_streak}")






# random_word = random.choice(word_list)
# hidden_word = ["_" for c in random_word]
# hidden_word = "".join(hidden_word)
# print(random_word)
# print(hidden_word)
# stage = 0

if __name__ == '__main__':
 main()