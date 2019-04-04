pizzas = ['pepperoni', 'spinach & mushrooms', 'soppressata & onions']

for pizza in pizzas:
    print "I like pizza with " + pizza + ".\r"
print "I really do enjoy all other types of pizza, but these are my favorites!"


friends_pizzas = pizzas[:]

pizzas.append('supreme')
friends_pizzas.append('sausage')

print pizzas
print friends_pizzas

print "My favorite pizzas are:"
for pizza in pizzas:
    print pizza

print "My friend's favorite pizzas are:"
for pizza in friends_pizzas:
    print pizza
