import random

logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ' _ \| '_ \ / _ \ '__|
/ /_\\\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|    
"""
print(logo)
print("Welcome to Guess the number!")
print("I'm thinking of a number between 1 and 100.")

lives = 0
random_num = random.randint(0,100)
dif = input("Choose a difficulty. Type 'easy' or 'hard': ")
if dif == "easy":
    lives = 10
    print("You have 10 attempts remaining to guess the number.")
elif dif == "hard":
    lives = 5
    print("You have 5 attempts remaining to guess the number.")
while(1):
    guess = int(input("Make a guess: "))
    if lives == 0:
        print(f"Game over! The number is {random_num}")
        break
    if guess > random_num:
        print("Too High.")
        lives -= 1
    elif guess < random_num:
        print("Too Low.")
        lives -= 1
    else:
        print(f"You got it! The answer is {random_num}")
        break
    



