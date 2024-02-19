"""
Author  : Lauren Murach
Date    : 02/11/2024
Purpose : The Database class handles all important logging to keep track of
          possible security vulnerabilities. Handling in SQL allows to query for 
          only small parts of data, such as motion sensor alerts, within a large
          set of data, such as all motion sensor events. The Database class also
          handles configurations, so that the GUI has better easy-of-use by 
          opening to the previous configurations on launch.

TODO: 
1. A relational database is the wrong choice for this application. Functions
will be used as a skeleton and be switched over to MongoDB, a NoSQL database.
This is because our logs use almost no relations and benefit from the way that
MongoDB queries. This was a suggestion from Prof. York after I consulted him 
about speed and design.

2. More functions need to be added for adding logs to the database. This will be
prioritized more as the codebases of those functions get built out so the 
correct arguments will be in place.

3. Look into dialog trees and possible better data structures for the string
array function. Currently the code is managable but better solutions should
exist for this type of function. 
"""

import sqlite3
from enum import IntEnum
import os

from database_temp_data import DBTemp

class LogTypes(IntEnum):
    '''Column names of logs so that the database functions are easier to read 
    and more maintainable. It also prevents index out of bounds errors.'''
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
        If the database exists then .'''

        #does the database exist:
        exists = os.path.isfile("database.db")

        con = sqlite3.connect("database.db")
        # strict database relations are off by defaut in sqlite, this turns it on
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
        cur.executemany(
            """INSERT INTO config(
                basement_temp, floor1_temp, floor2_temp, opening_time, 
                closing_time, is_dark_mode
                )
                VALUES(?, ?, ?, ?, ?, ?);""", DBTemp.config_log_data
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
    def get_config_temperature_array() -> int:
        '''Returns an array of temperature sensors in order from the basement
        to the top floor.'''
        con = sqlite3.connect("database.db")
        cur = con.cursor()
        res = cur.execute(
            """
            SELECT basement_temp, floor1_temp, floor2_temp 
            FROM config
            """
        )
        query_output = res.fetchall()
        # the output is a list of tuples. The tuple size is dependent on the
        # number of columns acessed. Since there is only one row of
        # configurations, then there is just one item in the list with a tuple
        # of 3 elements.
        temp_array = [
            query_output[0][0],
            query_output[0][1],
            query_output[0][2]
        ]
        return temp_array


    @staticmethod
    def get_log_string_array() -> list[str]:
        '''Returns a formatted string array of all database logs'''
        log_string_array = []
        sql_array = Database._get_logs_sql()
        for query in sql_array:
            if query[LogTypes.TYPE] == "door":
                log_string_array.append(
                    f"{query[LogTypes.DATE]}: "
                    f"{query[LogTypes.NAME]} opened the door."
                )
            if query[LogTypes.TYPE] == "HVAC":
                log_string_array.append(
                    f"{query[LogTypes.DATE]}: "
                    f"HVAC turned on for floor {query[LogTypes.FLOOR]}."
                )
            if query[LogTypes.TYPE] == "motion":
                if query[LogTypes.IS_ALERT]:
                    log_string_array.append(
                        f"{query[LogTypes.DATE]}: "
                        f"motion detected on floor {query[LogTypes.FLOOR]} "
                        f"after business hours."
                    )
                else:
                    log_string_array.append(
                        f"{query[LogTypes.DATE]}: "
                        f"motion detected on floor "
                        f"{query[LogTypes.FLOOR]}."""
                    )
            if query[LogTypes.TYPE] == "ele":
                if query[LogTypes.STATE] == "requested":
                    log_string_array.append(
                        f"{query[LogTypes.DATE]}: "
                        f"Elevator requested for floor" 
                        f"{query[LogTypes.FLOOR]}."
                    )
                if query[LogTypes.STATE] == "arrived":
                    log_string_array.append(
                        f"{query[LogTypes.DATE]}: "
                        f"Elevator arrived on floor {query[LogTypes.FLOOR]}."
                    )
        return log_string_array

    @staticmethod
    def _get_logs_sql():
        '''Returns a list of tuples to pass into the string array function. The
        tables are all unioned together into one resulting function so that they
        can be ordered by datetime.
        TODO: This function is extremely inefficient and needs to be reworked.
        The output should remain the same, just with a backend change.'''
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
