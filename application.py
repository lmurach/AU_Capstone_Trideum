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
from PyQt5 import QtWidgets
from ui_form import Ui_MainWindow
from database import Database

def setUpDials(ui:Ui_MainWindow):
    """ 
    This method configures the dials with a proper range
    and connects them to their corresponding functions for updating 
    the rest of the Ui. 
    """

    # Set the range of the dials
    ui.top_floor_hvac_dial.setRange(0, 100)
    ui.middle_floor_hvac_dial.setRange(0, 100)
    ui.bottom_floor_hvac_dial.setRange(0, 100)

    # Set the initial text and value of the dials
    ui.top_floor_activate_on.setText("Active on: 00.00")
    ui.top_floor_hvac_dial.setValue(0)

    ui.middle_floor_activate_on.setText("Active on: 00.00")
    ui.middle_floor_hvac_dial.setValue(0)

    ui.bottom_floor_activate_on.setText("Active on: 00.00")
    ui.bottom_floor_hvac_dial.setValue(0)

    # Connect the dial value to the text label
    ui.top_floor_hvac_dial.valueChanged.connect(
    lambda: ui.top_floor_activate_on.setText(
    f"Active on: {ui.top_floor_hvac_dial.value()}"))

    ui.middle_floor_hvac_dial.valueChanged.connect(
    lambda: ui.middle_floor_activate_on.setText(
    f"Active on: {ui.middle_floor_hvac_dial.value()}"))

    ui.bottom_floor_hvac_dial.valueChanged.connect(
    lambda: ui.bottom_floor_activate_on.setText(
    f"Active on: {ui.bottom_floor_hvac_dial.value()}"))

    # Debuggin print statements
    # ui.top_floor_hvac_dial.valueChanged.connect(lambda: print(f"Active on: {ui.top_floor_hvac_dial.value()}"))
    # ui.middle_floor_hvac_dial.valueChanged.connect(lambda: print(f"Active on: {ui.middle_floor_hvac_dial.value()}"))
    # ui.bottom_floor_hvac_dial.valueChanged.connect(lambda: print(f"Active on: {ui.bottom_floor_hvac_dial.value()}"))

def setUpAlarm(ui:Ui_MainWindow):
    """ 
    This method connects the alarm buttons to their corresponding 
    functions. 
    """

    ui.arm_alarm_button.clicked.connect(lambda: print("Alarm Armed!")) 
    ui.disarm_alarm_button.clicked.connect(lambda: print("Alarm Disarmed!"))

def setUpDoor(ui:Ui_MainWindow):
    """ 
    This method connects the door buttons to their corresponding 
    functions. 
    """

    ui.lock_door_button.clicked.connect(lambda: print("Door unlocked!"))
    ui.unlock_door_button.clicked.connect(lambda: print("Door locked!"))

def set_up_logs(ui:Ui_MainWindow):
    """
    This method will query the database for new logs and update the list view. 
    """

    logs = Database.get_log_string_array()

    for log in logs:
        item = QtWidgets.QListWidgetItem()
        item.setText(log)
        ui.log_list.addItem(item)


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

    # Configure Some Functionality on our UI object.
    setUpDials(ui)
    setUpAlarm(ui)
    setUpDoor(ui)
    set_up_logs(ui)

    MainWindow.show()
    sys.exit(app.exec_())
    GPIO.cleanup()  
