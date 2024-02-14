import sqlite3
import os


# find and stock database name
def get_db_n():
    file_path = os.path.realpath(__file__)
    work_dir = os.path.dirname(file_path)
    db_name = f"{work_dir}/database.db"
    return db_name


# find sql scripts in folders
def get_sql_s():
    file_path = os.path.realpath(__file__)
    work_dir = os.path.dirname(file_path)
    sql_init = f"{work_dir}/sql-scripts/init_database.sql"
    return sql_init


# initialize database
def init_db(db_name, sql_init):
    sqliteConnection = None
    try:
        with sqlite3.connect(db_name) as sqliteConnection:
            print(f"Connected to the {db_name}")
            cursor = sqliteConnection.cursor()
            try:
                with open(sql_init, "r") as sqlite_file:
                    try:
                        sql_script = sqlite_file.read()
                    except Exception as error:
                        print(f"Error while reading the SQL script: {error}")
                        return
            except Exception as error:
                print(f"Error while opening the SQL file: {error}")
                return
            try:
                cursor.executescript(sql_script)
                print("SQLite script executed successfully")
            except sqlite3.Error as error:
                print(f"Error while executing SQLite script: {error}")
            finally:
                cursor.close()
    except sqlite3.Error as error:
        print(f"Error while connecting to SQLite: {error}")
    except Exception as error:
        print(f"{error}")
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")


def fn_create_campaign():
    print("")


def fn_delete_campaign():
    print("")


def fn_read_campaign():
    print("")


def fn_create_char():
    print("")


def fn_delete_char():
    print("")


def fn_read_char():
    print("")


def init_menu_character():
    print("Menu Personnage(s)")
    q_choix_1 = "[1] Créer une fiche de personnage"
    q_choix_2 = "[2] Supprimer une fiche de personnage"
    q_choix_3 = "[3] Afficher la liste des fiches de personnage"
    q_choix_4 = "[4] Quitter"
    list_menu = [q_choix_1, q_choix_2, q_choix_3, q_choix_4]
    return list_menu


def menu_character(list_menu):
    for item in list_menu:
        print(f"{item}")
    q_status = "Entrer votre choix (1-4) : "
    answer = int(input(q_status))
    match answer:
        case 1:
            boucle = True
            while boucle:
                boucle = fn_create_char()
            return True
        case 2:
            boucle = True
            while boucle:
                boucle = fn_delete_char()
            return True
        case 3:
            db_name = get_db_n()
            fn_read_char(db_name)
            return True
        case 4:
            print(f"Fermeture de l'application")
            return False
        case _:
            print(f"\nErreur : Choix non-valide\n")
            return True


def fn_read_char(db_name):
    sqliteConnection = None
    try:
        with sqlite3.connect(db_name) as sqliteConnection:
            print(f"Connected to the database {db_name}")
            cursor = sqliteConnection.cursor()
            try:
                cursor.execute(f"SELECT * FROM CHARACTERS;")
                data = cursor.fetchall()
                print("SQLite script executed successfully")
                print(f"\nExecution du SELECT :")
                for line in data:
                    print(line)
                print()
            except sqlite3.Error as error:
                print(f"Error while executing SQLite script: {error}")
            finally:
                cursor.close()
    except sqlite3.Error as error:
        print(f"Error while connecting to SQLite: {error}")
    except Exception as error:
        print(f"{error}")
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

def fn_read_inscription(db_name):
    sqliteConnection = None
    try:
        with sqlite3.connect(db_name) as sqliteConnection:
            print(f"Connected to the database {db_name}")
            cursor = sqliteConnection.cursor()
            try:
                cursor.execute(f"SELECT * FROM INSCRIPTION;")
                data = cursor.fetchall()
                print("SQLite script executed successfully")
                print(f"\nExecution du SELECT :")
                for line in data:
                    print(line)
                print()
            except sqlite3.Error as error:
                print(f"Error while executing SQLite script: {error}")
            finally:
                cursor.close()
    except sqlite3.Error as error:
        print(f"Error while connecting to SQLite: {error}")
    except Exception as error:
        print(f"{error}")
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

def fn_read_campaign(db_name):
    sqliteConnection = None
    try:
        with sqlite3.connect(db_name) as sqliteConnection:
            print(f"Connected to the database {db_name}")
            cursor = sqliteConnection.cursor()
            try:
                cursor.execute(f"SELECT * FROM CAMPAIGN;")
                data = cursor.fetchall()
                print("SQLite script executed successfully")
                print(f"\nExecution du SELECT :")
                for line in data:
                    print(line)
                print()
            except sqlite3.Error as error:
                print(f"Error while executing SQLite script: {error}")
            finally:
                cursor.close()
    except sqlite3.Error as error:
        print(f"Error while connecting to SQLite: {error}")
    except Exception as error:
        print(f"{error}")
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")


def delete_user(db_name, user_id):
    sqliteConnection = None
    try:
        with sqlite3.connect(db_name, timeout=10) as sqliteConnection:
            print(f"Connected to the database {db_name}")
            cursor = sqliteConnection.cursor()
            try:
                cursor.execute(f"DELETE FROM USER WHERE userID = {user_id};")
                print("SQLite command executed successfully")
            except sqlite3.Error as error:
                print(f"Error while executing SQLite command: {error}")
            finally:
                cursor.close()
    except sqlite3.Error as error:
        print(f"Error while connecting to SQLite: {error}")
    except Exception as error:
        print(f"{error}")
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")


def init_delete_user_menu():
    q_choix_1 = "[1] Supprimer un utilisateur"
    q_choix_2 = "[2] Quitter"
    list_menu = [q_choix_1, q_choix_2]
    return list_menu


def delete_user_menu(list_menu):
    for item in list_menu:
        print(f"{item}")
    q_status = "Entrer votre choix : "
    status = int(input(q_status))
    match status:
        case 1:
            db_name = get_db_n()
            fn_read_user(db_name)
            q_id_status = "Entrer votre choix : "
            user_id = input(q_id_status)
            delete_user(db_name, user_id)
            return True
        case 2:
            print(f"Fermeture de l'application")
            return False
        case _:
            print(f"\nErreur : Choix non-valide\n")
            return True


def fn_delete_user():
    try:
        list_menu = init_delete_user_menu()
        delete_db_out = delete_user_menu(list_menu)
    except Exception as error:
        print(f"{error}")
    finally:
        return delete_db_out


def fn_read_user(db_name):
    sqliteConnection = None
    try:
        with sqlite3.connect(db_name) as sqliteConnection:
            print(f"Connected to the database {db_name}")
            cursor = sqliteConnection.cursor()
            try:
                cursor.execute(f"SELECT * FROM USER;")
                data = cursor.fetchall()
                print("SQLite script executed successfully")
                print(f"\nExecution du SELECT :")
                for line in data:
                    print(line)
                print()
            except sqlite3.Error as error:
                print(f"Error while executing SQLite script: {error}")
            finally:
                cursor.close()
    except sqlite3.Error as error:
        print(f"Error while connecting to SQLite: {error}")
    except Exception as error:
        print(f"{error}")
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

def insert_set_user(db_name, username, email, password):
    sqliteConnection = None
    try:
        with sqlite3.connect(db_name, timeout=10) as sqliteConnection:
            print(f"Connected to the database {db_name}")
            cursor = sqliteConnection.cursor()
            try:
                cursor.execute(
                    f"INSERT INTO USER (username, email, password) VALUES (?, ?, ?)",
                    (username, email, password),
                )
                print("SQLite command executed successfully")
            except sqlite3.Error as error:
                print(f"Error while executing SQLite script: {error}")
            finally:
                cursor.close()
    except sqlite3.Error as error:
        print(f"Error while connecting to SQLite: {error}")
    except Exception as error:
        print(f"{error}")
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")


def fn_create_user():
    username = input("Entrez votre nom d'utilisateur : ")
    email = input("Entrez votre adresse mail : ")
    password = input("Entrez votre mot de passe : ")
    db_name = get_db_n()
    insert_set_user(db_name, username, email, password)


def init_menu_user():
    print("Menu Utilisateur")
    choix_1 = "[1] Créer un compte"
    choix_2 = "[2] Supprimer un compte"
    choix_3 = "[3] Afficher les informations de mon compte"
    choix_4 = "[4] Quitter"
    list_menu = [choix_1, choix_2, choix_3, choix_4]
    return list_menu


def set_menu_user(menu_user):
    for item in menu_user:
        print(f"{item}")
    q_status = "Entrer votre choix (1-4) : "
    status = int(input(q_status))

    match status:
        case 1:
            boucle = True
            while boucle:
                boucle = fn_create_user()
            return True
        case 2:
            boucle = True
            while boucle:
                boucle = fn_delete_user()
            return True
        case 3:
            db_name = get_db_n()
            fn_read_user(db_name)
            return True
        case 4:
            print(f"Fermeture de l'application")
            return False
        case _:
            print(f"\nErreur : Choix non-valide\n")
            return True


def menu_user():
    try:
        list_menu = init_menu_user()
        set_user = set_menu_user(list_menu)
    except Exception as error:
        print(f"{error}")
    finally:
        return set_user


def init_menu_campaign():
    print("Menu Campagne")
    q_choix_1 = "[1] Créer une nouvelle campagne"
    q_choix_2 = "[2] Supprimer une campagne"
    q_choix_3 = "[3] Afficher les campagnes"
    q_choix_4 = "[4] Quitter"
    list_menu = [q_choix_1, q_choix_2, q_choix_3, q_choix_4]
    return list_menu


def menu_campaign(list_menu):
    for item in list_menu:
        print(f"{item}")
    q_status = "Entrer votre choix (1-4) : "
    answer = int(input(q_status))

    match answer:
        case 1:
            boucle = True
            while boucle:
                boucle = fn_create_campaign()
            return True
        case 2:
            boucle = True
            while boucle:
                boucle = fn_delete_campaign()
            return True
        case 3:
            db_name = get_db_n()
            fn_read_campaign(db_name)
            return True
        case 4:
            print(f"Fermeture de l'application")
            return False
        case _:
            print(f"\nErreur : Choix non-valide\n")
            return True
