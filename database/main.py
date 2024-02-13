import function_database

# def fn_init_menu():
#    q_choix_1 = "[1] Créer une base de données"
#    q_choix_2 = "[2] Encoder des données"
#    q_choix_3 = "[3] Afficher des données"
#    q_choix_4 = "[4] Mettre-à-jour des données"
#   q_choix_5 = "[5] Supprimer des données"
#    q_choix_6 = "[6] Quitter"
#    list_menu = [q_choix_1, q_choix_2, q_choix_3, q_choix_4, q_choix_5, q_choix_6]
#    return list_menu


def init_db():
    db_name = function_database.get_db_n()
    sql_init_script = function_database.get_sql_s()
    function_database.init_db(db_name, sql_init_script)


if __name__ == "__main__":
    init_db()
