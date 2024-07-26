class Dog():
    '''A simple attempt to model a dog'''

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name.title()} is now sitting")

    def roll_over(self):
        print(f"{self.name.title()} rolled over!")

my_dog = Dog("Hermoine", 13)

print(f"MY dog's name is {my_dog.name.title()} and she is {str(my_dog.age)} years old")

my_dog.sit()
my_dog.roll_over()

#defining a restaurant class and attributes 
class Restaurant():
    '''A model of a restaurant'''
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name  # Corrected attribute name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def set_number_served(self, number):
        '''Set the number of customers that have been served.'''
        self.number_served = number
        print(f"Number served set to: {str(self.number_served)}.")
        
    def increment_number_served(self, number):
        '''Increment the number of customers served.'''
        self.number_served += number
        print(f"Now serving number: {self.number_served}")
    
    def describe_restaurant(self):
        '''Describe the restaurant.'''
        print(f"This restaurant serves {self.cuisine_type.title()} cuisine and its name is {self.restaurant_name.title()}. It is some of the best food I have ever had.") 
        
    def open_restaurant(self):
        '''Indicate that the restaurant is open.'''
        print(f"{self.restaurant_name.title()} is now open for business!")

#instantiating
rest_1 = Restaurant("Gogeta's Wing Shack", "Wings")
rest_2 = Restaurant("Carl's BBQ Palace", "Bricket 'N More")

#calling the methods
rest_1.describe_restaurant()
rest_1.open_restaurant()
#calling the methods
rest_2.describe_restaurant()
rest_2.open_restaurant()

rest_1.increment_number_served(506)
rest_1.increment_number_served(506)

class User():

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print(f"This user's name is {self.first_name.title()} {self.last_name.title()}")  # Corrected string concatenation

    def greet_user(self):
        print(f"Hello, {self.first_name.title()} {self.last_name.title()}!")  # Corrected string concatenation

    def login(self, number):
        self.login_attempts += number
        print(f"Login attempts: {self.login_attempts}")

    def reset_login_attempts(self):
        self.login_attempts = 0
        print("Login attempts have been reset.")

# Test your class
name_1 = User("Chris", "Holcombe")
name_1.describe_user()
name_1.greet_user()

# Test login and reset login attempts
name_1.login(1)
name_1.login(3)
name_1.reset_login_attempts()
name_1.login(2)

name_2 = User("Caresa", "Stancil")
name_2.describe_user()
name_2.greet_user()

# Test login for the second user
name_2.login(5)
name_2.reset_login_attempts()


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type="Ice Cream"):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = [
        "Vanilla",
        "Chocolate",
        "Strawberry",
        "Mint Chocolate Chip",
        "Cookies and Cream",
        "Butter Pecan",
        "Rocky Road",
        "Neapolitan",
        "Pistachio",
        "Coffee",
        "Caramel Swirl",
        "Mango",
        "Lemon Sorbet",
        "Peanut Butter Cup",
        "Chocolate Chip Cookie Dough"
        ]


    def ice_cream_flavors(self):
        print(f"Here is a list of all of our Flavors:\n")
        for flavor in self.flavors:
            print(flavor)


cream_1 = IceCreamStand("Cream Pop")
cream_1.ice_cream_flavors()
cream_1.describe_restaurant()
cream_1.open_restaurant()
cream_1.ice_cream_flavors()