import random
import string

print("\nWelcome to password generator!\n")
letters = list(string.ascii_letters)
numbers = list(string.digits)
symbols = ['!','#','$','%','&','(',')','*','+']

# nr_letter = input("How many letters would you like in your password?: ")
# nr_symbols = input("How many symbols would you like?: ")
# nr_numbers = input("How many numbers?: ")


# user_input = [nr_letter, nr_symbols, nr_numbers]
user_input = [random.randint(8,10), random.randint(2,4),
              random.randint(2,4)]
values_for_pass = {"letters":letters,
                   "symbols":symbols,
                   "numbers":numbers}
pass_sorted = []
for index, key in zip(user_input,values_for_pass):
    for _ in range(int(index)):
        pass_sorted.append(random.choice(values_for_pass[key]))
random.shuffle(pass_sorted)
pass_str = "".join(pass_sorted)
print(pass_str)
    

    
    
