CREATE TABLE
    characters (
        characterID INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        character_name TEXT,
        character_classe TEXT,
        character_level INT,
        align TEXT,
        race TEXT,
        xp INT,
        caracteristics TEXT,
        competences TEXT,
        initiative INT,
        character_hp INT,
        death_counter INT,
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
        username TEXT,
        pass_word TEXT,
        type_of_user TEXT,
        characterID INT,
        FOREIGN KEY (characterID) REFERENCES characters (characterID)
    );

CREATE TABLE
    campaign (
        campaignID INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        campaign_name TEXT,
        c_creation_time DATETIME,
        userID INT journey_id INT,
        station_id INT,
        FOREIGN KEY (userID) REFERENCES user (userID),
        FOREIGN KEY (station_id) REFERENCES station (station_id)
    );

CREATE TABLE
    inscription (
        inscriptionID INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        i_creation_time DATETIME,
        userID INT,
        campaignID FOREIGN KEY (userID) REFERENCES user (userID),
        FOREIGN KEY (campaignID) REFERENCES campaign (campaignID)
    );