# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#         print(row)

#     print(temperatures)


import pandas

# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)
# print()

# print(data["temp"].mean())
# print(data["temp"].max())
# print(data.condition)
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(type(monday.condition))
# monday_temp = int(monday.temp)


# def c2f(c):
#     return (c * 9/5) + 32


# print(c2f(monday_temp))

# data_dict = {"students": ["Amy", "James", "Angela"], "score": [76, 56, 65]}

# my_data = pandas.DataFrame(data_dict)
# print(my_data)
# my_data.to_csv("my_data.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

color_count_table = {"Fur Color": [
    "Gray", "Cinnamon", "Black"], "Count": [0, 0, 0]}
print(color_count_table)

new_count = []

for col in color_count_table["Fur Color"]:
    print(col)
    rows = data[data["Primary Fur Color"] == col]
    new_count.append(rows.size)

color_count_table["Count"] = new_count

new_data = pandas.DataFrame(color_count_table)
new_data.to_csv("squirrel_count.csv")
