import json 

filename = "users.json"

def get_stored_username():
    '''Attempt to retrieve the username from the file.'''
    try:
        with open(filename) as file_object:
            username = json.load(file_object)
            return username
    except FileNotFoundError:
        print(f"Filename: {filename} does not exist. Please check again.")
        return None  # Ensure to return None if the file is not found

def display_greeting():
    '''Greet the user after retrieving or storing the username.'''
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"We will remember you when you come back, {username}!")

def get_new_username():
    '''Prompt the user to input a new username and store it in the file.'''
    username = input("What is your name?: ")
    with open(filename, 'w') as file_object:
        json.dump(username, file_object)
    return username

# Calling the function to ensure they work as expected
if __name__ == "__main__":
    display_greeting()
