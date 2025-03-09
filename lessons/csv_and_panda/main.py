import csv

import pandas

# import pandas

# with open("weather_data.csv",mode="r+") as file:
#     # list_csv = file.readlines()
#     # for csv in list_csv:
#     #     print(csv.strip())
#     csv_file = csv.reader(file)
#     temp = []
#     for row in csv_file:
#         if row[1] != "temp":
#             temp.append(int(row[1]))

# data = pandas.read_csv("weather_data.csv")

# data_dict = data.to_dict()
# data_list = data["temp"].to_list()
# sum_add = 0
# for temp in data_list:
#     if temp != "temp":
#         sum_add += int(temp)
#
# res = sum_add / len(data_list)
# print(f"Average Temp: {round(res,2)}")
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# print(f"Fahrenheit: {monday_temp * (9/5) + 32}")

# data_dict = {
#     "Names": ["Raphael", "Maaz", "Hamdhan"],
#     "Ranks": [4,4,4],
# }
#
# convert = pandas.DataFrame(data_dict)
# print(convert)

################### Squirrel Section ##############################

data_dict = {
    "Fur Color": ["gray","red","black"],
    "Count": [],
}
data = pandas.read_csv("Squirrel_data_2018.csv")
columns = data[data.X == "X"]
fur_color = data["Primary Fur Color"]

count_gray = 0
count_red = 0
count_black = 0
for check in fur_color:
    if check == "Gray":
        count_gray += 1
    elif check == "Cinnamon":
        count_red += 1
    elif check == "Black":
        count_black += 1
data_dict["Count"].append(count_gray)
data_dict["Count"].append(count_red)
data_dict["Count"].append(count_black)

for color in fur_color:
    if color == "R" or color == "r":
        print(color)

print(data_dict)
conv = pandas.DataFrame(data_dict)
conv.to_csv("Fur_color_count.csv")


