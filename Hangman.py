import random

# from random_words import eaeasy_wordlist, medium_wordlist, hard_wordlist
def making_a_guess():
    x = 0
    global update_display
    correct_guess = False
    for letter in chosen_word:
        if guess.lower() == chosen_word[x]:
            blank_list[x] = guess.lower()
            correct_guess = True
        x += 1
    if correct_guess == False:
        print(f"There is no {guess}, sorry.")
        update_display += 1
    x = 0
 
 
HANGMANPICS = ['''
  +---+                 # initial state
  |   |
      |
      |
      |
      |
=========''', '''
  +---+             # head
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+         # head and torso    
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |       # head, torso, and one arm
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |     # head, torso, and both arms
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |         # head, torso, both arms, and one leg
  O   |         
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |         # FINAL STATE - head, torso, both arms, and both legs
  O   |
 /|\  |
 / \  |
      |
=========''']
 
word_list = ["aardvark", "baboon", "camel", "jazz", "grass", "follow", "castle", "cloud"]
 
chosen_word = list(random.choice(word_list))
 
blank = ""
for letter in chosen_word:
    blank += "_"
blank_list = list(blank)
 
update_display = 0
 
#----------------------------------------------------------------------------------------------
 
print(HANGMANPICS[update_display])
guess = input(f"Welcome to hangman.\n{blank}\nMake a guess? ")
making_a_guess()
print(HANGMANPICS[update_display])
print(''.join(blank_list))
while update_display < 6:
    if blank_list == chosen_word:
        print("YOU WIN!")
        break
    guess = input("Make another guess? ")
    making_a_guess()
    print(HANGMANPICS[update_display])
    print(''.join(blank_list))
if update_display == 6:
    print("GAME OVER.")
