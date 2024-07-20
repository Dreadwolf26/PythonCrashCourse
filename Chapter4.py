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

#continue on page 65
