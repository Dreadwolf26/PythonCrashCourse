# Conditional Tests

# Variables for testing
car = 'Subaru'
age = 25
name = 'Alice'
height_cm = 170
temperature = 20
is_sunny = True
numbers = [1, 2, 3, 4, 5]
names_list = ['Alice', 'Bob', 'Charlie']
person = {'name': 'Bob', 'age': 30}

# Equality and Inequality with Strings
print("Is car == 'Subaru'? I predict True.")
print(car == 'Subaru')  # True

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')  # False

print("\nIs name != 'Alice'? I predict False.")
print(name != 'Alice')  # False

print("\nIs name != 'Bob'? I predict True.")
print(name != 'Bob')  # True

# Tests using the lower() function
print("\nIs name.lower() == 'alice'? I predict True.")
print(name.lower() == 'alice')  # True

print("\nIs name.lower() == 'ALICE'? I predict False.")
print(name.lower() == 'ALICE')  # False

# Numerical Tests
print("\nIs age == 25? I predict True.")
print(age == 25)  # True

print("\nIs age != 25? I predict False.")
print(age != 25)  # False

print("\nIs height_cm > 150? I predict True.")
print(height_cm > 150)  # True

print("\nIs height_cm < 150? I predict False.")
print(height_cm < 150)  # False

print("\nIs temperature >= 20? I predict True.")
print(temperature >= 20)  # True

print("\nIs temperature < 20? I predict False.")
print(temperature < 20)  # False

print("\nIs age <= 30? I predict True.")
print(age <= 30)  # True

print("\nIs age > 30? I predict False.")
print(age > 30)  # False

# Tests using the and keyword and the or keyword
print("\nIs age > 20 and height_cm > 160? I predict True.")
print(age > 20 and height_cm > 160)  # True

print("\nIs age > 30 and height_cm > 160? I predict False.")
print(age > 30 and height_cm > 160)  # False

print("\nIs temperature == 20 or is_sunny == False? I predict True.")
print(temperature == 20 or is_sunny == False)  # True

print("\nIs temperature == 30 or is_sunny == False? I predict False.")
print(temperature == 30 or is_sunny == False)  # False

# Test whether an item is in a list
print("\nIs 'Alice' in names_list? I predict True.")
print('Alice' in names_list)  # True

print("\nIs 'David' in names_list? I predict False.")
print('David' in names_list)  # False

# Test whether an item is not in a list
print("\nIs 'David' not in names_list? I predict True.")
print('David' not in names_list)  # True

print("\nIs 'Alice' not in names_list? I predict False.")
print('Alice' not in names_list)  # False


#5-3
alien_color = "yellow"

#This version fails due to it being false and no else statements
if alien_color == "green":
    print("You have earned 5 points!")

#this version passes due to the variable value matching the conditional 
if alien_color == "yellow":
    print("You have earned 5 points!")


#Writing an if-else chain 
if alien_color == "green":
    print("You have earned 5 points!")
else:
    print("You did not get an alient better luck next time.")

#if-elif-else chain aliens

if alien_color == "red":
    print("You've earned 15 points")
elif alien_color == "yellow": 
    print("You've scored 66 points")
elif alien_color == "green":
    print("You've earned 99 points")

#if-elif-else chain stage of life 

age = 32

if age < 2:
    print("You are a baby")
elif age >= 2 and age < 4:
    print("You are a toddler")
elif age >= 4 and age < 13:
    print("You are a kid")
elif age >= 13 and age < 20:
    print("You are a teenager")
elif age >= 20 and age < 65:
    print("You are an adult")
else:
    print("You are an elder")


favorite_fruits = ["Pineapple", "Watermelon", "Cantaloupe"]

if "Pineapple" in favorite_fruits:
    print("You really like Pineapple")
else:
    print("Fruit is not found in the list")

if "Watermelon" in favorite_fruits:
    print("You really like Watermelon")
else:
    print("Fruit is not found in the list")

if "Cantaloupe" in favorite_fruits:
    print("You really like Cantaloupe")
else:
    print("Fruit is not found in the list")

#5-8 
usernames = ["dreadwolf26", "admin", "chris", "malachi", "james"]

if usernames:
    for username in usernames:
        if username == "admin":
            print("Hello, " + username + " would you like to see a status report")
        else:
            print("Hello, " + username + " thanks for logging in")
else:
    print("We need to find some user!")

current_users = usernames

new_users = ["chris", "jeff", "joe", "bob", "billy"]

for user in new_users:
    if user in current_users:
        print(user + " this user has already been created. Please enter in a new username")
    else:
        print(user + " this username is ready for use!")

ordinal_numbers = [str(num) for num in range(1,10)]

for num in ordinal_numbers:
    if num == "1":
        print("\n" + num + "st")
    elif num =="2":
        print("\n" + num + "nd")
    elif num =="3":
        print("\n" + num + "rd")
    else:
        print("\n" + num + "th")
