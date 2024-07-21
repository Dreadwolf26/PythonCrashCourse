person = { "first_name": "Chris",
            "middle_name": "James",
            "last_name": "Holcombe",
            "state": "Georgia",
            "city": "Canton"}

#used a for loop because its easier than doing individual print statements
for k,v in person.items():
    print(str(k) + " : " + str(v))

#for the sake of demonstration here is an individual
print(person["first_name"])

#replacing the first name 
person["first_name"] = "Christopher"

#confirming the changes are there. 
print(person["first_name"])

#favorite number
favorite_numbers = {
    'Alice': 9,
    'Bob': 15,
    'Charlie': 3,
    'Diana': 22
}

#Same for loop can be used here for key value pairs
for k,v in favorite_numbers.items():
    print(str(k) + " : " + str(v))

#terms glossary:
python_terms = {
    'variable': 'A name that is used to denote something or a value is called a variable.',
    'list': 'A collection of items in a particular order.',
    'loop': 'A sequence of instructions that is continually repeated until a certain condition is reached.',
    'dictionary': 'A collection of key-value pairs.',
    'function': 'A block of code which only runs when it is called.'
}

#Using the same for loop because this exercise has only been about printing the entire dictionary 
for k,v in python_terms.items():
    print(str(k) + " : " + str(v))


major_rivers = {
    'nile': 'Egypt',
    'amazon': 'Brazil',
    'mississippi': 'USA'
}

for k,v in major_rivers.items(): 
    print("\n The " + k.title() + " runs through " + v.title())

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

poll_people = ['jen', 'sarah', 'phil', 'alice', 'tom']

for people in poll_people:
    if people in favorite_languages.keys():
        print(people.title() +" You have already taken the poll")
    else:
        print(people.title() + " Please take the poll and submit your favorite language")



enemies = []

for enemy_number in range(30):
    tyranid_hormagaunt = {
        'color': 'purple',
        'points': 10,
        'speed': 'fast',
        'attack_type': 'melee'
    }
    enemies.append(tyranid_hormagaunt)

for enemy in enemies[:9]:
    if enemy["color"] == "purple":
        enemy["color"] = "blue"
        enemy["points"] = "25"
        enemy["speed"] = "slow"
        enemy["attack_type"] = "rage"
    
for enemy in enemies:
    print(enemy)


# Dictionary of Warhammer 40K units with attributes in lists
warhammer_units = {
    'Space Marine': ['Blue', 20, 'Fast', 'Ranged'],
    'Ork Boyz': ['Green', 10, 'Medium', 'Melee'],
    'Eldar Wraithguard': ['Red', 30, 'Slow', 'Ranged'],
    'Tyranid Genestealer': ['Purple', 15, 'Fast', 'Melee']
}

# Printing the units and their attributes
print("Warhammer 40K Units and Their Attributes:")
for unit, attributes in warhammer_units.items():
    print(f"\n{unit}:")
    print(f"Color: {attributes[0]}")
    print(f"Points: {attributes[1]}")
    print(f"Speed: {attributes[2]}")
    print(f"Attack Type: {attributes[3]}")



jen = {
    'name': 'Jen',
    'language': 'Python',
    'experience': 5,  
    'location': 'USA'
}

# Two new dictionaries representing different people
alice = {
    'name': 'Alice',
    'language': 'JavaScript',
    'experience': 3,
    'location': 'Canada'
}

bob = {
    'name': 'Bob',
    'language': 'Java',
    'experience': 10,
    'location': 'UK'
}

# List containing all three dictionaries
people = [jen, alice, bob]

for i in people:
    name = i["name"].title()
    language = i["language"].title()
    experience = i["experience"]
    location = i["location"].title()
    print("Hello, " + name + " I see that you like " + language + " with a totaling experience of "\
          + str(experience) + " years. That is very impressive and you are located in the " + location + ".")


fido = {'name': 'Fido', 'type': 'dog', 'owner': 'Alice'}
whiskers = {'name': 'Whiskers', 'type': 'cat', 'owner': 'Bob'}
bubbles = {'name': 'Bubbles', 'type': 'fish', 'owner': 'Charlie'}
rex = {'name': 'Rex', 'type': 'dog', 'owner': 'Diana'}
snowball = {'name': 'Snowball', 'type': 'rabbit', 'owner': 'Eve'}

pets = [fido, whiskers, bubbles, rex, snowball]

for pet in pets:
    print(f"Name: {pet['name']}, Type: {pet['type']}, Owner: {pet['owner']}")