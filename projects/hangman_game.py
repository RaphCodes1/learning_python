import random

hangman_words = [
    "python", "elephant", "guitar", "butterfly", "computer", "sunflower",
    "adventure", "chocolate", "mountain", "keyboard", "notebook", "rainbow",
    "strawberry", "fireworks", "moonlight", "pineapple", "spaceship", "tornado",
    "treasure", "volcano", "whisper", "zebra", "penguin", "jellyfish",
    "parachute", "watermelon", "happiness", "champion", "mystery", "ocean"
]

hangman_logo = """
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _' | '_ \ / _' | '_ ' _ \ / _' | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/
"""

stage_1 = """ 
+---+
  |   |
  O   |
      |
      |
      |
=========
"""

stage_2 = """
+---+
  |   |
  O   |
  |   |
      |
      |
=========
"""

stage_3 = """
+---+
  |   |
  O   |
 /|   |
      |
      |
=========
"""

stage_4 = """
+---+
  |   |
  O   |
 /|\  |
      |
      |
=========
"""

stage_5 = """
+---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
"""

stage_6 = """
+---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
"""

hangman_modes = [stage_1, stage_2, stage_3, stage_4, stage_5, stage_6]

def letter_check(word_picked, in_letters):
    for i in range(0, len(word_picked)):
        if(in_letters == word_picked[i]):
            return (1)
    return (0)

def replace_letters(in_letters, word_guess, word_picked):
    for i in range(0, len(word_picked)):
        if(in_letters == word_picked[i]):
            word_guess[i] = in_letters


print("Welcome to\n")
print(f"{hangman_logo}")

lives = 6
word_picked = random.choice(hangman_words)
word_guess = ["_"]
you_won = 0
for i in range(len(word_picked) - 1):
    word_guess.append ("_")

# print(f"the word: {word_picked}")
while not lives == 0:
    print(f"word to guess: {''.join(word_guess)}")
    in_letters = input("guess a letter: ")
    if letter_check(word_picked, in_letters):
        print(f"{in_letters} is correct!")
        replace_letters(in_letters, word_guess, word_picked)
    else:
        print(f"{in_letters} is wrong!")
        lives -= 1
        print(f"{hangman_modes[(lives + 1) * -1]}")
        print(f"****************************{lives}/6 LIVES LEFT****************************")
    checker_conv = ''.join(word_guess)
    if word_picked == checker_conv:
        you_won = 1
        break 

if you_won == 1:
    print("\033[33mCongratulations! You Won!\033[0m")
    print(f"\033[33mWord is {''.join(word_guess)}\033[0m")
else:
    print("\033[31mGame Over!\033[0m")
    print(f"\033[31mWord is {word_picked}\033[0m")
    
