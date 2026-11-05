isLogin = False

while isLogin == False:
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username == "kokey" and password == "pogiako123":
        print("Login successful!")
        isLogin = True
    else:
        print("Invalid username or password, please try again.")