def login(users): 
    username = input("enter a username: ")
    password = input("enter a password: ")

    for u in users:
        if username == u[0]:
            if password == u[1]:
                return username

                print("Username or password is incorrect. Please try again!")
         



users = [['turrican','abc123'],['dizzy','def456'],['rygar','ghi789']]
username = login(users)
print(username, "has logged in")