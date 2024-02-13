import sqlite3

connexion = sqlite3.connect("database.db")
cursor = connexion.cursor()

connexion.commit()

connexion.close()
