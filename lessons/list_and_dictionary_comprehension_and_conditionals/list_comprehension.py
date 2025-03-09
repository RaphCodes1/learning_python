import random

# list comprehensions
# name = "Raphael"
# numbers = [random.randint(0,10), random.randint(0,10), random.randint(0,10)]
# new_list = [n + 1 for n in numbers]
# name_list = [name[i + 1] for i in range(-1,len(name) - 1)]
# name_list_2 = [letter for letter in name]
# num_double = [i * 2 for i in range(1,5)]
#
# print(name_list)
# print(name_list_2)
# print(num_double)
# for n in new_list:
#     print(f"numbers: {n}")

#conditional list comprehension

# names = ["Raphael", "Maaz", "Moe", "Shaheen", "Mike"]
# short_names = [n for n in names if len(n) < 6]
# all_caps = [n.upper() for n in names]
# print(short_names)
# print(all_caps)

# list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
# numbers = [int(s) for s in list_of_strings]
# result = [n for n in numbers]
# print(result)

#opening and reading files with list comprehension
# with open("file1.txt","r+") as file:
#     file_one = [int(line.strip()) for line in file]
#
# with open("file2.txt","r+") as file:
#     file_two = [int(line.strip()) for line in file]
#
#
#
# result = [one for one in file_one if one in file_two]

# print(file_one)
# print(file_two)
# print(result)

#Dictionary comprehension
# names = ["Raphael", "Maaz", "Moe", "Shaheen", "Mike"]
# new_dict = {n:random.randint(0,100) for n in names}
# passed_students = {s:n for (s,n) in new_dict.items() if n > 75}
# print(new_dict)
# print(passed_students)

#using .split() to split the words
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# result = {s:len(s) for s in sentence.split(" ")}
# print(result)

# using .items() to iterate through the dictionary
# weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
# weather_f = {s:(n * 9/5) + 32 for (s,n) in weather_c.items()}
# print(weather_f)

#using PANDAS to iterate through rows
# import pandas
#
# dict_2 = {
#     "name": ["one","two","three"],
#     "val": [420,69,777]
# }
# new_data = pandas.DataFrame(dict_2)
# print(new_data)
# # new_data.to_csv("test.csv")
# for (index,row) in new_data.iterrows():
#     print(row)