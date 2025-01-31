import random

rock = """
     _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
     _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

choices = [rock, paper, scissors]
print("\nWelcome to rock paper scissors game!\n")
user_choice = input("rock, paper or scissors?: ")
user_num = 0
cpu_num = random.randint(0,2)
who_won = 0
if(user_choice == "paper"):
    user_num = 1
elif(user_choice == "scissors"):
    user_num = 2
elif(user_choice == "rock"):
    user_num = 0
else:
    print("\n\033[31mInvalid Argument\033[0m\n")
    who_won = -1

if(who_won == -1):
    exit()
if(user_num == cpu_num):
    print("\n\033[33mits a tie!\033[0m\n")
    print(f"cpu:\n{choices[cpu_num]}")
    print(f"\nplayer:\n{choices[user_num]}")
    who_won = -1
elif((user_num == 0 and cpu_num == 2) or (cpu_num == 0 and user_num == 2)):
    print("\nrock wins against scissors!")
    if((cpu_num == 0 and user_num == 2)):
        who_won = 1
elif((user_num == 2 and cpu_num == 1) or (cpu_num == 2 and user_num == 1)):
    print("\nScissors wins against paper!")
    if((cpu_num == 2 and user_num == 1)):
        who_won = 1
elif((user_num == 1 and cpu_num == 0) or (cpu_num == 1 and user_num == 0)):
    print("\nPaper wins against rock!")
    if((cpu_num == 1 and user_num == 0)):
        who_won = 1

if(who_won == 1):
    print("\n\033[33mcpu wins!\033[0m\n")
    print(f"cpu:\n{choices[cpu_num]}")
    print(f"\nplayer:\n{choices[user_num]}")
elif(who_won == 0):
    print("\n\033[33mplayer wins!\033[0m\n")
    print(f"player:\n{choices[user_num]}")
    print(f"\ncpu:\n{choices[cpu_num]}")