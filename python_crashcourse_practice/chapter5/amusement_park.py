'''
age = 12

if age < 4:
    print("Your admission is free.")
elif age < 18:
    print("Your admission cost is $5.00")
else:
    print("Your admission cost is $10.00")
'''

age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age > 65:
    price = 5
print("Your admission cost is $" + str(price) + ".00.")
