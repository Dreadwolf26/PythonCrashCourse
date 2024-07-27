#Writing lists anmes to files
dogs = ["Herm", "Sally", "Trigger"]

cats = ["Toby", "Bella","Harper"]

with open("dogs.txt","w") as file_object:
    for dog in dogs:
        file_object.write(dog + "\n")

with open("cats.txt", "w") as file_object:
    for cat in cats:
        file_object.write(cat + "\n")

def read_files(filename):
    '''this function reads the file line by line and prints each line
    to a new line in the console.'''
    try:
        #opens file reads the lines
        with open(filename) as file_object:
            lines = file_object.readlines()
        #Loops through each line and prints them
        for line in lines:
            print(line + "\n")
    #If exception is thrown do something
    except FileNotFoundError:
        pass #this will make sure the error does not show
        #print(f"Files {filename} was not found. Check path.")

#compiled file names in a list
file_names = ["cats.txt","dogs.txt","test.txt"]
#looped through the list containing file names
for name in file_names:
    #passed each file name into the function call as a parameter
    read_files(name)

def word_count(filename):
    '''This function will count the approximate number of words in a file'''
    try:
        with open(filename) as file_object:
            lines = file_object.read()
            words = lines.split()
            num_words = len(words)
            print(f"File name {filename} contains approx. {num_words} words")
    except FileNotFoundError:
        print(f"File {filename} not found")

word_count("python_crash_course.txt")
