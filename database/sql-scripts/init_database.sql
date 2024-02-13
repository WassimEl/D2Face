CREATE TABLE
    characters (
        characterID INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        character_name TEXT,
        character_classe TEXT,
        character_level INTEGER,
        align TEXT,
        race TEXT,
        xp INTEGER,
        caracteristics TEXT,
        competences TEXT,
        initiative INTEGER,
        character_hp INTEGER,
        death_counter INTEGER,
        traits TEXT,
        ideal TEXT,
        links TEXT,
        defaults TEXT,
        sorts TEXT,
        equipments TEXT,
        capacity TEXT
    );

CREATE TABLE
    user (
        userID INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        departure_time DATETIME,
        arrival_time DATETIME,
        departure_platform VARCHAR(255),
        arrival_platform VARCHAR(255),
        type_journey VARCHAR(255),
        train_id INT,
        FOREIGN KEY (train_id) REFERENCES train (train_id)
    );

CREATE TABLE
    campaign (
        transfer_station_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        order_in_journey INT,
        journey_id INT,
        station_id INT,
        FOREIGN KEY (journey_id) REFERENCES journey (journey_id),
        FOREIGN KEY (station_id) REFERENCES station (station_id)
    );

CREATE TABLE
    inscription (
        station_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        station_name VARCHAR(255),
        platform_number VARCHAR(255),
        city_id INT,
        FOREIGN KEY (city_id) REFERENCES city (city_id)
    );

"CREATE TABLE IF NOT EXISTS character (characterID INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, name TEXT, classe TEXT, level INTEGER, align TEXT, race TEXT, xp INTEGER, caracteristics TEXT, competences TEXT, initiative INTEGER, pv INTEGER, death_counter INTEGER, chara_traits TEXT, ideal TEXT, links TEXT, defaults TEXT, sorts TEXT, equipments TEXT, capacity TEXT)" "CREATE TABLE IF NOT EXISTS user (userID INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, username TEXT, email TEXT, password TEXT, type_of_user TEXT)" "CREATE TABLE IF NOT EXISTS campaign (campaignID INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, nom TEXT, horodatage DATETIME, FOREIGN KEY (userID) REFERENCES user (userID))" "CREATE TABLE IF NOT EXISTS inscription (inscriptionID INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, horodatage DATETIME,userID INTEGER, campaignID INTEGER, FOREIGN KEY (userID) REFERENCES user (userID), FOREIGN KEY (campaignID) REFERENCES campaign (campaignID))"