#opens the file and prints its contents
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents) 
    file_object.close()
    print(contents)