import csv
from collections import Counter

with open("data.csv", newline='') as csv_file:
    reader = csv.reader(csv_file)
    file_data = list(reader)

file_data.pop(0)

weight_array = []

for index in range(len((file_data))):
    weight_item = file_data[index][2]
    weight_array.append(weight_item)

data = Counter(weight_array)
data_range = {
    "75-85":0,
    "85-95":0,
    "95-105":0,
    "105-115":0,
    "115-125":0,
    "125-135":0,
    "135-145":0,
    "145-155":0,
    "155-165":0,
    "165-175":0,
}
for weight,occurence in data.items():
    if 75 <= float(weight) < 85:
        data_range["75-85"] += occurence
    if 85 <= float(weight) < 95:
        data_range["85-95"] += occurence
    if 95 <= float(weight) < 105:
        data_range["95-105"] += occurence
    if 105 <= float(weight) < 115:
        data_range["105-115"] += occurence
    if 115 <= float(weight) < 125:
        data_range["115-125"] += occurence
    if 125 <= float(weight) < 135:
        data_range["125-135"] += occurence
    if 135 <= float(weight) < 145:
        data_range["135-145"] += occurence
    if 145 <= float(weight) < 155:
        data_range["145-155"] += occurence
    if 155 <= float(weight) < 165:
        data_range["155-165"] += occurence
    if 165 <= float(weight) < 175:
        data_range["165-175"] += occurence

mode_range_2,mode_occurence = 0,0
for range,occurence_2 in data_range.items():
    if occurence_2 > mode_occurence:
        mode_range_2, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence_2
mode = float((mode_range_2[0] + mode_range_2[1]) / 2)

print("""
    The mode (approximate) of the weight (in pounds) is-

    """+str(mode))