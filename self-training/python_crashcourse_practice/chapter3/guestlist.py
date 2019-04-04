names = ['Cristy', 'Mom', 'Tita', 'Tio Mando', 'Abuelita Raque', 'Don Felix']
message = ",\r\nI'd like to invite you to dinner this evening!\r\nPlease respond whether you will be attending or not.\r\n"

# the following prints each list item identified in names plus the defined message
for i in names:
    print (i + message)

# Guest will no longer be attending
print ("\r\n" + names[4] + " will no longer be attending!\r\n")

# replacing guest with new invitee
names[4] = 'Tia Mina'

# the following prints the dinner invitation message to newly added guest
print (names[4] + ",\r\nI'd like to invite you to dinner this evening!\r\n Please responde whether you will be attending or not.\r\n")

# Announcement to current guest list of larger table available
announce = "Hello everyone,\r\nI've been informed that there is a bigger table availabe for our party.\r\n"
print (announce)

names.insert(0, 'Mandito')
names.insert(3, 'Don Juan')
names.append('Mari')

# the following prints each list item identified in names plus the defined message
for i in names:
    print (i + message)

announce2 = "I regret to inform you that our table will no longer be able to accomodate a larger party for this evenning.\r\nWe will have to postpone our dinner for another time.\r\n"

for i in names:
    print ("Hello " + names.pop() + ",\r\n" + announce2)

print ("Hello " + names[2] + ",\r\nDespite the change in our dinner accomodations, I'd still like to invite you to a family dinner this evening!\r\nWe have dinner reservations at 6:00pm; therefore, I will pick you up around 5:30pm.\r\n")

print ("Hello " + names[1] + ",\r\nDespite the change in our dinner accomodations, I'd still like to invite you to a family dinner this evening!\r\nWe have dinner reservations at 6:00pm; therefore, I will pick you up around 5:30pm.")

for i in names:
    del names[0]
print names

'''
del names[0]
del names[0]
print names
'''

i = len(names)
print ("Number of guests invited: " + str(i))
