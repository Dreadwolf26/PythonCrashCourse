import json

filename = "favorite_number.json"


'''Bruh its got a bug it reads the json has the new number iput and saved and then deisplays
The saved number all at the same time IO only want it to display the save number if it isin file

and it keeps asking for number input and overwriting the original number

ahhhhh

This is the current output: 

What is your favorite number?: 15
Your favorite number has been saved!
Is this your favorite number?: 15

'''

def save_number():
    try:
        with open(filename,"w") as file_object:
            num = input("What is your favorite number?: ")
            json.dump(num, file_object)
            print(f"Your favorite number has been saved!")
    except Exception as e:
        print(f"Exceptions {e} was thrown what does it mean? To Google!")

def guess_number():
    try:
        with open(filename) as file_object:
            favorite_num = json.load(file_object)
            print(f"Is this your favorite number?: {favorite_num}")
    except Exception as e:
        print(f"Exceptions {e} was thrown what does it mean? To Google!")


def get_number():
    number = save_number()
    if number:
        return number
    else:
        number = guess_number()
        return number

get_number()