alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print alien_0

print("The alien's color is " + alien_0['color'] + ".")

# Modifying the value of speed
# alien_0['color'] = 'yellow'
# print("The alien's color is now " + alien_0['color'] + ".")

print alien_0
del alien_0['points']
print alien_0
