import sqlite3

connexion = sqlite3.connect("BaseDonnée.db")
cursor = connexion.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS character (characterID INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, name TEXT, classe TEXT, level INTEGER, align TEXT, race TEXT, xp INTEGER, caracteristics TEXT, competences TEXT, initiative INTEGER, pv INTEGER, death_counter INTEGER, chara_traits TEXT, ideal TEXT, links TEXT, defaults TEXT, sorts TEXT, equipments TEXT, capacity TEXT)") #comment faire pour caracteristic & competences ?
cursor.execute("CREATE TABLE IF NOT EXISTS user (userID INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, username TEXT, email TEXT, password TEXT, type_of_user TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS campaign (campaignID INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, nom TEXT, horodatage DATETIME, FOREIGN KEY (userID) REFERENCES user (userID))") #verif FK
cursor.execute("CREATE TABLE IF NOT EXISTS inscription (inscriptionID INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, horodatage DATETIME,userID INTEGER, campaignID INTEGER, FOREIGN KEY (userID) REFERENCES user (userID), FOREIGN KEY (campaignID) REFERENCES campaign (campaignID))") #add fk


fichin = open("test.csv","r")
user = fichin.readlines()

for el in user :
   decoupe = el.strip("\n").split(",") #le strip enlève le \n et le split divise chaque donnée apres chaque virgule
   username = decoupe[0]
   password = decoupe[1]
   type_user = decoupe[2]
   query = "INSERT INTO user (username, password, type_of_user) VALUES (?, ?, ?)"
   cursor.execute(query, (username, password, type_user))

cursor.execute("SELECT * FROM user")
cols = cursor.fetchall()

connexion.commit()

for col in cols:
   print(col)

connexion.close()
