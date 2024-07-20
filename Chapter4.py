#creating a list
pizzas = ["Pepperoni", "Bacon", "Jalapeno and Peperoni"]

#printing each iterm in a list using a for loop
for pizza in pizzas:
    print(pizza)

for pizza in pizzas:
    print("I like all of these pizzas: " + pizza)
    print("Pizza is super great. I want Dominos now. They offer all of these: " + pizza)


animals = ["Cat", "Dog", "Lizard"]
for animal in animals:
    print("A " + animal + " would make a great pet.")
print("Any of these animals would make a great pet!")

#printing 1 - 20
for i in range(1,21):
    print(i)

#list comprhension to count to 1 million 
million = [i for i in range(1,1000001)]
print(million)

#printing min,max and sum of the millions list
print(min(million))
print(max(million))
print(sum(million))

#odd steps
for i in range (1,21,2):
    print(i)

#multiples of 3s
multiplesOfThree = [i for i in range(3,31,3)]
for number in multiplesOfThree:
    print(number)

#list of cubes
cubesList = [i**3 for i in range(1,11)]
for cubes in cubesList:
    print(cubes)

#4-10 try it yourself
guests = ['Ronnie Radke', 'Henry Rollins', 'Jelly Roll', 'Royle McCoy']

print("The first three items in the list are: " + ",".join(guests[:3]))

print("The middle items in the list are: " + ",".join(guests[1:3]))

print("The last three items in the list are: " + ",".join(guests[-3:]))


#4-11

friendsPizzas = pizzas[:]

pizzas.append("Loaded Potato")

friendsPizzas.append("Pineapple (Gross)")

myPizzas = [pizza for pizza in pizzas]
print("My favorite pizas are: ", ",".join(myPizzas))

friendszzzaaaa = [pizza for pizza in friendsPizzas]
print("My friends favorite pizzas are: ", ",".join(friendszzzaaaa))

#4-13
buffetFoods = ("pizza", "chicken tenders", "ribeye", "key lime pie", "french fries")
print("\nOld Menu: ")
for buffet in buffetFoods:
    print(buffet)

#This rejects due to tuples cannot be modified
#buffetFoods.append("General Tso Chicken")

buffetFoods = ("Mac and cheese", "wings", "ribeye", "key lime pie", "french fries")
print("\nNew menu: ")
for buffet in buffetFoods:
    print(buffet)