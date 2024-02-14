"""
Author  : Lauren Murach
Date    : 02/11/2024
Purpose : The DBTemp class supplies arrays of data to the Database class. 
          The seperate file allows for seperation of concerns and a easy switch
          to real database information at a later time.
"""

import datetime

class DBTemp:
    '''This data class is to purely serve for testing the database.
    This file is kept seperate so that if real data needs to be loaded,
    it can be left off from Github by adding it to the .gitignore file.'''

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

    HVAC_log_data = [
        (datetime.datetime.now(), 1),
        (datetime.datetime.now(), 2),
        (datetime.datetime.now(), 3),
        (datetime.datetime.now(), 1),
        (datetime.datetime.now(), 2),
    ]

    motion_log_data = [
        (datetime.datetime.now(), 1, 0),
        (datetime.datetime.now(), 2, 0),
        (datetime.datetime.now(), 3, 1),
        (datetime.datetime.now(), 1, 0),
        (datetime.datetime.now(), 2, 1),
    ]

    elevator_log_data = [
        (datetime.datetime.now(), 1, "in-progress"),
        (datetime.datetime.now(), 1, "arrived"),
        (datetime.datetime.now(), 2, "in-progress"),
        (datetime.datetime.now(), 2, "arrived")
    ]
