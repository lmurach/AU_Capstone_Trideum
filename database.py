"""
Author  : Lauren Murach
Date    : 02/11/2024
Purpose : The Database class handles all important logging to keep track of
          possible security vulnerabilities. Handling in SQL allows to query for 
          only small parts of data, such as motion sensor alerts, within a large
          set of data, such as all motion sensor events. The Database class also
          handles configurations, so that the GUI has better easy-of-use by 
          opening to the previous configurations on launch.
"""

import sqlite3
from enum import IntEnum
import os

from database_temp_data import DBTemp

class LogTypes(IntEnum):
    NAME = 0
    DATE = 1
    FLOOR = 2
    IS_ALERT = 3
    STATE = 4
    TYPE = 5

# Note when generating test data: ids start at 1.
# Do not use an id of 0 or a foreign key constrain error
# will occur.

class Database:
    '''A class to manage all database related calls using SQLite'''

    @staticmethod
    def initialize_db():
        '''Sets up the database with all sample data. 
            Only call this function after the database has been dropped, 
            such as during debugging or massive database changes.'''

        #does the database exist:
        exists = os.path.isfile("database.db")

        con = sqlite3.connect("database.db")
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()

        # Don't re fill the database if exists
        if not exists:
            Database._create_tables(cur)
            Database._fill_tables_with_temp_data(cur)
        con.commit()

    @staticmethod
    def _create_tables(cur: sqlite3.Cursor):
        '''Creates all tables on initialization, for testing purposes.
        To avoid any debugging problems, tables should be dropped first.'''

        cur.execute(
            """CREATE TABLE IF NOT EXISTS employees(
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
                name TEXT,
                door_perm INTEGER
            );"""
        )
        cur.execute(
            """CREATE TABLE IF NOT EXISTS door_logs(
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
                date INTEGER,
                e_id INTEGER,
                FOREIGN KEY(e_id) REFERENCES employees(id)
            );"""
        )
        cur.execute(
            """CREATE TABLE IF NOT EXISTS HVAC_logs(
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
                date INTEGER,
                floor INTEGER
            );"""
        )
        cur.execute(
            """CREATE TABLE IF NOT EXISTS motion_logs(
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
                date INTEGER,
                floor INTEGER,
                is_alert INTEGER
            )"""
        )
        cur.execute(
            """CREATE TABLE IF NOT EXISTS elevator_logs(
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
                date INTEGER,
                floor INTEGER,
                state TEXT
            )"""
        )
        cur.execute(
            """CREATE TABLE IF NOT EXISTS config(
                basement_temp INTEGER,
                floor1_temp INTEGER,
                floor2_temp INTEGER,
                opening_time INTEGER,
                closing_time INTEGER,
                is_dark_mode INTEGER
            )"""
        )

    @staticmethod
    def _fill_tables_with_temp_data(cur: sqlite3.Cursor):
        '''runs all necessary inserts of temporary data'''
        cur.executemany(
            """INSERT INTO employees(
                    name, door_perm
                )
                VALUES(?, ?);""", DBTemp.employee_data
        )
        cur.executemany(
            """INSERT INTO door_logs(
                date, e_id
                )
                VALUES(?, ?);""", DBTemp.door_log_data
        )
        cur.executemany(
            """INSERT INTO HVAC_logs(
                date, floor
                )
                VALUES(?, ?);""", DBTemp.HVAC_log_data
        )
        cur.executemany(
            """INSERT INTO motion_logs(
                date, floor, is_alert
                )
                VALUES(?, ?, ?);""", DBTemp.motion_log_data
        )
        cur.executemany(
            """INSERT INTO elevator_logs(
                date, floor, state
                )
                VALUES(?, ?, ?);""", DBTemp.elevator_log_data
        )

    @staticmethod
    def drop_db():
        '''Drops all tables. Used ONLY for testing purposes'''

        con = sqlite3.connect("database.db")
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS door_logs;")
        cur.execute("DROP TABLE IF EXISTS employees;")
        cur.execute("DROP TABLE IF EXISTS HVAC_logs;")
        cur.execute("DROP TABLE IF EXISTS motion_logs;")
        cur.execute("DROP TABLE IF EXISTS elevator_logs;")
        cur.execute("DROP TABLE IF EXISTS config;")
        con.commit()

    @staticmethod
    def get_log_string_array():
        log_string_array = []
        sqlArray = Database._get_logs_sql()
        for query in sqlArray:
            if query[LogTypes.TYPE] == "door":
                log_string_array.append(
                    f"""{query[LogTypes.DATE]}: {query[LogTypes.NAME]} opened the door."""
                )
            if query[LogTypes.TYPE] == "HVAC":
                log_string_array.append(
                    f"""{query[LogTypes.DATE]}: HVAC turned on for floor {query[LogTypes.FLOOR]}."""
                )
            if query[LogTypes.TYPE] == "motion":
                if query[LogTypes.IS_ALERT]:
                    log_string_array.append(
                        f"""{query[LogTypes.DATE]}: motion detected on floor {query[LogTypes.FLOOR]} after business hours."""
                    )
                else:
                    log_string_array.append(
                        f"""{query[LogTypes.DATE]}: motion detected on floor {query[LogTypes.FLOOR]}."""
                    )
            if query[LogTypes.TYPE] == "ele":
                if query[LogTypes.STATE] == "requested":
                    log_string_array.append(
                        f"""{query[LogTypes.DATE]}: Elevator requested for floor {query[LogTypes.FLOOR]}."""
                    )
                if query[LogTypes.STATE] == "arrived":
                    log_string_array.append(
                        f"""{query[LogTypes.DATE]}: Elevator arrived on floor {query[LogTypes.FLOOR]}."""
                    )
        return log_string_array

    @staticmethod
    def _get_logs_sql():
        con = sqlite3.connect("database.db")
        cur = con.cursor()
        res = cur.execute(
            """
            SELECT e.name, d.date, NULL AS floor, NULL AS is_alert, NULL AS state, 'door' AS type
            FROM employees AS e, door_logs AS d
            WHERE d.e_id = e.id

            UNION ALL

            SELECT NULL AS name, date, floor, NULL AS is_alert, NULL AS state, 'HVAC' AS type
            FROM HVAC_logs

            UNION ALL

            SELECT NULL AS name, date, floor, is_alert, NULL AS state, 'motion' AS type
            FROM motion_logs

            UNION ALL

            SELECT NULL AS name, date, floor, NULL AS is_alert, state, 'ele' AS type
            FROM elevator_logs

            ORDER BY date;
            """
        )
        return res.fetchall()