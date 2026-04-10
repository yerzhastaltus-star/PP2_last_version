import psycopg2
import csv
from config import load_config
from connect import connect


def create_table():
    config = load_config()
    try:
        with connect(config) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS pphonebook(
                        id SERIAL PRIMARY KEY,
                        first_name VARCHAR(100) NOT NULL,
                        surname VARCHAR(100) NOT NULL,
                        phone VARCHAR(20) UNIQUE NOT NULL
                    );
                """)
    except Exception as error:
        print("Error while creating table:", error)


def load_sql_file(filename):
    config = load_config()
    try:
        with connect(config) as conn:
            with conn.cursor() as cur:
                with open(filename, "r", encoding="utf-8") as file:
                    cur.execute(file.read())
    except Exception as error:
        print(f"Error while loading {filename}:", error)


def import_csv():
    config = load_config()
    try:
        with connect(config) as conn:
            with open("contacts.csv", "r", newline="", encoding="utf-8") as file:
                reader = csv.reader(file)
                next(reader)

                list_phone_numbers = []
                for row in reader:
                    # CSV format: first_name, surname, phone
                    s = (row[0], row[1], row[2])
                    list_phone_numbers.append(s)

                with conn.cursor() as cur:
                    cur.executemany(
                        """
                        INSERT INTO pphonebook(first_name, surname, phone)
                        VALUES(%s, %s, %s)
                        ON CONFLICT (phone) DO NOTHING;
                        """,
                        list_phone_numbers
                    )
    except Exception as error:
        print("Error while importing CSV:", error)


def add_or_update_user():
    first_name = input("Input first name: ")
    surname = input("Input surname: ")
    phone = input("Input phone: ")

    config = load_config()
    try:
        with connect(config) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "CALL insert_or_update_user(%s, %s, %s);",
                    (first_name, surname, phone)
                )
        print("Done.")
    except Exception as error:
        print("Error:", error)


def search_pattern():
    pattern = input("Input pattern: ")

    config = load_config()
    try:
        with connect(config) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT * FROM search_contacts(%s);",
                    (pattern,)
                )
                rows = cur.fetchall()

                if not rows:
                    print("No matches found.")
                else:
                    for row in rows:
                        print(row)
    except Exception as error:
        print("Error:", error)


def show_paginated():
    limit_value = int(input("Input LIMIT: "))
    offset_value = int(input("Input OFFSET: "))

    config = load_config()
    try:
        with connect(config) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT * FROM get_contacts_paginated(%s, %s);",
                    (limit_value, offset_value)
                )
                rows = cur.fetchall()

                if not rows:
                    print("No rows.")
                else:
                    for row in rows:
                        print(row)
    except Exception as error:
        print("Error:", error)


def delete_user():
    p_by = input("Delete by 'name' or 'phone': ")
    value = input("Input value: ")

    config = load_config()
    try:
        with connect(config) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "CALL delete_user(%s, %s);",
                    (value, p_by)
                )
        print("Deleted if record existed.")
    except Exception as error:
        print("Error:", error)


def insert_many_users():
    n = int(input("How many users do you want to add? "))

    first_names = []
    surnames = []
    phones = []

    for _ in range(n):
        first_name = input("First name: ")
        surname = input("Surname: ")
        phone = input("Phone: ")

        first_names.append(first_name)
        surnames.append(surname)
        phones.append(phone)

    config = load_config()
    try:
        with connect(config) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT * FROM insert_many_users(%s, %s, %s);",
                    (first_names, surnames, phones)
                )
                bad_rows = cur.fetchall()

                if bad_rows:
                    print("Incorrect data:")
                    for row in bad_rows:
                        print(row)
                else:
                    print("All users processed successfully.")
    except Exception as error:
        print("Error:", error)


create_table()
load_sql_file("functions.sql")
load_sql_file("procedures.sql")

while True:
    command = input("""
1: import csv
2: add or update one user
3: search by pattern
4: pagination
5: delete user
6: insert many users
7: stop

Input any number from 1 till 7: """)

    if command == "1":
        import_csv()
    elif command == "2":
        add_or_update_user()
    elif command == "3":
        search_pattern()
    elif command == "4":
        show_paginated()
    elif command == "5":
        delete_user()
    elif command == "6":
        insert_many_users()
    elif command == "7":
        break