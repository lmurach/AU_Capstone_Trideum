import sqlite3
import datetime

# Note when generating test data: ids start at 1.
# Do not use an id of 0 or a foreign key constrain error
# will occur.

employee_data = [
    ("John Johnman", 1),
    ("Dave Daveman", 1),
    ("Lisa Liswoman", 1),
    ("Forest Forestman", 0)
]

door_log_data = [
    (datetime.datetime.now(), 2),
    (datetime.datetime.now(), 1),
    (datetime.datetime.now(), 2)
]

class Database:
    '''A class to manage all database related calls using SQLite'''

    @staticmethod
    def initialize_db():
        '''Sets up the database with all sample data. 
            Only call this function after the database has been dropped, 
            such as during debugging or massive database changes.'''
        con = sqlite3.connect("database.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()
        cur.execute(
            """CREATE TABLE employees(
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
                name TEXT,
                door_perm INTEGER
            );"""
        )
        cur.execute(
            """CREATE TABLE door_logs(
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
                date INTEGER,
                e_id INTEGER,
                FOREIGN KEY(e_id) REFERENCES employees(id)
            );"""
        )
        cur.execute(
            """CREATE TABLE HVAC_logs(
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
                date INTEGER,
                floor INTEGER
            );"""
        )
        cur.execute(
            """CREATE TABLE motion_logs(
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
                date INTEGER,
                floor INTEGER,
                is_alert INTEGER
            )"""
        )
        cur.executemany(
            """INSERT INTO employees(
                    name, door_perm
                )
                VALUES(?, ?);""", employee_data
        )
        cur.executemany(
            """INSERT INTO door_logs(
                date, e_id
                )
                VALUES(?, ?);""", door_log_data
        )
        con.commit()

    @staticmethod
    def drop_db():
        '''Drops all tables. Used ONLY for testing purposes'''
        con = sqlite3.connect("database.db")
        cur = con.cursor()
        cur.execute("DROP TABLE door_logs;")
        cur.execute("DROP TABLE employees;")
        cur.execute("DROP TABLE HVAC_logs;")
        cur.execute("DROP TABLE motion_logs;")
        con.commit()

Database.drop_db()
Database.initialize_db()
