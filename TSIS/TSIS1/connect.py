# Import database configuration variables from config.py
from config import DB_NAME, USER, PASSWORD, HOST, PORT

# Import psycopg2 library to work with PostgreSQL
import psycopg2

# Establish a connection to the PostgreSQL database using provided configuration
def get_connection():
    return psycopg2.connect(
        dbname=DB_NAME,
        user=USER,
        password=PASSWORD,
        host=HOST,
        port=PORT
    )