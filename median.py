import csv

with open("data.csv", newline='') as csv_file:
    reader = csv.reader(csv_file)
    file_data = list(reader)

file_data.pop(0)

weight_array = []

for index in range(len((file_data))):
    weight_item = file_data[index][2]
    weight_array.append(weight_item)

length = len(weight_array)
print(length)
weight_array.sort()
if length % 2 == 0:
    median1 = float(weight_array[length//2])
    median2 = float(weight_array[(length//2)-1])
    median = (median1 + median2)/2

else:
    median = weight_array[length//2]

print("""
    The median of the weight (in pounds) is-

    """+str(median))