#Create a list of name and print each individual one

names = ['chris', 'ean', 'ken', 'tim']

print(names[0])
print(names[1])
print(names[2])
print(names[3])

# print them again to show correct title
print(names[0].title())
print(names[1].title())
print(names[2].title())
print(names[3].title())

#print a greeting for each person in correct title

greeting = "Hello, my friend: "

print(greeting + names[0].title())
print(greeting + names[1].title())
print(greeting + names[2].title())
print(greeting + names[3].title())


motorcycles = ['Ninja', 'GSXR', 'R1', 'CanAm Ryker']

print("I have always wanted a " + motorcycles[3] + " motorcyle")

#adding Honda shadow to the end of the list 
motorcycles.append("Honda Shadow")
print(motorcycles)

#Deleting the last item in the list 
del motorcycles[-1]
print(motorcycles)

#inserting Honda Shadow into the index position 0 
motorcycles.insert(0, "Honda Shadow")
print(motorcycles)

PoppedMotorcycle = motorcycles.pop()
print(motorcycles)
#the pop item is stored in the PoppedMotorcycle variable name
print(PoppedMotorcycle)


#creating guests list for dinner
guests = ['Ronnie Radke', 'Henry Rollins', 'Jelly Roll', 'Royle McCoy']

invitation = "Hello, you have been invited to this evening at 7:15 PM please by my guest: "

print(invitation + guests[0])
print(invitation + guests[1])
print(invitation + guests[2])
print(invitation + guests[3])

#unable to attend message
UnableToAttend = "Unfortunatly this guest is unable to attend: "
print(UnableToAttend + guests.pop(2))

#adding a guest to the list
guests.append("Ryan Reynolds")
print("I will need to invite another guest and add them to the list this will be: " + guests[-1])

#sending invites again
print(invitation + guests[0])
print(invitation + guests[1])
print(invitation + guests[2])
print(invitation + guests[3])

#3 more guests can be added I will add them to the beginning middle and end of the list using insert 
guests.insert(0, "Randy Blythe")
guests.insert(2, "Alex The Terrible")
guests.insert(-1, "Craig Mabbit")

#sending invites again this could be taken care of as a for loop but I am following the book
print(invitation + guests[0])
print(invitation + guests[1])
print(invitation + guests[2])
print(invitation + guests[3])
print(invitation + guests[4])
print(invitation + guests[5])
print(invitation + guests[6])

#Only able to invite 2 people the rest need to be removed with pop
guests.pop()
guests.pop()
guests.pop()
guests.pop()
guests.pop()

StillInvited = "Hello, you are still invited!: "

print(StillInvited + guests[0])
print(StillInvited + guests[1])

#using the del function to remove the last 2 names
#This could have been done by string slicing
del guests[0]
del guests[0]

#printing list to confirm it is empty
print(guests)


#Try it yourself 3-8

PlacesToSee = ['Japan', 'Ireland', 'Sweden', 'Russia' ,'China']

print(PlacesToSee)

#sorting list into another variable
PlacesToSeeSorted = sorted(PlacesToSee)
print(PlacesToSeeSorted)

#ensuring original list is intact
print(PlacesToSee)

#sorting and reversing a string
PlacesToSeeSortedAndReverse = sorted(PlacesToSee, reverse=True)
print(PlacesToSeeSortedAndReverse)

#ensuring list is the same as original
print(PlacesToSee)

#reversing the original order of the list
PlacesToSee.reverse()
print(PlacesToSee)

#permanently sorting list to alpabetical
PlacesToSee.sort()
print(PlacesToSee)

#permanently reversing the list order
PlacesToSee.reverse()
print(PlacesToSee)