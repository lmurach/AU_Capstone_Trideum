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
from ui_5 import Ui_MainWindow
from PyQt5 import QtWidgets
from database import Database
from door import Door
from functools import partial

def setUpDials(ui:Ui_MainWindow):
    """ 
    This method configures the dials with a proper range
    and connects them to their corresponding functions for updating 
    the rest of the Ui. 
    """
    temps = Database.get_config_temperature_array() # basement to top 

    # Set the range of the dials
    ui.top_floor_hvac_dial_4.setRange(0, 100)
    ui.middle_floor_hvac_dial_4.setRange(0, 100)
    ui.bottom_floor_hvac_dial_4.setRange(0, 100)

    # Set the initial text and value of the dials
    ui.top_floor_activate_on_4.setText(f"Active on: {temps[2]}")
    ui.top_floor_hvac_dial_4.setValue(temps[2])

    ui.middle_floor_activate_on_4.setText(f"Active on: {temps[1]}")
    ui.middle_floor_hvac_dial_4.setValue(temps[1])

    ui.bottom_floor_activate_on_4.setText(f"Active on: {temps[0]}")
    ui.bottom_floor_hvac_dial_4.setValue(temps[0])

    # Connect the dial value to the text label
    ui.top_floor_hvac_dial_4.valueChanged.connect(
    lambda: ui.top_floor_activate_on_4.setText(
    f"Active on: {ui.top_floor_hvac_dial_4.value()}"))

    ui.middle_floor_hvac_dial_4.valueChanged.connect(
    lambda: ui.middle_floor_activate_on_4.setText(
    f"Active on: {ui.middle_floor_hvac_dial_4.value()}"))

    ui.bottom_floor_hvac_dial_4.valueChanged.connect(
    lambda: ui.bottom_floor_activate_on_4.setText(
    f"Active on: {ui.bottom_floor_hvac_dial_4.value()}"))

    # Debuggin print statements
    # ui.top_floor_hvac_dial.valueChanged.connect(lambda: print(f"Active on: {ui.top_floor_hvac_dial.value()}"))
    # ui.middle_floor_hvac_dial.valueChanged.connect(lambda: print(f"Active on: {ui.middle_floor_hvac_dial.value()}"))
    # ui.bottom_floor_hvac_dial.valueChanged.connect(lambda: print(f"Active on: {ui.bottom_floor_hvac_dial.value()}"))

def setUpAlarm(ui:Ui_MainWindow):
    """ 
    This method connects the alarm buttons to their corresponding 
    functions. 
    """

    ui.arm_alarm_button_4.clicked.connect(lambda: print("Alarm Armed!")) 
    ui.disarm_alarm_button_4.clicked.connect(lambda: print("Alarm Disarmed!"))

def setUpDoor(ui:Ui_MainWindow, aDoor:Door):
    """ 
    This method connects the door buttons to their corresponding 
    functions. 
    """

    ui.lock_door_button_4.clicked.connect(lambda: aDoor._close_lock())
    ui.unlock_door_button_4.clicked.connect(lambda: aDoor._open_lock())

    ui.lock_door_button_4.clicked.connect(lambda: aDoor._log_to_database(0, "close"))
    ui.unlock_door_button_4.clicked.connect(lambda: aDoor._log_to_database(0, "open"))

    ui.lock_door_button_4.clicked.connect(lambda: set_up_logs(ui))
    ui.unlock_door_button_4.clicked.connect(lambda: set_up_logs(ui))

def set_up_logs(ui:Ui_MainWindow):
    """
    This method will query the database for new logs and update the list view. 
    """
    print("Setting up logs..")
    ui.listWidget.clear()
    logs = Database.get_log_string_array()
    print("---")
    for log in logs:
        print(log)
    print("---")

    for log in logs:
        item = QtWidgets.QListWidgetItem()
        item.setText(log)
        ui.listWidget.addItem(item)

def setup_menus(ui:Ui_MainWindow):
    """ Fill this out later wesley """
    ui.logs_btn.clicked.connect(ui.click_change_page)

if __name__ == "__main__":
    """ 
    If this file is ran, it's __name__ variable will be '__main__'. 
    This protects from duplicate imports. 

    This file makes a QApplication() object and connects the Ui_MainWindow() object 
    to th
    """
    import sys
    Database.initialize_db()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.stackedWidget.setCurrentWidget(ui.page_3)
    
    # Create a door that assoicates user id 3 with it... 
    ourDoor = Door(3)

    # Configure Some Functionality on our UI object.
    setUpDials(ui)
    setUpAlarm(ui)
    setUpDoor(ui, ourDoor)
    set_up_logs(ui)
    setup_menus(ui)

    MainWindow.show()
    sys.exit(app.exec_())
    GPIO.cleanup()  
