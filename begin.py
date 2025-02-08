#day 1: printing and variables
# print("welcome to band name generator!\n")
# city = input("name of the city?: ")
# pet_name = input("what is your pet's name?: ")
# print("Your band name is " + city + " " + pet_name)

#day 2: data types and string manipulation
# print("Welcome to tip calculator!")
# total_bill = float(input("total bill: "))
# tip = int(input("Tip 10, 12, or 15?: "))
# split_bill = int(input("split the bill: "))
# bill_with_tip = round(((total_bill + round(total_bill * (tip * 0.01), 2)) / split_bill), 2)
# print(f"Each person should pay: ${bill_with_tip}") 

#day 3: conditional statements, logical operators, code blocks and scope
# print("welcome to treasure island!")
# choose_dir = input("left or right?: ")
# if choose_dir == "left":
#     path_2 = input("swim or wait: ")
#     if(path_2 == "wait"):
#         path_3 = input("which door: ")
#         if path_3 == "red" or path_3 == "blue":
#             print("\033[31mRoom exploded\033[0m")
#         elif path_3 == "yellow":
#             print("\033[33mCongrats! You Won!\033[0m")
#         else:
#             print("\033[31mThanos snapped\033[0m")
#     elif path_2 == "swim":
#         print("\033[31mYou got eaten by the sharks fam\033[0m")
#     else:
#         print("\033[31mThanos snapped\033[0m")
# elif choose_dir == "right":
#     print("\033[31mYou dead bruh\033[0m")
# else:
#     print("\033[31mThanos snapped\033[0m")

#day 4: randomization and python lists 
# import random
# friends = ["Moe", "Mike", "Maaz", "Max", "Raphael"]
# random_num = random.randint(0, len(friends) - 1)
# print(f"the lucky person paying the bill is: {random.choice(friends)}")
# list1 = ["banana", "apple", "grape", "watermelon"]
# list2 = ["cookie", "juice", "salad", "chocolate"]
# nested = [list1, list2]
# # print(f"combo is: {random.choice(nested[0])} + {random.choice(nested[1])}")
# print(f"combo is: {nested[1][-3]}")

#day 5: Python Loops for loop

# list1 = ["hello", "there", 42]
# for i in list1:
#     print(i)
#     print(type(i))

# list_num = [110, 80, 172, 54, 7, 45, 69, 66, 49, 11, 90, 132, 122, 183, 149, 14, 6, 57, 84, 63, 143, 156, 17, 186, 174, 29, 78, 157, 52, 126]

# max_num = 0
# for i in list_num:
#     if(max_num < i):
#         max_num = i
# print(max_num)

# total_sum = 0
# for i in range(1,101):
#     total_sum += i
# print(total_sum)

#day 6: python function and while loop
# def my_func(i):
#     return i + 1
# i = 0
# for loop in range(0, 10):
#     print("bruh")
#     i = my_func(i)
# print(f"result: {i}")

#day 7: hang_man project // see projects page

#day 8: functions with inputs // arguments & parameters
# def life_in_weeks(age):
#     till_90 = 90 * 52
#     print(f"You have {till_90 - (age * 52)} weeks left.")
# life_in_weeks(20)
# def calculate_love_score(name1, name2):
#     true = ['T','R','U','E']
#     love = ['L','O','V','E']
    
#     names_together = " ".join([name1,name2])
#     capitalized = names_together.upper()
    
#     calc1 = 0
#     calc2 = 0
#     for i in range(0,len(true)):
#         for f in range(0, len(capitalized)):
#             if capitalized[f] == true[i]:
#                 calc1 += 1
    
#     for i in range(0,len(love)):
#         for f in range(0, len(capitalized)):
#             if capitalized[f] == love[i]:
#                 calc2 += 1
                
#     print(f"{calc1}{calc2}")

# calculate_love_score("Angela Yu", "Jack Bauer")

#day 9: python dictionary, nesting

# student_scores = {
#     'Harry': 88,
#     'Ron': 78,
#     'Hermione': 95,
#     'Draco': 75,
#     'Neville': 60
# }

# student_grades = {}

# for i in student_scores:
#     grade = student_scores[i]
#     if(grade >= 91):
#         student_grades[i] = "Outstanding"
#     elif(grade >= 81 and grade <= 90):
#         student_grades[i] = "Exceeds Expectations"
#     elif(grade >= 71 and grade <= 80):
#         student_grades[i] = "Acceptable"
#     elif(grade <= 70):
#         student_grades[i] = "Fail"
        
# for test in student_grades:
#     print(test)
#     print(student_grades[test])

# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Philippines": ["Manila", "Cebu"],
# }

# nested_list = ['A', 'B', ['C', 'D']]

# print(travel_log["France"][1])
# print(nested_list[2][1])

#day 10: function with outputs

# def is_leap_year(year):
#     """calculates a year if it is a leap year or not"""
#     if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
#         return True
#     else:
#         return False

# print(is_leap_year(1700))

