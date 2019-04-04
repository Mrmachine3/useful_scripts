'''
# define empty list, compute square values from range, append results into list, print values from list
squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)
'''

# compute square values from range into list, print values from list
squares = [value**2 for value in range(1, 11)]
print squares

print ("The first three items in the list are:")
print squares[:3]

print ("Three items from the middle of the list are:")
print squares[4:7]

print ("The last three items in the list are:")
print squares[-3:]
