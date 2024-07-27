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
    p_lines = file_object.readlines()

pi_string = ''
for p_line in p_lines:
    pi_string += p_line.rstrip()

print(pi_string)
print(len(pi_string))

l_file_name = "learning_python.txt"

with open(l_file_name) as file_object:
    #this makes a list
    l_lines = file_object.readlines()
    print(l_lines)
#this iterates through the lists and prints each line
for l_line in l_lines:
    '''these below print statements will alternate because the 
    for loop will iterate through both'''
    #this prints each line
    print(l_line)
    #this replaces Python with Java
    print(l_line.replace("Python", "Java"))

write_to_file = "programming.txt"

#This is how you write to a file
with open(write_to_file, "w") as file_object:
    file_object.write("This is how you write to a file\n")
    file_object.write("You can write as many files as you desire\n")

#this is how you append to a written file without over writing
with open(write_to_file, "a") as file_object:
    file_object.write("this is the first newly appended line\n")
    file_object.write("This is the second newly appended line\n")

#assigning the file name to a variable
user_name = "guest.txt"
#asking user for input 
name = input("Please enter your name to be on the guest list: ")
#opening the file in write mode
with open(user_name, "w") as file_object:
    #writing the user name to the guest.txt
    file_object.write(name)

#Using a while loop to write many name
guest_book = "guest_book.txt"

#opening the file and writing the file entry
with open(guest_book, "w") as file_object:
    file_object.write("Please sign the guest book:\n")

while True:
    name = input("Please sign the guest book here! When all names have been added please enter the word exit.: \n")

    with open(guest_book, "a") as file_object:
        file_object.write(name + "\n")

    if name == "exit":
        break

like_programming = "like_programming"

with open(like_programming, "w") as file_object:
    file_object.write("These are all the reasons people like programming:\n")

while True:
    name = input("Please enter your name or simply enter exit to quit:\n")
    l_programming = input("Please enter what you like about programming. When everyone has went simply enter the word exit: \n")

    with open(like_programming,"a") as file_object:
        file_object.write(f"{name} likes all these things about programming {l_programming}\n")

    if l_programming or name == "exit":
        break



