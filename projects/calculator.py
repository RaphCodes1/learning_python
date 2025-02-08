logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ '.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ '.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   '._____.'  | || ||____|  |____|| || |  |________|  | || |   '._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
def add(one,two):
    return one + two

def sub(one,two):
    return one - two

def mult(one,two):
    return one * two

def div(one,two):
    return one / two

operations = {
    "+" : add,
    "-" : sub,
    "/" : div,
    "*" : mult,
}
print(logo)
print("\nWelcome to calculator!\n")

def calc():
    end = 0
    res = int(input("1st number: "))
    while(end == 0):
        print("+ - * /")
        op = input("Pick an operation: ")
        second_num = int(input("2nd number: "))
        res = operations[op](res, second_num) 
        check = input(f"Type 'y' to continue calculating with {res}, or type 'n' to start a new calculation or 'x' for exit: ")
        if check == "x":
            end = 1
        elif check == "y":
            continue
        elif check == "n":
            calc()
    print("Thanks for using pycalc")
calc()

    
    
        

