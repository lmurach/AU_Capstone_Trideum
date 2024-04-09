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

    sample_date_times = [
        datetime.datetime(2023, 10, 1, 1, 20, 20),
        datetime.datetime(2023, 12, 17, 16, 2, 55),
        datetime.datetime(2024, 1, 16, 11, 24, 13),
        datetime.datetime(2024, 1, 18, 8, 24, 50),
        datetime.datetime(2024, 1, 25, 11, 24, 13),
        datetime.datetime(2024, 2, 2, 8, 24, 50),
        datetime.datetime(2024, 2, 2, 8, 0, 0),
        datetime.datetime(2024, 2, 2, 17, 0, 0)
    ]

    employee_data = [
        ("John Johnman", 1, 49208238123),
        ("Dave Daveman", 1, 21341168163),
        ("Lisa Liswoman", 1, -1),
        ("Forest Forestman", 0, 49722214946)
    ]

    door_log_data = [
        (sample_date_times[0], 2, 0, "open"),
        (sample_date_times[1], 1, 0, "close"),
        (sample_date_times[5], 2, 1, "open")
    ]

    HVAC_log_data = [
        (sample_date_times[0], 1, 0, 0),
        (sample_date_times[1], 2, 0, 0),
        (sample_date_times[2], 3, 0, 0),
        (sample_date_times[3], 1, 1, 1),
        (sample_date_times[4], 2, 1, 1),
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

    config_log_data = [
        (68, 72, 73, sample_date_times[6], sample_date_times[7], 0)
    ]
