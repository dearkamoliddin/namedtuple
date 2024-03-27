from connect_db import Database
import main


def register():
    services = input("""
    Register Page:
    1. Register
    0. Back
    >>> """)

    if services == "1":  # INSERT
        full_name = input("Full Name: ")
        card_number = input("Card Number: ")
        if 15 < len(card_number) < 17:
            money_amount = int(input("Money Amount: "))
            expire_date = input("Expire Date: ")
            phone_number = input("Phone Number: ")
            password_0 = input("Password: ")
            password_1 = input("Confirm Password: ")
            while password_0 != password_1:
                password_0 = input("Password: ")
                password_1 = input("Confirm Password: ")

            query = f"""INSERT INTO person(full_name, card_number, money_amount, expire_date, phone_number, password)
            VALUES('{full_name}', '{card_number}', {money_amount}, '{expire_date}', '{phone_number}', '{password_1}') 
            """

            print(Database.connect(query, "insert"))
            return main.entrance()

        else:
            print("Card number should be 16 digits")
            return register()

    elif services == "0":
        return main.entrance()

    else:
        print("Error")
        return register()

