#7-1
car = input("What kinbd of rental car would you like?: ")
print("Let me see if I can find you a " + car)

#7-2
seating = input("How many are in your party?: ")
seating = int(seating)
if seating >= 8:
    print("You will need to wait due to party size")
else:
    print("We may seat you now")

#7-3
num = input("enter a number to see if it is a multiple of 10: ")
num = int(num)
if num % 10 == 0:
    print(str(num) + " is a multiple of ten")
else:
    print(str(num) + " is not multiple of ten")

#7-4
toppings = "\nwhich topping would you like on your pizza?: "
toppings += "\nif you are done adding toppings enter the word 'quit': "
while True:
    pizza_toppings = input(toppings)

    if pizza_toppings == "quit":
        break
    else:
        print("Here is your pizza with: \n" + pizza_toppings)

#7-5
age_prompt = "\nWhat is your age? This will determine your movie ticket price."
age_prompt += "\nEnter 'quit' when you are finished ordering tickets: "

while True:
    user_input = input(age_prompt)
    
    if user_input.lower() == 'quit':
        break

    try:
        input_age = int(user_input)
        
        if input_age < 3:
            print("Your ticket is free.")
        elif input_age <= 12:
            print("Your ticket is $10.")
        else:
            print("Your ticket is $15.")
    
    except ValueError:
        print("Please enter a valid age or 'quit' to exit.")

#7-8
sandwich_orders = [
    "Turkey Club",
    "Veggie Delight",
    "Ham and Swiss",
    "Pastrami",
    "Roast Beef",
    "Chicken Caesar",
    "BLT",
    "Tuna Salad",
    "Pastrami",
    "Grilled Cheese",
    "Reuben",
    "Pastrami",
    "Philly Cheesesteak"
]
finished_sandwiches = []

no_pastrami = "We have run out of pastrami it has been 86'd and no longer here"

while "Pastrami" in sandwich_orders:
    sandwich_orders.remove("Pastrami")
    print(no_pastrami)

for order in sandwich_orders:
    print("I have a " + order + " ready for pick up!")
    finished_sandwiches.append(order)
print(finished_sandwiches)


polling_active = True

vacation = {}

while polling_active:
    name = input("\n what is your name? ")
    spot = input("\n If you could go any place in the world where would you go? ")
    vacation[name] = spot

    repeat = input("Would you like for another person to respond? enter (y / n): ")
    if repeat == "n":
        polling_active = False

print("-------The Results Are In----------")
for name, spot in vacation.items():
    print(name + " would like to go to " + spot )







