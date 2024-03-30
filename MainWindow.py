from main_form import Ui_MainWindow
from PyQt5 import QtWidgets, QtCore
from database import Database
from door import Door
from background_main import BackgroundMain
import sys

class OurMainWindow():
    """ 
    This object sets up the UI elements and has control over all updates
    that are displayed on the UI.
    """

    def __init__(self, adoor:Door, adb: Database):
        """
        Constructor. Our UI needs a Door object and a Database object.
        The door object will give us updates for the RFID door. 
        The database object will allow us to pull information from our database and 
        store new data there.
        """

        # Create a QApplication using Pyqt5
        self.app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()

        # Load the UI class that is generated from piuic5
        self.ui = Ui_MainWindow()

        # Allow the UI to use our QMainWindow object
        self.ui.setupUi(self.MainWindow)

        # Keep the door and database as class members.
        self.door = adoor
        self.db = adb
        self.bg_task_manager = BackgroundMain()

        # Set up functionality for the dials, alarm, door, and logs.
        self.setUpDials()
        self.setUpAlarm()
        self.setUpDoor()
        self.set_up_logs()

        # These are style sheets that we swap between for colors.
        self.GREEN = "border: 3px solid green;\nborder-radius: 40px;\nbackground-color: lightGreen;\n"
        self.RED   = "border: 3px solid red;\nborder-radius: 40px;\nbackground-color: pink;\n"
        self.GREY  = "border: 3px solid grey;\nborder-radius: 40px;\nbackground-color: lightGrey;\n"

    def show(self):
        """ This method will start the QApplication and present the user with the GUI. """
        self.MainWindow.show()
        sys.exit(self.app.exec_())

    def update_top_floor_dials(self):
        """ This method will activate when a user rotates the top dial from the control view."""
        
        # Update the text with the new value for the control and split views.
        self.ui.top_floor_activate_on.setText(f"Cool to: {self.ui.top_floor_hvac_dial.value()}°F")
        self.ui.top_floor_activate_on_split.setText(f"{self.ui.top_floor_hvac_dial.value()}°F")
        # Set the split view dial to the same value.
        self.ui.top_floor_hvac_dial_split.setValue(self.ui.top_floor_hvac_dial.value())
    
    def update_top_floor_dials_split(self):
        """ This method will activate when a user rotates the top dial from the split view."""

        # Update the text with the new values for the control and split views.
        self.ui.top_floor_activate_on.setText(f"Cool to: {self.ui.top_floor_hvac_dial_split.value()}°F")
        self.ui.top_floor_activate_on_split.setText(f"{self.ui.top_floor_hvac_dial_split.value()}°F")
        # Set the control view dial to the same value.
        self.ui.top_floor_hvac_dial.setValue(self.ui.top_floor_hvac_dial_split.value())

    def update_mid_floor_dials(self):
        """ This method will activate when a user rotates the middle dial from the control view."""
        # Update the text with the new values for the control and split views.
        self.ui.middle_floor_activate_on.setText(f"Cool to: {self.ui.middle_floor_hvac_dial.value()}°F")
        self.ui.middle_floor_activate_on_split.setText(f"{self.ui.middle_floor_hvac_dial.value()}°F")
        # Set the split view dial to the same value. 
        self.ui.middle_floor_hvac_dial_split.setValue(self.ui.middle_floor_hvac_dial.value())
    
    def update_mid_floor_dials_split(self):
        """ This method will activate when a user rotates the middle dial from the split view."""
        # Update the text with the new values for the control and split views.
        self.ui.middle_floor_activate_on.setText(f"Cool to: {self.ui.middle_floor_hvac_dial_split.value()}°F")
        self.ui.middle_floor_activate_on_split.setText(f"{self.ui.middle_floor_hvac_dial_split.value()}°F")
        # Set the control view dial to the same value.
        self.ui.middle_floor_hvac_dial.setValue(self.ui.middle_floor_hvac_dial_split.value())
    
    def update_bot_floor_dials(self):
        """ This method will activate when a user rotates the bottom dial from the control view."""
        # Update the text with the new values for the control and split views.
        self.ui.bottom_floor_activate_on.setText(f"Cool to: {self.ui.bottom_floor_hvac_dial.value()}°F")
        self.ui.bottom_floor_activate_on_split.setText(f"{self.ui.bottom_floor_hvac_dial.value()}°F")
        # Set the split view dial to the same value.
        self.ui.bottom_floor_hvac_dial_split.setValue(self.ui.bottom_floor_hvac_dial.value())
    
    def update_bot_floor_dials_split(self):
        """ This method activates when a user rotates the bottom dial from the split view."""
        # Update the text with the new values for the control and split views.
        self.ui.bottom_floor_activate_on.setText(f"Cool to: {self.ui.bottom_floor_hvac_dial_split.value()}°F")
        self.ui.bottom_floor_activate_on_split.setText(f"{self.ui.bottom_floor_hvac_dial_split.value()}°F")
        # Set the control view dial to the same value.
        self.ui.bottom_floor_hvac_dial.setValue(self.ui.bottom_floor_hvac_dial_split.value())

    def setUpDials(self):
        """ 
        This method configures the dials with a proper range
        and connects them to their corresponding functions for updating 
        the rest of the Ui. 
        """
        temps = self.db.get_config_temperature_array() # basement to top

        # Set the range of the dials
        self.ui.top_floor_hvac_dial.setRange(0, 100)
        self.ui.middle_floor_hvac_dial.setRange(0, 100)
        self.ui.bottom_floor_hvac_dial.setRange(0, 100)
        
        self.ui.top_floor_hvac_dial_split.setRange(0, 100)
        self.ui.middle_floor_hvac_dial_split.setRange(0, 100)
        self.ui.bottom_floor_hvac_dial_split.setRange(0, 100)

        # Set the initial text and value of the dials
        self.ui.top_floor_activate_on.setText(f"Cool to: {temps[2]}°F")
        self.ui.top_floor_hvac_dial.setValue(temps[2])

        self.ui.top_floor_activate_on_split.setText(f"{temps[2]}°F")
        self.ui.top_floor_hvac_dial_split.setValue(temps[2])

        self.ui.middle_floor_activate_on.setText(f"Cool to: {temps[1]}°F")
        self.ui.middle_floor_hvac_dial.setValue(temps[1])

        self.ui.middle_floor_activate_on_split.setText(f"{temps[1]}°F")
        self.ui.middle_floor_hvac_dial_split.setValue(temps[1])

        self.ui.bottom_floor_activate_on.setText(f"Cool to: {temps[0]}°F")
        self.ui.bottom_floor_hvac_dial.setValue(temps[0])
        
        self.ui.bottom_floor_activate_on_split.setText(f"{temps[0]}°F")
        self.ui.bottom_floor_hvac_dial_split.setValue(temps[0])

        # Connect the dial value to the text label
        self.ui.top_floor_hvac_dial.valueChanged.connect(lambda: self.update_top_floor_dials())
        self.ui.top_floor_hvac_dial_split.valueChanged.connect(lambda: self.update_top_floor_dials_split())

        self.ui.middle_floor_hvac_dial.valueChanged.connect(lambda: self.update_mid_floor_dials())
        self.ui.middle_floor_hvac_dial_split.valueChanged.connect(lambda: self.update_mid_floor_dials_split())

        self.ui.bottom_floor_hvac_dial.valueChanged.connect(lambda: self.update_bot_floor_dials())
        self.ui.bottom_floor_hvac_dial_split.valueChanged.connect(lambda: self.update_bot_floor_dials_split())

        # Debuggin print statements
        # ui.top_floor_hvac_dial.valueChanged.connect(lambda: print(f"Active on: {ui.top_floor_hvac_dial.value()}"))
        # ui.middle_floor_hvac_dial.valueChanged.connect(lambda: print(f"Active on: {ui.middle_floor_hvac_dial.value()}"))
            # ui.bottom_floor_hvac_dial.valueChanged.connect(lambda: print(f"Active on: {ui.bottom_floor_hvac_dial.value()}"))

    def setUpAlarm(self):
        """ 
        This method connects the alarm buttons to their corresponding 
        functions. 
        """

        self.ui.arm_alarm_button.clicked.connect(self.arm_alarm)
        self.ui.disarm_alarm_button.clicked.connect(self.disarm_alarm)

    def setUpDoor(self):
        """ 
        This method connects the door buttons to their corresponding 
        functions. 
        """

        self.ui.lock_door_button.clicked.connect(self.door.close_lock)
        self.ui.unlock_door_button.clicked.connect(self.door.open_lock)

        self.ui.lock_door_button.clicked.connect(lambda: self.door._log_to_database(0, "close"))
        self.ui.unlock_door_button.clicked.connect(lambda: self.door._log_to_database(0, "open"))

        self.ui.lock_door_button.clicked.connect(self.set_up_logs)
        self.ui.unlock_door_button.clicked.connect(self.set_up_logs)

    def set_up_logs(self):
        """
        This method will query the database for new logs and update the list view. 
        """
        self.ui.logs_list.clear()
        self.ui.logs_list_split.clear()
        logs = self.db.get_log_string_array()

        for log in logs:
            item = QtWidgets.QListWidgetItem()
            item.setText(log)
            self.ui.logs_list.addItem(item)

        for log in logs:
            item = QtWidgets.QListWidgetItem()
            item.setText(log)
            self.ui.logs_list_split.addItem(item)

    def arm_alarm(self) -> None:
        '''Changes all floors to display red lights and alert of intruders
        until the alarm is disarmed.'''
        for sensor in self.bg_task_manager.motionsensors:
            sensor.lockdown_state = True

    def disarm_alarm(self) -> None:
        '''Removes alarm status so that all floors to display white lights 
        and do not log intrusion alerts.'''
        for sensor in self.bg_task_manager.motionsensors:
            sensor.lockdown_state = False

    def set_temp(self, floor:int, temp:int) -> None:
        '''A background process calls this function and sets the floor and temp 
        whenever a temperature is changed. Then the UI is changed 
        accordingly.'''

        if (floor == 0):
            # This sensor is disconnected and should never emit a signal.
            print("How'd you get here?")

        elif (floor == 1):
        
            # If the temperature is above the "Cool To Temperature"
            if (temp > self.ui.middle_floor_hvac_dial.value()):
                # Set the text on the control and split view.
                self.ui.middle_floor_temp.setText(f"{str(temp)}°F ON")
                self.ui.middle_floor_temp_split.setText(f"{str(temp)}°F")
                # Change the Style Sheet
                self.ui.middle_floor_temp.setStyleSheet(self.GREEN)
                self.ui.middle_floor_temp_split.setStyleSheet(self.GREEN)
            # If the temperature is less than or at the "Cool To Temperature"
            elif (temp <= self.ui.middle_floor_hvac_dial.value()):
                # Set the text on the control and split view.
                self.ui.middle_floor_temp.setText(f"{str(temp)}°F OFF")
                self.ui.middle_floor_temp_split.setText(f"{str(temp)}°F")
                # Change the Style Sheet
                self.ui.middle_floor_temp.setStyleSheet(self.GREY)
                self.ui.middle_floor_temp_split.setStyleSheet(self.GREY)

        elif (floor == 2):

            if (temp > self.ui.top_floor_hvac_dial.value()):
                self.ui.top_floor_temp.setText(f"{str(temp)}°F ON")
                self.ui.top_floor_temp_split.setText(f"{str(temp)}°F")
                self.ui.top_floor_temp.setStyleSheet(self.GREEN)
                self.ui.top_floor_temp_split.setStyleSheet(self.GREEN)

            elif (temp <= self.ui.top_floor_hvac_dial.value()):
                self.ui.top_floor_temp.setText(f"{str(temp)}°F OFF")
                self.ui.top_floor_temp_split.setText(f"{str(temp)}°F")
                self.ui.top_floor_temp.setStyleSheet(self.GREY)
                self.ui.top_floor_temp_split.setStyleSheet(self.GREY)
    
    def detect_motion(self, floor:int, state:str):
        '''A background process calls this function with the floor and state and
        the UI is updated with the correct colors and text'''
        if floor == 2:
            if state == "off":
                self.ui.top_floor_motion_split.setStyleSheet(self.GREY)
                self.ui.top_floor_motion.setStyleSheet(self.GREY)
                self.ui.top_floor_motion.setText("NO MOTION")
                self.ui.top_floor_motion_split.setText("NONE")

            elif state == "on":
                self.ui.top_floor_motion.setStyleSheet(self.GREEN)
                self.ui.top_floor_motion_split.setStyleSheet(self.GREEN)
                self.ui.top_floor_motion.setText("MOTION DETECTED")
                self.ui.top_floor_motion_split.setText("MOTION")
        
        elif floor == 1:
            if state == "off":
                self.ui.middle_floor_motion_split.setStyleSheet(self.GREY)
                self.ui.middle_floor_motion.setStyleSheet(self.GREY)
                self.ui.middle_floor_motion.setText("NO MOTION")
                self.ui.middle_floor_motion_split.setText("NONE")

            elif state == "on":
                self.ui.middle_floor_motion.setStyleSheet(self.GREEN)
                self.ui.middle_floor_motion_split.setStyleSheet(self.GREEN)
                self.ui.middle_floor_motion.setText("MOTION DETECTED")
                self.ui.middle_floor_motion_split.setText("MOTION")
        
        elif floor == 0:
            if state == "off":
                self.ui.bottom_floor_motion_split.setStyleSheet(self.GREY)
                self.ui.bottom_floor_motion.setStyleSheet(self.GREY)
                self.ui.bottom_floor_motion.setText("NO MOTION")
                self.ui.bottom_floor_motion_split.setText("NONE")

            elif state == "on":
                self.ui.bottom_floor_motion.setStyleSheet(self.GREEN)
                self.ui.bottom_floor_motion_split.setStyleSheet(self.GREEN)
                self.ui.bottom_floor_motion.setText("MOTION DETECTED")
                self.ui.bottom_floor_motion_split.setText("MOTION")