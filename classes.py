from connect_db import Database


class Card:

    @staticmethod
    def get_full_info():
        query = f"SELECT * FROM person"
        return Database.connect(query, "select")

    @staticmethod
    def transfer_money(card_number):
        query = f"SELECT {card_number} FROM person"
        return Database.connect(query, "select")

    @staticmethod
    def get_amount():
        query = f"SELECT money_amount FROM person"
        return Database.connect(query, "select")

    @staticmethod
    def update_money(card_number, summa):
        query = f"UPDATE person SET money_amount = {summa} WHERE card_number = {card_number}"
        return Database.connect(query, "select")

