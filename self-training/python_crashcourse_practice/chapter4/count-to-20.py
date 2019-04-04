'''
for i in range(0,20):
    print i+1
'''
'''
# list comprehension
twenty = [i+1 for i in range(0,20)]
print twenty
'''
'''
# min, max, and sum of twenty list
print min(twenty)
print max(twenty)
print sum(twenty)
'''
'''
# if 1st number in range set is 0, prints even numbers; if 1st number in range is 1, prints odd numbers
for i in range(1,20,2):
    print i
'''
# list of threes in a for loop
for x in range(0, 33, 3):
    print x

# threes in a list comprehension
threes = [i for i in range(3, 33, 3)]
print threes

# cubed numbers in a for loop
for i in range(1, 11):
    print i**3

# cubed number list comprehension
cubed = [i**3 for i in range(1, 11)]
print cubed
