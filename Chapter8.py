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