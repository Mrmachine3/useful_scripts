# beginning with an empty list, allows you to append new list items
motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

# adding new list elements by using the insert method

motorcycles.insert(1, 'ducati')
motorcycles.append('harley')
# print(motorcycles)

# to remove list items include the del method and define the target item in the index

# print (motorcycles)
del motorcycles[1]
motorcycles.insert(3, 'ducati')
motorcycles.insert(-1, 'indian')
print (motorcycles)

popped_motorcycles = motorcycles.pop()
# print (motorcycles)
# print (popped_motorcycles)

last_owned = motorcycles.pop()
print ("The last motorcycle I owned was a " + last_owned.title() + ".")

first_owned = motorcycles.pop(0)
print ('The first motorcycle I owned was a ' + first_owned.title() + ".")

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print (motorcycles)
print ("\nA " + too_expensive.title() + " is too expensive for me!")
