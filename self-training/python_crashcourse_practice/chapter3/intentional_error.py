cars = []
print cars

cars.insert(0, 'Jeep Wrangler JKU')
print cars

wish = "My dream car is a "

print (wish + cars[-1])

cars.append('Jeep Grand Cherokee SRT')

print (wish + cars[-1])

# print cars[2]
cars.insert(2, "1969 Chevy Camaro SS")
print "These are my favorite cars:" + "\r\n" + cars[0] + "\r\n" + cars[1] + "\r\n" + cars[2]
