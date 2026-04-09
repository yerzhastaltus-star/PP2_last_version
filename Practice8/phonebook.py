import os
from connect import connect


def create_table():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            surname VARCHAR(50),
            phone VARCHAR(20)
        );
    """)

    conn.commit()
    cur.close()
    conn.close()
    print("Table created")


def create_functions_and_procedures():
    conn = connect()
    cur = conn.cursor()

    base_dir = os.path.dirname(__file__)

    with open(os.path.join(base_dir, "functions.sql"), "r", encoding="utf-8") as f:
        cur.execute(f.read())

    with open(os.path.join(base_dir, "procedures.sql"), "r", encoding="utf-8") as f:
        cur.execute(f.read())

    conn.commit()
    cur.close()
    conn.close()
    print("Functions and procedures created")


def insert_or_update_user():
    name = input("Enter name: ")
    surname = input("Enter surname: ")
    phone = input("Enter phone: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "CALL insert_or_update_user(%s, %s, %s);",
        (name, surname, phone)
    )

    conn.commit()
    cur.close()
    conn.close()
    print("User inserted or updated")


def search_contacts():
    pattern = input("Enter pattern: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM search_pattern(%s);", (pattern,))
    rows = cur.fetchall()

    if rows:
        for row in rows:
            print(row)
    else:
        print("No contacts found")

    cur.close()
    conn.close()


def show_paginated_contacts():
    limit_value = int(input("Enter limit: "))
    offset_value = int(input("Enter offset: "))

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM get_contacts_paginated(%s, %s);",
        (limit_value, offset_value)
    )
    rows = cur.fetchall()

    if rows:
        for row in rows:
            print(row)
    else:
        print("No contacts found")

    cur.close()
    conn.close()


def insert_many_users():
    names = ["Ali", "Aruzhan", "Dias"]
    surnames = ["Serik", "Nur", "Bek"]
    phones = ["87771234567", "12345", "87001112233"]

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "CALL insert_many_users(%s, %s, %s);",
        (names, surnames, phones)
    )

    conn.commit()
    cur.close()
    conn.close()
    print("Many users inserted")


def delete_user():
    value = input("Enter name or phone: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute("CALL delete_user(%s);", (value,))

    conn.commit()
    cur.close()
    conn.close()
    print("User deleted if existed")


def menu():
    while True:
        print("\n--- PHONEBOOK MENU ---")
        print("1. Create table")
        print("2. Create functions and procedures")
        print("3. Insert or update user")
        print("4. Search by pattern")
        print("5. Show paginated contacts")
        print("6. Insert many users")
        print("7. Delete user")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            create_table()
        elif choice == "2":
            create_functions_and_procedures()
        elif choice == "3":
            insert_or_update_user()
        elif choice == "4":
            search_contacts()
        elif choice == "5":
            show_paginated_contacts()
        elif choice == "6":
            insert_many_users()
        elif choice == "7":
            delete_user()
        elif choice == "0":
            print("Goodbye")
            break
        else:
            print("Wrong choice")


if __name__ == "__main__":
    menu()