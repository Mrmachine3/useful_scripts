# new user validation to current user access list; check includes case insensitive matches
current_users = ['warpi01', 'warpi02', 'admin', 'anthonymrodriguez', 'warZpi01', 'war machine']
new_users = ['warZpi02', 'warZpi03', 'warpi03', 'warpi02', 'admin', 'WAR MACHINE']

for new_user in new_users:
    if new_user.lower() in current_users:
        print("\r\n" + new_user + " username has already been used.\r\nPlease enter a new username.")
    else:
        print("\r\n" + new_user + " username is available for use.\r\nThank your for logging in...")
