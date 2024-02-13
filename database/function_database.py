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


def input_user_info():
    q_user = input("Entrez votre nom d'utilisateur : ")
    q_mail = input("Entrez votre adresse mail : ")
    q_pw = input("Entrez votre mot de passe : ")
    list_info = [q_user, q_mail, q_pw]
    return list_info


def set_user(db_name, username, email, password):
    sqliteConnection = None
    try:
        with sqlite3.connect(db_name, timeout=10) as sqliteConnection:
            print(f"Connected to the database {db_name}")
            cursor = sqliteConnection.cursor()
            try:
                print(
                    f"Commande SQL exécutée : INSERT INTO user (username, email, password) VALUES ('{username, password, email}');"
                )
                cursor.execute(
                    f"INSERT INTO user (username, email, password) VALUES ('{username, password, email}');"
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


def fn_create_user(list_info,):
    username = list_info[1]
    email = list_info[2]
    password = list_info[3]
    db_name = get_db_n()
    set_user(db_name, username, email, password)


def fn_delete_user():
    print("")


def fn_read_user():
    print("")
