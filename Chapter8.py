#8-1
def display_message():
    print("\nIn this chapter we are alearning abouit functions and how to use them")

display_message()

#8-2
def favorite_book(title):
    print("\nOne of my favorite books is " + title.title() + ".")

favorite_book("Insomnia by Stephen King")

#8-3
def make_shirt(size,message):
    print("\nYou have ordered " + size + " for your size")
    print("\nThe message: " + message + " will be displayed on the back just like you have specified.")

make_shirt("XXL", "Momento Mori")
make_shirt(size = "Medium", message = "Lamb of God")

#8-4
def make_shirt(message, size="Large"):
    print("\nYou have ordered " + size + " for your size")
    print("\nThe message: " + message + " will be displayed on the back just like you have specified.")

make_shirt(message="I Love Python")

#8-5
def describe_city(city, country="Russia"):
    print(f"The city {city} is in the country of {country}")

describe_city("Moscow")
describe_city("Saint Petersburg")
describe_city("Yekaterinburg")

#8-6
def city_country(city, country):
    cc_pair = (f"{city}, {country}")
    print(cc_pair.title())

city_country("Atlanta", "USA")
city_country("Canton", "USA")
city_country("Knoxville", "USA")

#8-7
def make_album(aritist_name, album_title):
    album = {"name": aritist_name, "title": album_title}
    print(album)

make_album("Falling in Reverse", "The Drug in me is you")
make_album("Hawthorne Heights", "The silence in black and white")
make_album("Escape the Fate", "This war is ours")

while True:
    print("\nThis prgram will story your favorite bands and their albums you input.")
    print("\nWhen prompted enter in the Bands name ad after enter in their album.")
    print("\nIf you want to simply enter the word exit")

    b_name = input("\nInput the name of the band you want to add")
    if b_name == "exit":
        break

    a_name = input(f"/nInput the name of your favorite album by {b_name}")
    if a_name == "exit":
        break

    favorite_band_and_album = make_album(b_name, a_name)
    print(favorite_band_and_album)

#8-9
# Define a list of famous magicians
magicians = [
    "David Copperfield",
    "Houdini",
    "Penn Jillette",
    "Teller",
    "David Blaine",
    "Dynamo",
    "Criss Angel",
    "Siegfried & Roy",
    "Lance Burton",
    "Ricky Jay"
]

# Function to print each magician's name from the list
def show_magicians(magicians):
    # Loop through each magician in the list and print their name
    for magician in magicians:
        print(magician)

# Function to modify a copy of the list of magicians by adding 'the Great' to each name
def make_great(magicians):
    # Make a copy of the magicians list using slicing
    magicians_copy = magicians[:]
    # Iterate through the copied list using indices
    for i in range(len(magicians_copy)):
        # Append ' the Great' to each magician's name and update the copied list
        magicians_copy[i] = magicians_copy[i] + " the Great"
    # Return the modified copy of the list
    return magicians_copy

# Display the original list of magicians
print("Original magicians list:")
show_magicians(magicians)

# Print a newline for better readability
print("\nModifying magicians list by adding 'the Great' to each name:")

# Get a modified copy of the magicians list by calling make_great function
great_magicians = make_great(magicians)

# Display the modified copy of the magicians list
print("\nChanged magicians list:")
show_magicians(great_magicians)

# Display the original list of magicians to confirm it is unchanged
print("\nUnchanged magicians list:")
show_magicians(magicians)

#Using arbitrary number of arguments 
#This return a tuple when using the * paramters
def shopping_list(*items):
    print(items)

shopping_list("Tomatoes", "Garlic", "Basil")

#using a for loop to list out thing better
def shopping_list(*items):
    print("\nHere is your grocery list:")
    for item in items:
        print("- " + item)
    
shopping_list("Tomatoes", "Garlic", "Basil") 

#mix of size and positional arguments
def build_computer(cpu, ram, *components):
    print("\nHere is a list of your custom build computer specifications: ")
    print(f"\nYour CPU choice: {cpu}")
    print(f"\nYour RAM Choice: {ram}")
    print(f"\nThe components select for this build: ")
    for component in components:
        print(f"- {component}")

build_computer("Intel i7", "16GB", "Graphics Card", "SSD", "Cooling System", "Power Supply", "Motherboard")

#practice referencing the book example adding arguments into a dict
def build_car(make, model, **features):
    car = {}
    car["car_make"] = make
    car["car_model"] = model
    for key, value in features.items():
        car[key] = value
    return car

car = build_car('Tesla', 'Model S', color='red', year=2022, autopilot=True, battery='100 kWh')
print(car)


