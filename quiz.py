import time
question_bank = [
  ["What is the principle of Starfleet's “Prime Directive”?", "a) Diplomacy and nonviolence", "b) Non-intervention", "c) Providing assistance to those in need","d) Exploration and scientific study"],
  ["USS Enterprise (NCC-1701-D) bartender Guinan (played by Whoopi Goldberg, who requested a part on the series) is a member of what long-lived species?", "a) Haakonian", "b) Denobulan", "c) El-Aurian","d) Human/Terran"],
  ["What is the name of the Klingon home world?", "a) Qo'noS", "b) Klingonia", "c) Anacreon","d) Gorkon"],
  ["Hikaru Sulu held which position for the longest period of time aboard the USS Enterprise (NCC-1701-A)?", "a) Helmsman", "b) Chief Engineer", "c) Science Officer","d) Communications Officer"],
  ["What is the name of the species that compelled Capt. James T. Kirk and Lt. Nyota Uhura to kiss (the first kiss between a white man and a black woman on a scripted U.S. TV show)?", "a) The Iconians", "b) The Platonians", "c) The Romulans","d) The Kazon"],
  ["Which of the following was not a founding species of the United Federation of Planets, a collection of governments based on universal liberty and equality?", "a) Vulcans", "b) Andorians", "c) Tellarites","d) Betazoids"],
  ["Who was the disgraced scientist who created Lt. Cmdr Data, an android who was ultimately granted rights and privileges equal to those afforded to all humanoid species?", "a) Julian Bashir", "b) Noonien Soong", "c) Tolian Soran","d) Ma'Bor Jetrel"],
  ["What was Seven of Nine's given first name, before she was forcefully assimilated by the cybernetic pseudo-species the Borg?", "a) Alice", "b) Annika", "c) Maria","d) Deanna"],
  ["What is the purpose of the Vulcan ritual of Kolinahr?", "a) A purging of emotion", "b) The temporary union of two minds", "c) Sexual release and mating","d) The transfer of one's consciousness into the body of another"],
  ["What is the name of the alien who killed Lt. Tasha Yar (played by Denise Crosby, who chose to leave the Next Generation series after its first season)?", "a) Locutus", "b) Armus", "c) Nagilum" ,"d) Khan"],
  ["What title was given by the Bajorans to Capt. Benjamin Sisko (played by Avery Brooks, the first African-American captain to lead a Star Trek series)?", "a) The Emissary", "b) The Prophet", "c) The Messiah","d) The Minister"],
]

answers = [
  "b",
  "c",
  "a",
  "a",
  "b",
  "d",
  "b",
  "b",
  "a",
  "b",
  "a"
]

def answer_index(letter):
          if letter == "a":
            return 1
          if letter == "b":
            return 2
          if letter == "c":
            return 3
          if letter == "d":
            return 4
          return "error"

score = 0
quit = False

while True:
  print('Welcome to the Star Trek Quiz! (enter "q" to quit at any time)')
  for i in range(len(question_bank)):
    time.sleep(1)
    print(f"Question {i+1}")
    time.sleep(1)
    for item in question_bank[i]:
      print(item)
      time.sleep(1)
    while True:
      answer = input("Answer: ").lower()
      if answer == "q":
        quit = True
        break
      if not answer == "a" and not answer == "b" and not answer == "c" and not answer == "d":
        print("Please answer with a,b,c or d")
        continue
      else:
        time.sleep(1)
        if answer == answers[i]:
          print("Correct!")
          score += 1
          break
        else:
          print("Incorrect!")
          print(f"The correct answer is {question_bank[i][answer_index(answers[i])]}")
          break
    if quit:
        break
    time.sleep(1)
    print(f"Current score: {score}/{i+1}")
  if quit:
     break
  time.sleep(2)
  print("Quiz complete!")
  time.sleep(1)
  print(f"Your final score is: {score}/{len(question_bank)}")
  time.sleep(1)
  if (score == 0):
    print("Oh dear, you are an idiot!")
  elif (score / len(question_bank) < 0.25):
    print("That was pretty bad!")
  elif (score / len(question_bank) < 0.5):
    print("Better luck next time!")
  elif (score / len(question_bank) < 0.75):
    print("Well Done!")
  elif (score / len(question_bank) < 1):
     print("You are a Star Trek Officionado!")
  else:
     print("Nerd.")
  time.sleep(2)
  break
