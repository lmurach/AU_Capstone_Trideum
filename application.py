"""
Author  : Wesley Cooke 
Date    : 02/12/2024  
Purpose : This file shows how to add some basic functionality 
          to the GUI from the auto generated python file named 
          'ui_form.py'. 
        
        Current Features Implemented: 
        - Unlock and Lock door buttons work with physical system
        - Dial changes the "cool to" temp
        - Buttons generatore appropriate logs inthe database
        - Logs can be filtereted according to some criteria
        - Temperature labels show the current temperature
        - Motion blocks light up when motion has been detected. 
        - Arduino communicates the requested queue to the GUI.
        - Alarm buttons function 

        :TODO:       
        - Save temperature dial value to database on close
        - integrate elevator functionality 
        - integrate hvac 

Last Updated : 04/15/2024 - WC
"""

# Imports. Make sure PyQt5 is properly installed
from main_form import Ui_MainWindow
from MainWindow import OurMainWindow
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QThread
from functools import partial
from database import Database
from door import Door
from background_main import BackgroundMain
import sys

def initiate_background_thread():
    ''' TODO: figure out why threading stuff makes this function blocking. 
    It works perfectly in the __main__ fnction but not if this function has
    those same 3 functions but are called through this'''
    pass

# The following slots are for updates from the background threads

@QtCore.pyqtSlot()
def update_logs():
    # When needed, update the logs for the GUI 
    ourMainWindow.set_up_logs()

@QtCore.pyqtSlot(int)
def get_temp(floor:int, temp:int, is_connected:bool):
    # When needed, set the temperature on the GUI 
    if not is_connected:
        ourMainWindow.set_temp_text(
            floor,
            "Not Connected",
            ourMainWindow.GREY,
            "")
    else:
        ourMainWindow.set_temp(floor, temp)

@QtCore.pyqtSlot(int, str)
def detect_motion(num, state):
    # When needed, update the motion blocks
    ourMainWindow.detect_motion(num, state)

@QtCore.pyqtSlot(list)
def update_requested(bsList):
    # When needed, update the requested blocks for the elevator
    ourMainWindow.update_requested(bsList)


if __name__ == "__main__":
    """ 
    If this file is ran, it's __name__ variable will be '__main__'. 
    This protects from duplicate imports. 

    This file instantiates all the main objects for the life
    of our program.
    """
    ### GLOBAL VARS ### 
    # Create a door that assoicates user id 3 with it...
    db = Database()
    db.initialize_db()
    ourDoor = Door()
    ourDoor.card_owner_id = 3
    ourMainWindow = OurMainWindow(ourDoor, db)

    # L: initial integration
    # TODO: this does not work in a function and I don't know why!!
    ## 
    # Set up the background thread
    bm = ourMainWindow.bg_task_manager
    thread = QThread()
    bm.moveToThread(thread)
    thread.started.connect(bm.run)
    bm.temp_signal.connect(get_temp)
    bm.motion_signal.connect(detect_motion)
    bm.logs_changed.connect(update_logs)

    # # Set up the Elevator thread
    bge = ourMainWindow.bg_elevator
    eThread = QThread()
    bge.moveToThread(eThread)
    eThread.started.connect(bge.run)
    bge.button_signal.connect(update_requested)

    # Start the Threads
    thread.start()
    eThread.start()

    # Finally show the window
    ourMainWindow.show()
