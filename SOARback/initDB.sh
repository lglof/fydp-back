#!/bin/bash

interventions_dbFile=db/SOARback_interventions.db
users_dbFile=db/SOARback_users.db

if test -f "$interventions_dbFile"; then
    echo "SOARback interventions db exists at $interventions_dbFile"
else
    echo "SOARback interventions db does not already exist, creating at $interventions_dbFile"
    sqlite3 $interventions_dbFile "
        CREATE TABLE INTERVENTION_TYPES(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            name TEXT NOT NULL);
        CREATE TABLE PERFORMED_INTERVENTIONS(
            id INTEGER PRIMARY KEY NOT NULL,
            type INTEGER NOT NULL,
            worker TEXT NOT NULL,
            time DATETIME NOT NULL,
            direction TEXT,
            pain_level INTEGER,
            satisfaction_level INTEGER,
            FOREIGN KEY (type)
                REFERENCES INTERVENTION_TYPES (id)
            );
        "
    echo "created tables INTERVENTION_TYPES and PERFORMED_INTERVENTIONS"
    sqlite3 $interventions_dbFile "
        INSERT INTO INTERVENTION_TYPES(name)
            VALUES('shift');
        INSERT INTO INTERVENTION_TYPES(name)
            VALUES('barrier cream');
        INSERT INTO INTERVENTION_TYPES(name)
            VALUES('duoderm');
    "
fi

if test -f "$users_dbFile"; then
    echo "SOARback users db exists at $users_dbFile"
else
    echo "SOARback users db does not exist, creating at $users_dbFile"
    sqlite3 $users_dbFile "
        CREATE TABLE USER_TYPES(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            name TEXT NOT NULL,
            view INTEGER NOT NULL,
            edit INTEGER NOT NULL
        );
        CREATE TABLE USERS(
            id INTEGER PRIMARY KEY NOT NULL,
            friendly TEXT NOT NULL,
            password INTEGER NOT NULL,
            user_type INTEGER NOT NULL,
            FOREIGN KEY (user_type)
                REFERENCES USER_TYPES (id)
        );
    "
    echo "created tables USER_TYPES and PERFORMED_INTERVENTIONS"
    sqlite3 $users_dbFile "
        INSERT INTO USER_TYPES(name, view, edit)
            VALUES('RN', 1, 1);
        INSERT INTO USER_TYPES(name, view, edit)
            VALUES('PSW', 0, 1);
        INSERT INTO USER_TYPES(name, view, edit)
            VALUES('PATIENT', 1, 0);
    "
fi
