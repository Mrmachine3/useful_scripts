userlist = []

if userlist == []:
    print("We need to find some users!")
for user in userlist:
    if user == 'admin':
        print("Greetings " + user + ",\r\nWould you like to see a status report?\r\n")
    else:
        print("Greetings " + user + ",\r\nThanking you for logging in again.\r\n")
