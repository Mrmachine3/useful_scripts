rivers = {
    'mississippi': 'United States of America',
    'amazon': 'Brazil',
    'congo': 'Democratic Republic of Congo'
}

for river in rivers:
    print("The " + river.title() + " River runs through " + str(rivers[river]) + ".")

print("\n")
for river in rivers:
    print(river.title() + " River")
print("\n")
for river in rivers:
    print(str(rivers[river]))
