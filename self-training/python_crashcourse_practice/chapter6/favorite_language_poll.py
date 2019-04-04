favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'anthony': 'python',
}

# loop through the names in the dictionary
# display message when name matches friends
friends = ['phil', 'sarah',
           'anthony', 'cristina',
           'luigi', 'ron', 'tommy']

for friends in friends:
    if friends in favorite_languages.keys():
        print("Hi " + friends.title() +
              ", I see your favorite language is " +
              favorite_languages[friends].title() + "!\n")
    else:
        print(str(friends.title()) + " , please take our poll!\n")
