import random
import time

word_list = ("art","basin","writing","representative","feeling","spark","seat","babies","sponge","key","news","can","toad","health","mitten","way","button","spark","beginner","scissors","attraction","approval","territory","range","decision","wren","letters","wound","tomatoes","pump","dinosaurs","shake","gold","drain","pest","chance","toy","downtown","join","light","crook","direction","stew","children","skate","branch","shoe","statement","insurance")
random_word = random.choice(word_list)
letter_list = ()
all_letter_guesses = ()
# print(random_word)

guesses = 0
win = False
quit = False

print("Welcome to Word Guesser!")
time.sleep(1)
print('Type "quit" to quit at any time')
time.sleep(1)
while True:
  while True:
    reply = input("Would you like to guess either: 1. a word or 2. a letter? ").lower()
    if reply == "quit":
      quit = True
      break
    elif "1" in reply or "word" in reply:
      guesses += 1
      guess = input("What is your guess?: ").lower()
      if guess == "quit":
        quit = True
        break
      elif guess == random_word:
        win = True
        break
      else:
        print("Incorrect guess")
        time.sleep(1)
        print(f"Total guesses: {guesses}")
        continue
    elif "2" in reply or "letter" in reply:
      guesses += 1
      while True:
        guess = input("What is your guess?: ").lower()
        if guess == "quit":
          quit = True
          break
        elif not len(guess) == 1:
          print("Please guess a single letter")
          continue
        elif guess in all_letter_guesses:
          print("You have already guessed that!")
          continue
        elif guess in random_word:
          print(f"Correct! The word contains the letter {guess.upper()}")
          letter_list = letter_list + (guess, ) if guess not in letter_list else ""
          all_letter_guesses = all_letter_guesses + (guess, ) if guess not in all_letter_guesses else ""
          break
        else:
          print("Incorrect guess")
          all_letter_guesses = all_letter_guesses + (guess, ) if guess not in all_letter_guesses else ""
          break
    else:
      print("Incorrect input")
      continue
    
    break
  if quit == True or win == True:
    break

  time.sleep(1)
  print(f"Next Guess. You have made {guesses} guess{"es" if not len(letter_list) == 1 else ""} so far")
  if len(letter_list) > 0:
    time.sleep(1)
    print(f"Remember, the word contains the letter{"s" if len(letter_list) > 1 else ""} {", ".join(map(str.upper, letter_list[:-1]))}{" and " if len(letter_list) > 1 else ""}{letter_list[-1].upper()}")
  time.sleep(1)
      
if win == True:
  print(f"Congrats! you correctly guessed that the word was {random_word.upper()} in {guesses} guess{"es" if not guesses == 1 else ""}")
elif quit == True:
  print(f"You gave up after {guesses} guess{"es" if not guesses == 1 else ""}")
  time.sleep(1)
  print(f"The word was {random_word.upper()}")
else:
  print("How did you get here?! Something's gone wrong!")