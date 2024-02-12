import sqlite3

connexion = sqlite3.connect("BaseDonnée.db")
cursor = connexion.cursor()
cursor.execute(
    "CREATE TABLE IF NOT EXISTS character (id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, )"
)  # add fk
cursor.execute(
    "CREATE TABLE IF NOT EXISTS campagne (id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, horodatage DATETIME)"
)  # add fk
cursor.execute(
    "CREATE TABLE IF NOT EXISTS inscription (id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, horodatage DATETIME)"
)  # add fk
cursor.execute(
    "CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, username TEXT, email TEXT, password TEXT)"
)  # add fk
print("HELLO WORLD NIIGER")
