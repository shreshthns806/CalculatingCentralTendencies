import csv

with open("data.csv", newline='') as csv_file:
    reader = csv.reader(csv_file)
    file_data = list(reader)

file_data.pop(0)

weight_array = []

for index in range(len((file_data))):
    weight_item = file_data[index][2]
    weight_array.append(weight_item)


sum = 0

for index in weight_array:
    sum += float(index)

mean = 0

mean = sum/len(weight_array)

print("""
    The mean of the weight (in pounds) is-

    """+str(mean))