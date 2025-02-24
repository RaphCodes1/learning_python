import random
import string

print("\nWelcome to password generator!\n")
letters = list(string.ascii_letters)
numbers = list(string.digits)
symbols = list(string.punctuation)

nr_letter = input("How many letters would you like in your password?: ")
nr_symbols = input("How many symbols would you like?: ")
nr_numbers = input("How many numbers?: ")

user_input = [nr_letter, nr_symbols, nr_numbers]
values_for_pass = [letters, symbols, numbers]
check_valid = 0
for i in range(0,3):
    check = 0
    len_num = 0
    while len_num < len(user_input[i]) and ('0' <= user_input[i][len_num] <= '9'):
        len_num += 1
    if(len_num == len(user_input[i])):
        check = 1
    if(check == 1):
        check_valid += 1
if not(check_valid == len(user_input)):
    print("\033[31mInvalid Args\033[0m")
    exit()
result_pass = []
loop_index = 0
for i in range(0, len(user_input)):
    loop_index += int(user_input[i])
lens = [0, 0, 0]
full = [0, 0, 0]
marked = [0 , 1 , 2]
for i in range(0, loop_index):
    which_list = random.choice(marked)
    random_num = random.randint(0, len(values_for_pass[which_list]) - 1)
    result_pass.append(values_for_pass[which_list][random_num])
    lens[which_list] += 1
    if(lens[which_list] == int(user_input[which_list]) and full[which_list] == 0):
        marked.remove(which_list)
        full[which_list] = 1
print("Your password: " + "".join(result_pass))
    

    
    
