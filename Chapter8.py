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



    
