car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print car == 'subaru'

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

topping = 'sausage'
print("\nIs pizza topping == 'sausage'? I predict True.")
print topping == 'sausage'

print("\nIs pizza topping == 'sausage'? I predict False.")
print(car == 'cheese')

trim = 'rubicon'
print("\nIs the Jeep Wrangler trim == 'rubicon'? I predict True.")
print trim == 'rubicon'

print("\nIs the Jeep Wrangler trim == 'sport'? I predict False.")
print trim == 'sport'

location = 'Matanzas'
print("\nIs the trip location == 'matanzas'? I predict True.")
print location == 'Matanzas'

print("\nIs the trip location == 'lagos'? I predict False.")
print location.upper == 'Lagos'

color = 'green'
print("\nIs the color == 'green'? I predict True.")
print color == 'green'

print("\nIs the color == 'blue'? I predict False.")
print color == 'blue'

topics = ['subaru', 'sausage', 'rubicon', 'Matanzas', 'green']
for topic in topics:
    print color[-1] == 'blue'
    print location[-2] == 'Lagos'
    print (trim[3] == 'rubicon') or (trim[3] == 'Rubicon')

topics.append('windows')
if topics[-1] == 'windows':
    print(topics[-1] + " is not the operating system of choice")
