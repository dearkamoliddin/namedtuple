import login
import registration


def entrance():
    enter = input("""
    1. Log in
    2. Register
    >>> """)

    if enter == "1":
        return login.login()

    elif enter == "2":
        registration.register()

    else:
        print("Error")
        return entrance()


if __name__ == "__main__":
    entrance()
