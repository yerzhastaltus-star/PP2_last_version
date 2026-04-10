import psycopg2
import csv
from config import load_config
from connect import connect
config = load_config()
try:
    with connect(config) as conn:
        #creating table named Phonebook
        with conn.cursor() as cur:
            cur.execute("""
                create table if not exists Phonebook(
                        id serial primary key,
                        first_name varchar(100) not null,
                        phone varchar(20) unique not null,
                        email varchar(100) unique
                        );
            """)
except Exception as error:
    print(error)
finally:
    conn.close()

#inserting data from a csv file
def import_csv():
    config = load_config()
    with connect(config) as conn:
        with open("contacts.csv", "r", newline = "", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader) #passing header
            list_phone_numbers = []
            for row in reader:
                s = (row[0], row[1], row[2])
                list_phone_numbers.append(s)
            with conn.cursor() as cur:
                cur.executemany(
                    "insert into Phonebook(first_name, phone, email) values(%s, %s, %s) on conflict(phone) do nothing;",
                    list_phone_numbers
                )

def add(first_name, phone):
    config = load_config()
    with connect(config) as conn:
        with conn.cursor() as cur:
            cur.execute(
                "insert into Phonebook(first_name, phone) values(%s, %s);",
                (first_name, phone)
            )

def updating_phone_number(old_phone, new_phone):
    config = load_config()
    with connect(config) as conn:
        with conn.cursor() as cur:
            cur.execute(
                "update Phonebook set phone = %s where phone = %s;",
                (new_phone, old_phone)
            )

def updating_name(old_name, new_name):
    config = load_config()
    with connect(config) as conn:
        with conn.cursor() as cur:
            cur.execute(
                "update Phonebook set first_name = %s where first_name = %s;",
                (new_name, old_name)
            )
def querying(info, which_column): #name, first_name     or     phone_prefix, phone
    config = load_config()
    with connect(config) as conn:
        with conn.cursor() as cur:
            if which_column == "first_name":
                cur.execute(
                    "select * from Phonebook where first_name = %s;",
                    (info,)
                )
                rows = cur.fetchall()
                for id, name, phone, email in  rows:
                    print(id, name, phone, email)
            elif which_column == "phone":
                value = info + "%"
                cur.execute(
                    "select * from Phonebook where phone like %s",
                    (value,)
                )
                rows = cur.fetchall()
                for id, name, phone, email in  rows:
                    print(id, name, phone, email)
def deleting(info, which_column):
    config = load_config()
    with connect(config) as conn:
        with conn.cursor() as cur:
            if which_column == "first_name":
                cur.execute(
                    "delete from Phonebook where first_name = %s;",
                    (info,)
                )
            elif which_column == "phone":
                cur.execute(
                    "delete from Phonebook where phone = %s;",
                    (info,)
                )
while True:
    command = input("1:import csv, 2:add, 3:update, 4:query, 5:delete, 6:stop  input any number from 1 till 6: ")
    if command == "1":
        import_csv()
    elif command == "2":
        first_name1 = input("input first_name: ")
        phone1 = input("input phone number: ")
        add(first_name1, phone1)
    elif command == "3":
        command = input("input command -phone- or -name-: ")
        if command == "phone":
            old_phone = input("input old_phone number: ")
            new_phone = input("input new phone number: ")
            updating_phone_number(old_phone, new_phone)
        if command == "name":
            old_name = input("input old name:")
            new_name = input("input new name")
            updating_name(old_name, new_name)
    elif command == "4":
        command_which_col = input("by which column querying   -first_name- or -phone-:")
        info = input("input info: ")
        querying(info, command_which_col)
    elif command == "5":
        which_column = input("input by which column information   -first_name- or -phone-:")
        info = input("input info: ")
        deleting(info, which_column)
    elif command == "6":
        break;