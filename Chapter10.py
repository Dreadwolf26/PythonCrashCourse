#opens the file and prints its contents
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip()) 

file_name = "loop_test.txt"

with open(file_name) as file_object:
    for line in file_object:
        print(line)

with open(file_name) as file_object:
    lines = file_object.readlines()
    #printing lines so show it is in a list
    print(lines)

#looping through the list and printing the stripped lines from it. 
for line in lines:
    print(line.rstrip())

filename = "pi_digits.txt"

with open(filename) as file_object:
    line = file_object.readlines()

pi_string = ""
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))