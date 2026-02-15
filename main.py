from connection import connect_to_db
from init_db import init_db

connection = connect_to_db()

if connection:
    init_db(connection)