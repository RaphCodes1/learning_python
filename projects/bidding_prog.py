import random

logo = """
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-'''---------'' '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
"""
print(logo)
print("\n\nWelcome to bidding wars!\n")
game_end = 1
bidders = {}
while(game_end == 1):
    check_input = 1
    name = input("What is your name?: ")
    dollar_amount = int(input("What is your bid?: $"))
    bidders[name] = dollar_amount 
    while(check_input == 1):
        check = input("Are there other bidders? type \"yes\" or \"no\"\n")
        if(check == "no"):
            game_end = 0
            check_input = 0
        elif(check == "yes"):
            print("\n" * 100)
            print(logo)
            check_input = 0
        else:
            print("\033[31mEnter valid input\033[0m")

highest_bidder = ""
amount = 0
for i in bidders:
    if(bidders[i] >= amount):
        amount = bidders[i]
        highest_bidder = i
print(f"\033[33m{logo}\033[0m")
print(f"\033[33mCongratulations {highest_bidder}!\nYour ${bidders[highest_bidder]} bid won!\033[0m")