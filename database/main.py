import function_database

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
                boucle = function_database.fn_create_char()
            return True
        case 2:
            boucle = True
            while boucle:
                boucle = function_database.fn_delete_char()
            return True
        case 3:
            db_name = function_database.get_db_n()
            function_database.fn_read_char(db_name)
            return True
        case 4:
            print(f"Fermeture de l'application")
            return False
        case _:
            print(f"\nErreur : Choix non-valide\n")
            return True

def init_menu_user():
    print("Menu Utilisateur")
    q_choix_1 = "[1] Créer un compte"
    q_choix_2 = "[2] Supprimer un compte"
    q_choix_3 = "[3] Afficher les informations de mon compte"
    q_choix_4 = "[4] Quitter"
    list_menu = [q_choix_1, q_choix_2, q_choix_3, q_choix_4]
    return list_menu

def menu_user(list_menu):
    for item in list_menu:
        print(f"{item}")
    q_status = "Entrer votre choix (1-4) : "
    answer = int(input(q_status))

    match answer:
        case 1:
            boucle = True
            while boucle:
                boucle = function_database.fn_create_user()
            return True
        case 2:
            boucle = True
            while boucle:
                boucle = function_database.fn_delete_user()
            return True
        case 3:
            db_name = function_database.get_db_n()
            function_database.fn_read_user(db_name)
            return True
        case 4:
            print(f"Fermeture de l'application")
            return False
        case _:
            print(f"\nErreur : Choix non-valide\n")
            return True

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
                boucle = function_database.fn_create_campaign()
            return True
        case 2:
            boucle = True
            while boucle:
                boucle = function_database.fn_delete_campaign()
            return True
        case 3:
            db_name = function_database.get_db_n()
            function_database.fn_read_campaign(db_name)
            return True
        case 4:
            print(f"Fermeture de l'application")
            return False
        case _:
            print(f"\nErreur : Choix non-valide\n")
            return True

def init_menu_main():
    print("Menu Principal")
    q_choix_1 = "[1] User"
    q_choix_2 = "[2] Character"
    q_choix_3 = "[3] Campagne"
    q_choix_4 = "[4] Quitter"
    list_menu = [q_choix_1, q_choix_2, q_choix_3, q_choix_4]
    return list_menu

def menu_main(list_menu):
    for item in list_menu:
        print(f"{item}")
    q_status = "Entrer votre choix (1-4) : "
    answer = int(input(q_status))

    match answer:
        case 1:
            boucle = True
            while boucle:
                boucle = menu_user(list_menu)
            return True
        case 2:
            boucle = True
            while boucle:
                boucle = menu_character(list_menu)
            return True
        case 3:
            boucle = True
            while boucle:
                boucle = menu_campaign(list_menu)
            return True
        case 4:
            print(f"Fermeture de l'application")
            return False
        case _:
            print(f"\nErreur : Choix non-valide\n")
            return True


def init_db():
    db_name = function_database.get_db_n()
    sql_init_script = function_database.get_sql_s()
    function_database.init_db(db_name, sql_init_script)


def fn_app():
    boucle = True
    list_menu = init_menu_main()
    while boucle:
        boucle = menu_main(list_menu)


if __name__ == "__main__":
    init_db()
    fn_app()
