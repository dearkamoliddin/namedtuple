import os
import psycopg2
from dotenv import load_dotenv
load_dotenv()


class Database:
    @staticmethod
    def connect(query, query_type):
        database = psycopg2.connect(
            database=os.getenv("database"),
            host=os.getenv("host"),
            user=os.getenv("user"),
            password=os.getenv("password")
        )

        cursor = database.cursor()
        cursor.execute(query, query_type)
        if query_type == "create":
            database.commit()
            return "Created"

        elif query_type == "insert":
            database.commit()
            return "Registered"

        else:
            return cursor.fetchall()
