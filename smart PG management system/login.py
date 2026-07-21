# login.py

USERNAME = "admin"
PASSWORD = "1234"


def login():
    print("\n========== LOGIN ==========")

    username = input("Enter Username : ")
    password = input("Enter Password : ")

    if username == USERNAME and password == PASSWORD:
        print("\nLogin Successful!")
        return True

    else:
        print("\nInvalid Username or Password!")
        return False