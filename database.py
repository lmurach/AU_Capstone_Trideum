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

from datetime import datetime
import sqlite3
from enum import IntEnum
import os
from typing import List
from PyQt5.QtCore import QMutex

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

class AlertTypes(IntEnum):
    '''Alert types passed from the GUI in an array format. This is so that
    various alerts can be turned on and off.'''
    MOTION = 0
    MOTION_ALERT = 1
    ELEVATOR = 2
    HVAC = 3
    DOOR = 4
    DOOR_ALERTS = 5
    IO_ALERTS = 6

# Note when generating test data: ids start at 1.
# Do not use an id of 0 or a foreign key constrain error
# will occur.

class Database:
    '''A class to manage all database related calls using SQLite'''

    mutex = QMutex()
    log_filtering_is_on = [False] * 6

    @staticmethod
    def initialize_db():
        '''Sets up the database with all sample data. 
        If the database exists then .'''

        #does the database exist:
        file = os.path.isfile("database.db")

        con = sqlite3.connect("database.db")
        # strict database relations are off by defaut in sqlite, this turns it on
        con.execute("PRAGMA foreign_keys = 1")
        cur = con.cursor()

        # Don't re fill the database if exists
        if not file:
            Database._create_tables(cur)
            Database._fill_config_table(cur)
            Database._fill_employees_table(cur)
            Database._fill_tables_with_temp_data(cur)
        con.commit()
        con.close()

    @staticmethod
    def _create_tables( cur: sqlite3.Cursor):
        '''Creates all tables on initialization, for testing purposes.
        To avoid any debugging problems, tables should be dropped first.'''

        cur.execute(
            """CREATE TABLE IF NOT EXISTS employees(
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
                name TEXT,
                door_perm INTEGER,
                card_uid INTEGER
            );"""
        )
        cur.execute(
            """CREATE TABLE IF NOT EXISTS door_logs(
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
                date INTEGER,
                e_id INTEGER,
                is_alert INTEGER,
                state TEXT,
                FOREIGN KEY(e_id) REFERENCES employees(id)
            );"""
        )
        cur.execute(
            """CREATE TABLE IF NOT EXISTS HVAC_logs(
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
                date INTEGER,
                floor INTEGER,
                is_alert INTEGER,
                state INTEGER
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
    def _fill_config_table(cur: sqlite3.Cursor):
        '''Fills only the config table as it is more critial'''
        cur.executemany(
            """INSERT INTO config(
                basement_temp, floor1_temp, floor2_temp, opening_time, 
                closing_time, is_dark_mode
                )
                VALUES(?, ?, ?, ?, ?, ?);""", DBTemp.config_log_data
        )

    @staticmethod
    def _fill_employees_table(cur: sqlite3.Cursor):
        cur.executemany(
            """INSERT INTO employees(
                    name, door_perm, card_uid
                )
                VALUES(?, ?, ?);""", DBTemp.employee_data
        )

    @staticmethod
    def _fill_tables_with_temp_data(cur: sqlite3.Cursor):
        '''runs all necessary inserts of temporary data'''
        cur.executemany(
            """INSERT INTO door_logs(
                date, e_id, is_alert, state
                )
                VALUES(?, ?, ?, ?);""", DBTemp.door_log_data
        )
        cur.executemany(
            """INSERT INTO HVAC_logs(
                date, floor, is_alert, floor
                )
                VALUES(?, ?, ?, ?);""", DBTemp.HVAC_log_data
        )
        cur.executemany(
            """INSERT INTO motion_logs(
                date, floor, is_alert
                )
                VALUES(?, ?, ?);""", DBTemp.motion_log_data
        )
        cur.executemany(
            """INSERT INTO elevator_logs(
                date, floor
                )
                VALUES(?, ?);""", DBTemp.elevator_log_data
        )

    def drop_db(self):
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
        con.close()

    def get_config_temperature_array(self) -> List[int]:
        '''Returns an array of temperature sensors in order from the basement
        to the top floor.'''

        Database.mutex.lock()
        con = sqlite3.connect("database.db")
        cur = con.cursor()
        res = cur.execute(
            """
            SELECT basement_temp, floor1_temp, floor2_temp 
            FROM config
            """
        )
        query_output = res.fetchall()
        con.close()
        Database.mutex.unlock()
        # the output is a list of tuples. The tuple size is dependent on the
        # number of columns acessed. Since there is only one row of
        # configurations, then there is just one item in the list with a tuple
        # of 3 elements.
        if len(query_output) == 0:
            return []
        temp_array = [
            query_output[0][0],
            query_output[0][1],
            query_output[0][2]
        ]
        print(temp_array)
        return temp_array

    def set_temperature(self, floor:int, temp:int):
        '''Sets default temperature for a given floor.
        Use 0 for basement and 1 for first floor and so on.'''
        if floor == 0:
            floor_name = "basement_temp"
        elif floor == 1:
            floor_name = "floor1_temp"
        else:
            floor_name = "floor2_temp"
        Database.mutex.lock()
        con = sqlite3.connect("database.db")
        cur = con.cursor()
        cur.execute(
            f"""
            UPDATE config
                SET {floor_name} = ?
            """, (temp,)
        )
        con.commit()
        con.close()
        Database.mutex.unlock()

    def create_motion_log(self, floor:int, is_alert:bool):
        '''Creates a motion log. Enter the floor using 0 for the basement, 1
        for the 1st floor, and 2 for the top floor. Use 1 for red light mode
        and 0 for normal light mode.'''
        Database.mutex.lock()
        date = datetime.now()
        con = sqlite3.connect("database.db")
        cur = con.cursor()
        cur.execute(
            """INSERT INTO motion_logs(
                date, floor, is_alert
                )
                VALUES(?, ?, ?);""", (date, floor, is_alert)
        )
        con.commit()
        con.close()
        Database.mutex.unlock()

    def create_door_log(self, date:datetime, e_id:int, is_alert:int, state:str):
        '''Creates a new door log for opening doors'''
        Database.mutex.lock()
        con = sqlite3.connect("database.db")
        cur = con.cursor()
        cur.execute(
            """INSERT INTO door_logs(
                date, e_id, is_alert, state
                )
                VALUES(?, ?, ?, ?);""", (date, e_id, is_alert, state)
        )
        con.commit()
        con.close()
        Database.mutex.unlock()

    def create_HVAC_log(self, date:datetime, floor:int, is_alert:int, state:str):
        '''Creates a log when the HVAC turns on for an individual floor'''
        Database.mutex.lock()
        con = sqlite3.connect("database.db")
        cur = con.cursor()
        cur.execute(
            """INSERT INTO HVAC_logs(
                date, floor, is_alert, state
                )
                VALUES(?, ?, ?, ?);""", (date, floor, is_alert, state)
        )
        con.commit()
        con.close()
        Database.mutex.unlock()
    
    def create_elevator_log(self, floor):
        '''Creates an elevator log. Enter the floor using 0 for the basement, 1
        for the 1st floor, and 2 for the top floor.'''

        Database.mutex.lock()
        date = datetime.now()
        con = sqlite3.connect("database.db")
        cur = con.cursor()
        cur.execute(
            """INSERT INTO motion_logs(
                date, floor
                )
                VALUES(?, ?);""", (date, floor)
        )
        con.commit()
        con.close()
        Database.mutex.unlock()

    def does_employee_have_access(self, name:str) -> int:
        '''Checks if the employee exists and if they have have door permissions.
        An id of 0 is returned if the employee doesn't exist (this id is
        impossible using the autoincrement property)'''
        Database.mutex.lock()
        con = sqlite3.connect("database.db")
        cur = con.cursor()
        cur.execute(
            """SELECT id 
            FROM employees
            WHERE name == ?
            AND door_perm == 1;""", (name,)
        )
        result = cur.fetchone()
        con.close()
        Database.mutex.unlock()
        if result is None:
            # User does not exist
            return -1
        return result[0]

    def add_employee_card_uid(self, name:str, uid:str):
        '''Adds a uid to the employees database when writing a new card. This
        is to help prevent cards from having different names rewritten on them.
        When reading, the card should always check that the uid matches what
        is in the database.'''
        con = sqlite3.connect("database.db")
        cur = con.cursor()
        cur.execute(
            """UPDATE employees
            SET card_uid = ?
            WHERE name == ?""", (uid, name)
        )
        con.commit()

    def does_employee_have_uid(self, e_id:int, uid:str) -> bool:
        '''Upon reading a card, validates that the uid matches the 
        employee uid'''
        con = sqlite3.connect("database.db")
        cur = con.cursor()
        print(f"id is {e_id}")
        cur.execute(
            """SELECT card_uid 
            FROM employees
            WHERE id == 1
            AND door_perm == 1;"""
        )
        print(f"scan uid: {uid}")
        print(f"db uid: {cur.fetchone()}")
        cur.execute(
            """SELECT name 
            FROM employees
            WHERE card_uid == ?
            AND id == ?
            AND door_perm == 1;""", (uid, e_id)
        )
        result = cur.fetchone()
        if result is None:
            # unscanned card
            return False
        return True

    def get_log_string_array(self) -> List[str]:
        '''Returns a formatted string array of all database logs'''
        log_string_array = []
        sql_array = self._get_logs_sql()
        if sql_array.count == 0:
            return log_string_array
        for query in sql_array:
            if query[LogTypes.TYPE] == "door":
                if query[LogTypes.STATE] == "close":
                    log_string_array.append(
                        f"{query[LogTypes.DATE]}: "
                        f"{query[LogTypes.NAME]} closed the door."
                    )
                elif query[LogTypes.IS_ALERT] == 0:
                    log_string_array.append(
                        f"{query[LogTypes.DATE]}: "
                        f"{query[LogTypes.NAME]} opened the door."
                    )
                else:
                    log_string_array.append(
                        f"{query[LogTypes.DATE]}: "
                        f"{query[LogTypes.NAME]} left the door open."
                    )
            if query[LogTypes.TYPE] == "HVAC":
                if query[LogTypes.IS_ALERT] == 1:
                    if query[LogTypes.STATE] == 1:
                        log_string_array.append(
                            f"{query[LogTypes.DATE]}: "
                            f"Temperature sensor reconnected "
                            f"on floor {query[LogTypes.FLOOR]}."
                        )
                    if query[LogTypes.STATE] == 0:
                        log_string_array.append(
                            f"{query[LogTypes.DATE]}: "
                            f"Temperature sensor disconnected "
                            f"on floor {query[LogTypes.FLOOR]}."
                        )
                if query[LogTypes.IS_ALERT] == 0:
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

    def _get_logs_sql(self):
        '''Returns a list of tuples to pass into the string array function. The
        tables are all unioned together into one resulting function so that they
        can be ordered by datetime.
        TODO: This function is extremely inefficient and needs to be reworked.
        The output should remain the same, just with a backend change.'''
        Database.mutex.lock()
        con = sqlite3.connect("database.db")
        query_list = []
        if (Database.log_filtering_is_on[AlertTypes.MOTION] and
            Database.log_filtering_is_on[AlertTypes.MOTION_ALERT]):
            query_list.append("""
                SELECT NULL AS name, time(date), floor, is_alert, NULL AS state,
                    'motion' AS type
                FROM motion_logs
                """)
        elif Database.log_filtering_is_on[AlertTypes.MOTION]:
            query_list.append("""
                SELECT NULL AS name, time(date), floor, is_alert, NULL AS state,
                    'motion' AS type
                FROM motion_logs
                WHERE is_alert = 0
                """)
        elif Database.log_filtering_is_on[AlertTypes.MOTION_ALERT]:
            query_list.append("""
                SELECT NULL AS name, time(date), floor, is_alert, NULL AS state,
                    'motion' AS type
                FROM motion_logs
                WHERE is_alert = 1
                """)
        if (Database.log_filtering_is_on[AlertTypes.DOOR] and
            Database.log_filtering_is_on[AlertTypes.DOOR_ALERTS]):
            query_list.append("""
                SELECT e.name, time(d.date), NULL AS floor, is_alert, state,
                    'door' AS type
                FROM employees AS e, door_logs AS d
                WHERE d.e_id = e.id
                """)
        elif Database.log_filtering_is_on[AlertTypes.DOOR]:
            query_list.append("""
                SELECT e.name, time(d.date), NULL AS floor, is_alert, state,
                    'door' AS type
                FROM employees AS e, door_logs AS d
                WHERE d.e_id = e.id
                AND is_alert = 0
                """)
        elif Database.log_filtering_is_on[AlertTypes.DOOR_ALERTS]:
            query_list.append("""
                SELECT e.name, time(d.date), NULL AS floor, is_alert, state,
                    'door' AS type
                FROM employees AS e, door_logs AS d
                WHERE d.e_id = e.id
                AND is_alert = 1
                              
                UNION ALL
                              
                SELECT NULL AS name, time(date), floor, is_alert, state,
                    'HVAC' AS type
                FROM HVAC_logs
                WHERE is_alert = 1
                """)
        if Database.log_filtering_is_on[AlertTypes.ELEVATOR]:
            query_list.append("""
                SELECT NULL AS name, time(date), floor, NULL AS is_alert, NULL AS state,
                    'ele' AS type
                FROM elevator_logs
                """)
        if Database.log_filtering_is_on[AlertTypes.HVAC]:
            query_list.append("""
                SELECT NULL AS name, time(date), floor, is_alert, state,
                    'HVAC' AS type
                FROM HVAC_logs
                WHERE is_alert = 0
                """)
        # if Database.log_filtering_is_on[AlertTypes.IO_ALERTS]:
        #     query_list.append("""
        #         SELECT NULL AS name, time(date), floor, is_alert, state,
        #             'HVAC' AS type
        #         FROM HVAC_logs
        #         WHERE is_alert = 1
        #         """)
        query_string = ""
        for index, query in enumerate(query_list):
            if (index != 0 and index < len(query_list)):
                query_string += """
                    UNION ALL

                    """
            query_string += query
        if len(query_list) != 0:
            query_string += """
                ORDER BY time(date) DESC
                
                LIMIT 45;
                """
        # print(query_string)
        cur = con.cursor()
        res = cur.execute(query_string)
        logs = res.fetchall()
        con.close()
        Database.mutex.unlock()
        if len(logs) == 0:
            return []
        return logs

if __name__ == "__main__":
    Database.initialize_db()
