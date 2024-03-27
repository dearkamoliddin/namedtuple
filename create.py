from connect_db import Database


def create_tables():
    person_table = """
       CREATE TABLE person(
        person_id SERIAL PRIMARY KEY,
        full_name VARCHAR(30),
        card_number VARCHAR(30),
        money_amount INT,
        expire_date VARCHAR(30),
        phone_number VARCHAR(30),
        password VARCHAR(30));
    """

    data = {
        "person": person_table
    }

    for i in data:
        print(f"{i}: {Database.connect(data[i], 'create')}")


if __name__ == "__main__":
    create_tables()
