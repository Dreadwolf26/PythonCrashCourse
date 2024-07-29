import json
import os

filename = "users.json"

#if filename does not exist create it with an empty string
if not os.path.exists(filename):
    with open (filename, "w") as file_object:
        json.dump([],file_object)

def get_stored_usernames():
    '''Attempt to retrieve the list of usernames from the file.'''
    try:
        with open(filename) as file_object:
            usernames = json.load(file_object)
            return usernames
    except FileNotFoundError:
        return []  # Return an empty list if the file is not found

def display_greeting():
    '''Greet the user after retrieving or storing the username.'''
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"We will remember you when you come back, {username}!")

def get_stored_username():
    '''Retrieve the username if it exists in the file.'''
    usernames = get_stored_usernames()
    if usernames:
        return usernames[-1]
    return None

def get_new_username():
    '''Prompt the user to input a new username and store it in the file.'''
    usernames = get_stored_usernames()  # Read existing usernames
    username = input("What is your name?: ")
    usernames.append(username)  # Append the new username
    with open(filename, 'w') as file_object:
        json.dump(usernames, file_object)  # Write the updated list back to the file
    return username

# Calling the function to ensure they work as expected
if __name__ == "__main__":
    user_check = input("Please enter your username to login: ")
    if user_check in get_stored_usernames():
        display_greeting()
    else:
        get_new_username() 
