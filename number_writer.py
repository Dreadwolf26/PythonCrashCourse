import json 

filename = "number.json"

numbers = [1,6,5,4,2,8,9,6,7,89,2]

#writing the numbers to a json file
with open(filename, "w") as file_object:
    json.dump(numbers, file_object)

#reading json file
with open(filename) as file_object:
    numbers = json.load(file_object)
#printing the file
print(numbers)