from connect_db import Database
from classes import Card


def services():
    service = input("""
    1. Transfer money
    2. Get info
    3. History transfers
    0. Exit
    >>> """)

    if service == "1":
        card_number = input("Card Number: ")
        get = Card.get_amount()
        print(list(get))
        for i in Card.transfer_money(card_number):
            for j in i:
                if j == card_number:
                    money_amount = int(input("Amount of money: "))
                    summa = money_amount + int(Card.get_amount())
                    s = Card.update_money(summa, card_number)
                    print(s)

    elif service == "2":
        if len(Card.get_full_info()) == 0:
            print("Data mavjud emas")
        else:
            for i in Card.get_full_info():
                print(f"""
                ID: {i[0]},
                Full Name: {i[1]},
                Card Name: {i[2]},
                Money Amount: {i[3]},
                Expire Date: {i[4]},
                Phone Number: {i[5]},
                Password: {i[6]},
                """)
        return services()

    elif service == "3":
        pass

    elif service == "0":
        pass

    else:
        print("Error")
        return services()


def check(query):
    card_number = input("Card Number: ")
    password = input("Password: ")
    data = Database.connect(query, "select")

    for i in data:
        if i[2] != card_number and i[6] != password:
            continue
        elif i[2] == card_number and i[6] == password:
            return services()
        else:
            print("Password or Card Number incorrect")
            return check(query)


def login():
    print("Login Page")
    query = "SELECT * FROM person"""
    return check(query)
