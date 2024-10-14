def greet_users(names):
    #print a simple greeting each user in the list.
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)
usernames = ['hannah', 'try', 'margot']
greet_users(usernames)