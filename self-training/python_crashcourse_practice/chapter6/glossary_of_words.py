words = {'immutable': 'An object with a fixed value. Immutable objects include numbers, strings and tuples.',
         'list': 'A built-in Python sequence.',
         'statement': 'A statement is part of a block of code.',
         'slice': 'An object usually containing a portion of a sequence.',
         'dictionary': 'An associative array, where arbitrary keys are mapped to values.',
         'module': 'A block of code imported by some other code.',
         'package': 'A module that contains other modules, as in a directory stored in a file system.',
         'function': 'A block of code that is invoked by "calling" a program to execute an action.',
         'regular expression': 'A formula for matching strings that follow some defined pattern.',
         'string': 'One of the basic Python data types to store text.',
         }
print("Glossary:\n")

for word in words:
    print(word.title() + ":\n\t" + str(words[word]) + "\n")
