from main_form import Ui_MainWindow
from PyQt5 import QtWidgets, QtCore
from database import Database
from door import Door
from tempSensor import TempControl
from background_main import BackgroundMain
from background_elevator import BGElevator
import sys
import RPi.GPIO as GPIO
from PyQt5.QtCore import QThread

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
        # Create a thread 
        self.thread = QThread()

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
        # self.bg_elevator     = BGElevator()

        # Set up functionality for the dials, alarm, door, and logs.
        self.setUpDials()
        self.setUpAlarm()
        self.setUpDoor()
        self.set_up_logs()
        self.setUpCheckBoxes()

        self.ui.tabWidget.setCurrentIndex(0)

        # These are style sheets that we swap between for colors.
        self.GREEN  = "border: 3px solid green;\nbackground-color: lightGreen;\n"
        self.RED    = "border: 3px solid red;\nbackground-color: pink;\n"
        self.GREY   = "border: 3px solid grey;\nbackground-color: lightGrey;\n"
        self.YELLOW = "border: 3px solid yellow;\nbackground-color: lightYellow;\n"

    def show(self):
        """ This method will start the QApplication and present the user with the GUI. """
        self.MainWindow.show()
        sys.exit(self.appExec())

    def appExec(self):
        self.app.exec_()
        self.bg_task_manager.running = False
        self.thread.quit()
        self.thread.wait()
        GPIO.cleanup()
        TempControl.pwm_stop()


    def update_top_floor_dials(self):
        """ This method will activate when a user rotates the top dial from the control view."""
        # Update the text with the new value for the control and split views.
        dial_temp_value = self.ui.top_floor_hvac_dial.value()
        self.ui.top_floor_activate_on.setText(f"Cool to: {dial_temp_value}°F")
        self.ui.top_floor_activate_on_split.setText(f"{dial_temp_value}°F")
        TempControl.set_temps[2] = dial_temp_value
        # Set the split view dial to the same value.
        self.ui.top_floor_hvac_dial_split.setValue(dial_temp_value)

    def update_top_floor_dials_split(self):
        """ This method will activate when a user rotates the top dial from the split view."""
        # Update the text with the new values for the control and split views.
        dial_temp_value = self.ui.top_floor_hvac_dial_split.value()
        self.ui.top_floor_activate_on.setText(f"Cool to: {dial_temp_value}°F")
        self.ui.top_floor_activate_on_split.setText(f"{dial_temp_value}°F")
        # update the background object's set value
        TempControl.set_temps[2] = dial_temp_value
        # Set the control view dial to the same value.
        self.ui.top_floor_hvac_dial.setValue(dial_temp_value)

    def update_mid_floor_dials(self):
        """ This method will activate when a user rotates the middle dial from the control view."""
        # Update the text with the new values for the control and split views.
        dial_temp_value = self.ui.middle_floor_hvac_dial.value()
        self.ui.middle_floor_activate_on.setText(f"Cool to: {dial_temp_value}°F")
        self.ui.middle_floor_activate_on_split.setText(f"{dial_temp_value}°F")
        # update the background object's set value
        TempControl.set_temps[1] = dial_temp_value
        # Set the split view dial to the same value.
        self.ui.middle_floor_hvac_dial_split.setValue(dial_temp_value)

    def update_mid_floor_dials_split(self):
        """ This method will activate when a user rotates the middle dial from the split view."""
        # Update the text with the new values for the control and split views.
        dial_temp_value = self.ui.middle_floor_hvac_dial_split.value()
        self.ui.middle_floor_activate_on.setText(f"Cool to: {dial_temp_value}°F")
        self.ui.middle_floor_activate_on_split.setText(f"{dial_temp_value}°F")
        # update the background object's set value
        TempControl.set_temps[1] = dial_temp_value
        # Set the control view dial to the same value.
        self.ui.middle_floor_hvac_dial.setValue(dial_temp_value)

    def update_bot_floor_dials(self):
        """ This method will activate when a user rotates the bottom dial from the control view."""
        # Update the text with the new values for the control and split views.
        dial_temp_value = self.ui.bottom_floor_hvac_dial.value()
        self.ui.bottom_floor_activate_on.setText(f"Cool to: {dial_temp_value}°F")
        self.ui.bottom_floor_activate_on_split.setText(f"{dial_temp_value}°F")
        # update the background object's set value
        TempControl.set_temps[0] = dial_temp_value
        # Set the split view dial to the same value.
        self.ui.bottom_floor_hvac_dial_split.setValue(dial_temp_value)
    
    def update_bot_floor_dials_split(self):
        """ This method activates when a user rotates the bottom dial from the split view."""
        # Update the text with the new values for the control and split views.
        dial_temp_value = self.ui.bottom_floor_hvac_dial_split.value()
        self.ui.bottom_floor_activate_on.setText(f"Cool to: {dial_temp_value}°F")
        self.ui.bottom_floor_activate_on_split.setText(f"{dial_temp_value}°F")
        # update the background object's set value
        TempControl.set_temps[0] = dial_temp_value
        # Set the control view dial to the same value.
        self.ui.bottom_floor_hvac_dial.setValue(dial_temp_value)

    def setUpDials(self):
        """ 
        This method configures the dials with a proper range
        and connects them to their corresponding functions for updating 
        the rest of the Ui. 
        """
        temps = self.db.get_config_temperature_array() # basement to top
        if len(temps) == 0:
            temps = [70, 70, 70]
        TempControl.set_temps = temps

        # Set the range of the dials
        self.ui.top_floor_hvac_dial.setRange(50, 90)
        self.ui.middle_floor_hvac_dial.setRange(50, 90)
        self.ui.bottom_floor_hvac_dial.setRange(5, 90)
        
        self.ui.top_floor_hvac_dial_split.setRange(50, 90)
        self.ui.middle_floor_hvac_dial_split.setRange(50, 90)
        self.ui.bottom_floor_hvac_dial_split.setRange(50, 90)

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

        # Cleaer the old logs
        self.ui.logs_list.clear()
        self.ui.logs_list_split.clear()

        # Get the new logs
        logs = self.db.get_log_string_array()

        # Set the logs
        for log in logs:
            item = QtWidgets.QListWidgetItem()
            item.setText(log)
            self.ui.logs_list.addItem(item)

        for log in logs:
            item = QtWidgets.QListWidgetItem()
            item.setText(log)
            self.ui.logs_list_split.addItem(item)

    def arm_alarm(self) -> None:
        """
        Changes all floors to display red lights and alert of intruders
        until the alarm is disarmed.
        """
        for sensor in self.bg_task_manager.motionsensors:
            sensor.lockdown_state = True

    def disarm_alarm(self) -> None:
        """
        Removes alarm status so that all floors to display white lights 
        and do not log intrusion alerts.
        """
        for sensor in self.bg_task_manager.motionsensors:
            sensor.lockdown_state = False

    def set_temp(self, floor:int, temp:int) -> None:
        """
        A background process calls this function and sets the floor and temp 
        whenever a temperature is changed. Then the UI is changed 
        accordingly.
        """

        if (floor == 0):
            # If the temperature is above the "Cool To Temperature"
            if (temp > self.ui.bottom_floor_hvac_dial.value()):
                self.set_temp_text(floor, str(temp), self.GREEN, " ON")
            # If the temperature is less than or at the "Cool To Temperature"
            elif (temp <= self.ui.bottom_floor_hvac_dial.value()):
                self.set_temp_text(floor, str(temp), self.GREY, " OFF")

        elif (floor == 1):
        
            # If the temperature is above the "Cool To Temperature"
            if (temp > self.ui.middle_floor_hvac_dial.value()):
                self.set_temp_text(floor, str(temp), self.GREEN, " ON")
            # If the temperature is less than or at the "Cool To Temperature"
            elif (temp <= self.ui.middle_floor_hvac_dial.value()):
                self.set_temp_text(floor, str(temp), self.GREY, " OFF")

        elif (floor == 2):

            if (temp > self.ui.top_floor_hvac_dial.value()):
                self.set_temp_text(floor, str(temp), self.GREEN, " ON")

            elif (temp <= self.ui.top_floor_hvac_dial.value()):
                self.set_temp_text(floor, str(temp), self.GREY, " OFF")
    
    def set_temp_text(self, floor, text:str, color:str, state:str) -> None:
        '''Changes the text on the UI (regular view and split)
        and changes the stylesheet so that the color changes'''
        degree_text = "°F"
        short_text = text
        if text == "Not Connected":
            degree_text = ""
            short_text = "NC"
        if floor == 0:
            self.ui.bottom_floor_temp.setText(f"{text}{degree_text}{state}")
            self.ui.bottom_floor_temp_split.setText(f"{short_text}{degree_text}")
            self.ui.bottom_floor_temp.setStyleSheet(color)
            self.ui.bottom_floor_temp_split.setStyleSheet(color)
        elif floor == 1:
            self.ui.middle_floor_temp.setText(f"{text}{degree_text}{state}")
            self.ui.middle_floor_temp_split.setText(f"{short_text}{degree_text}")
            self.ui.middle_floor_temp.setStyleSheet(color)
            self.ui.middle_floor_temp_split.setStyleSheet(color)
        elif floor == 2:
            self.ui.top_floor_temp.setText(f"{text}{degree_text}{state}")
            self.ui.top_floor_temp_split.setText(f"{short_text}{degree_text}")
            self.ui.top_floor_temp.setStyleSheet(color)
            self.ui.top_floor_temp_split.setStyleSheet(color)
    
    def detect_motion(self, floor:int, state:str):
        """
        A background process calls this function with the floor and state and
        the UI is updated with the correct colors and text
        """
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
    
    def setUpCheckBoxes(self):
        """
        This method tells the check boxes on the "Log Filtering" view which method to
        call when their state has changed
        """

        self.ui.DoorCheckBox.stateChanged.connect(lambda:self.logFilteringStateChanged())
        self.ui.HVAC_CheckBox.stateChanged.connect(lambda:self.logFilteringStateChanged())
        self.ui.ElevatorCheckBox.stateChanged.connect(lambda:self.logFilteringStateChanged())
        self.ui.MotionSensorCheckBox.stateChanged.connect(lambda:self.logFilteringStateChanged())
        self.ui.AfterHoursDoorCheckBox.stateChanged.connect(lambda:self.logFilteringStateChanged())
        self.ui.AfterHoursMotionCheckBox.stateChanged.connect(lambda:self.logFilteringStateChanged())
        self.ui.HardwareAlertsCheckBox.stateChanged.connect(lambda:self.logFilteringStateChanged())
    
    def logFilteringStateChanged(self):
        """
        logFilteringStateChanged is desinged to be called when one of the 
        check boxes change state on the "Log Filtering" view. 
        This method will gather the current states and send it to the database.
        """

        self.states = [
        self.ui.MotionSensorCheckBox.isChecked(),
        self.ui.AfterHoursMotionCheckBox.isChecked(),
        self.ui.ElevatorCheckBox.isChecked(),
        self.ui.HVAC_CheckBox.isChecked(),
        self.ui.DoorCheckBox.isChecked(),
        self.ui.AfterHoursDoorCheckBox.isChecked(),
        self.ui.HardwareAlertsCheckBox.isChecked()]
        print(self.states)

        Database.log_filtering_is_on = self.states
        self.set_up_logs()
    
    def update_requested(self, bsList):
        """ 
        This method updates the state of the elevator boxes. If a specific floor is in the 
        requested list, it will change that box to yellow. 
        """

        # Updates for the bottom floor. 
        current_floor = bsList[3]

        if (current_floor == 0):
            self.ui.bottom_floor_elevator.setStyleSheet(self.GREEN)
            self.ui.bottom_floor_elevator_split.setStyleSheet(self.GREEN)

            self.ui.bottom_floor_elevator.setText("HERE")
            self.ui.bottom_floor_elevator_split.setText("HERE")
        else:
            if (0 in bsList):
                self.ui.bottom_floor_elevator.setStyleSheet(self.YELLOW)
                self.ui.bottom_floor_elevator_split.setStyleSheet(self.YELLOW)

                self.ui.bottom_floor_elevator.setText("Requested")
                self.ui.bottom_floor_elevator_split.setText("REQ")
                
            else:
                self.ui.bottom_floor_elevator.setStyleSheet(self.GREY)
                self.ui.bottom_floor_elevator_split.setStyleSheet(self.GREY)
                
                self.ui.bottom_floor_elevator.setText("Not Here")
                self.ui.bottom_floor_elevator_split.setText("Not Here")
        
        # Updates for the middle floor
        if (current_floor == 1):
            self.ui.middle_floor_elevator.setStyleSheet(self.GREEN)
            self.ui.middle_floor_elevator_split.setStyleSheet(self.GREEN)

            self.ui.middle_floor_elevator.setText("HERE")
            self.ui.middle_floor_elevator_split.setText("HERE")
        else: 
            if (1 in bsList):
                self.ui.middle_floor_elevator.setStyleSheet(self.YELLOW)
                self.ui.middle_floor_elevator_split.setStyleSheet(self.YELLOW)

                self.ui.middle_floor_elevator.setText("Requested")
                self.ui.middle_floor_elevator_split.setText("REQ")
            else:
                self.ui.middle_floor_elevator.setStyleSheet(self.GREY)
                self.ui.middle_floor_elevator_split.setStyleSheet(self.GREY)

                self.ui.middle_floor_elevator.setText("Not Here")
                self.ui.middle_floor_elevator_split.setText("Not Here")
        
        # Updates for the top floor
        if (current_floor == 2):
            self.ui.top_floor_elevator.setStyleSheet(self.GREEN)
            self.ui.top_floor_elevator_split.setStyleSheet(self.GREEN)

            self.ui.top_floor_elevator.setText("HERE")
            self.ui.top_floor_elevator_split.setText("HERE")
        else:
            if (2 in bsList):
                self.ui.top_floor_elevator.setStyleSheet(self.YELLOW)
                self.ui.top_floor_elevator_split.setStyleSheet(self.YELLOW)

                self.ui.top_floor_elevator.setText("Requested")
                self.ui.top_floor_elevator_split.setText("REQ")
            else:
                self.ui.top_floor_elevator.setStyleSheet(self.GREY)
                self.ui.top_floor_elevator_split.setStyleSheet(self.GREY)

                self.ui.top_floor_elevator.setText("Not Here")
                self.ui.top_floor_elevator_split.setText("Not Here")
