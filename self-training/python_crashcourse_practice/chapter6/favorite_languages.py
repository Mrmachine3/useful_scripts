favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'anthony': 'python',
}

'''
print("Sarah's favorite language is " +
      favorite_languages['sarah'].title() +
      ".")
'''

'''
# loop through each key-value pair in the dictionary
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")
'''

'''
# loop through dictionary to print names of everyone who took the poll
for name in favorite_languages.keys():
    print(name.title())
'''

'''
# loop through the names in the dictionary and display message when name matches friends
friends = ['phil', 'sarah', 'anthony']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print("\tHi " + name.title() +
              ", I see your favorite language is " +
              favorite_languages[name].title() + "!\n")
if 'erin' not in favorite_languages.keys():
    print('Erin, please take our poll!')
'''

'''
# loop through dictionary and display message in sorted order
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")
'''

# loop thorugh all values in dictionary and print unique values
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())
