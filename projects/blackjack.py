import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
'-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      '------'                           |__/  

"""

def hit(deck):
    
    ran_2 = random.choice(deck[1])
    return ran_2

def check_hand_sum(hand, player):
    sum = 0
    for i in range(0,len(hand[player])):
        sum += hand[player][i]
    return sum

def result_after_cpu(hand):
    if(check_hand_sum(hand,"cpu") > 21):
        print("\033[33mPlayer wins! :D\033[0m" + "\n\033[31mComputer went over! \033[0m")
        return 
    if(check_hand_sum(hand,"player") > check_hand_sum(hand,"cpu")):
        print("\033[33mPlayer Wins!\033[0m")
    elif(check_hand_sum(hand,"player") == check_hand_sum(hand,"cpu")):
        print("\033[35mIts a tie!\033[0m")
    else:
        print("\033[34mComputer Wins!\033[0m")

def cpu_gets_cards(hand, deck):
    res = 0
    hand["cpu"].append(hit(deck))
    if (check_hand_sum(hand,"player") == 21 and check_hand_sum(hand,"cpu") == 21):
        print("\033[35mTwo Blackjacks! Its a tie!\033[0m")
    if(check_hand_sum(hand,"cpu") == 21):
        print("\033[34mBlackjack for Computer!\033[0m")
        res = 1
        return res
    if check_hand_sum(hand,"cpu") <= 16:
        hand["cpu"].append(hit(deck))
        while(check_hand_sum(hand,"cpu") <= 16):
            hand["cpu"].append(hit(deck))
    return res

def print_status(hand, mode):
    if(mode == 1):
        print("   Your cards: " + str(hand["player"]) + " current score: " + str(check_hand_sum(hand,"player")))
        print("   Computer cards: " + str(hand["cpu"]))
    elif(mode == 2):
        print("   Your cards: " + str(hand["player"]) + " current score: " + str(check_hand_sum(hand,"player")))
        print("   Computer cards: " + str(hand["cpu"]) + " current score: " + str(check_hand_sum(hand,"cpu")))

def blackjack():
    print(logo)
    print("\nWelcome to Blackjack!\n")
    deck = {
        1: [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11],
    }
    hand = {
        "player": [],
        "cpu": []
    }
    hand["player"].append(hit(deck))
    hand["player"].append(hit(deck))
    hand["cpu"].append(hit(deck))
    if check_hand_sum(hand,"player") == 21:
        print("\033[33mBlackjack for player!\033[0m")
        return 
    print_status(hand,1)
    while(1):
        if(check_hand_sum(hand,"player") > 21):
            print("\n\033[33mComputer wins!\033[0m" + "\n\033[31mPlayer went over :( \033[0m")
            break
        get_card_pl = input("Type 'y' to get another card, type 'n' to pass: ")
        if get_card_pl == "y":
            hand["player"].append(hit(deck))
            print_status(hand,1)
        elif get_card_pl == "n":
            if(cpu_gets_cards(hand, deck)):
                print_status(hand,2)
                break
            print_status(hand,2)
            result_after_cpu(hand)
            break
        else:
            print("\033[31m enter valid character\033[0m")
            continue


intro = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
while (1):
    if intro == "y":
        blackjack()
        play_again = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
        if play_again == 'y':
            continue
        else:
            print("\n\033[33mThank you for playing blackjack\033[0m\n")
            break
    elif intro == "n":
        print("\n\033[33mThank you for playing blackjack\033[0m\n")
        break
    else:
        print("\033[31mEnter valid character\033[0m")
        intro = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

    
    
