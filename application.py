"""
Author  : Wesley Cooke 
Date    : 02/12/2024
Purpose : This file shows how to add some basic functionality 
          to the GUI from the auto generated python file named 
          'ui_form.py'. 
        
        Current Features Implemented: 
        - Dial value chaning on ui
        - Alarm button setup function
        - door button setup function
        
        :TODO:       
        - Integrate Database for Dial start up. 
        - Integrate Alarm buttons with real functionality
        - Integrate Door buttons with real functionality 
        - Set up Log method for start up and integrate with database
          - Method to display new logs (Query Database?)
        
"""

# Imports. Make sure PyQt5 is properly installed
#from ui_form import Ui_MainWindow
from main_form import Ui_MainWindow
from MainWindow import OurMainWindow
from PyQt5 import QtWidgets
from PyQt5.QtCore import QThreadPool
from functools import partial
from database import Database
from door import Door
from background_main import BackgroundMain

def initiate_background_thread():
    ''' TODO: figure out why threading stuff makes this function blocking. 
    It works perfectly in the __main__ fnction but not if this function has
    those same 3 functions but are called through this'''
    pass

if __name__ == "__main__":
    """ 
    If this file is ran, it's __name__ variable will be '__main__'. 
    This protects from duplicate imports. 

    This file makes a QApplication() object and connects the Ui_MainWindow() object 
    to th
    """

    import sys
    db = Database()
    db.initialize_db()
    
    # Create a door that assoicates user id 3 with it...
    ourDoor = Door()
    ourDoor.card_owner_id = 3

    ourMainWindow = OurMainWindow(ourDoor, db)

    # L: initial integration
    # TODO: this does not work in a function and I don't know why!!
    threadpool = QThreadPool()
    bm = BackgroundMain()
    threadpool.start(bm)

    # Configure Some Functionality on our UI object.

    ourMainWindow.show()