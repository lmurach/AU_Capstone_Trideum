from main_form import Ui_MainWindow
from PyQt5 import QtWidgets
import sys

class OurMainWindow():

    def __init__(self, adoor, adb):

        self.app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.door = adoor
        self.db = adb

        self.setUpDials()
        self.setUpAlarm()
        self.setUpDoor()
        self.set_up_logs()
    
    def show(self):
        self.MainWindow.show()
        sys.exit(self.app.exec_())

    def update_top_floor_dials(self):
        self.ui.top_floor_activate_on.setText(f"Cool to: {self.ui.top_floor_hvac_dial.value()}")
        self.ui.top_floor_activate_on_split.setText(f"{self.ui.top_floor_hvac_dial.value()}")
        self.ui.top_floor_hvac_dial_split.setValue(self.ui.top_floor_hvac_dial.value())
    
    def update_top_floor_dials_split(self):
        self.ui.top_floor_activate_on.setText(f"Cool to: {self.ui.top_floor_hvac_dial_split.value()}")
        self.ui.top_floor_activate_on.setText(f"{self.ui.top_floor_hvac_dial_split.value()}")
        self.ui.top_floor_hvac_dial.setValue(self.ui.top_floor_hvac_dial_split.value())

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
        self.ui.top_floor_activate_on.setText(f"Active on: {temps[2]}")
        self.ui.top_floor_hvac_dial.setValue(temps[2])

        self.ui.top_floor_activate_on_split.setText(f"Active on: {temps[2]}")
        self.ui.top_floor_hvac_dial_split.setValue(temps[2])

        self.ui.middle_floor_activate_on.setText(f"Active on: {temps[1]}")
        self.ui.middle_floor_hvac_dial.setValue(temps[1])

        self.ui.middle_floor_activate_on_split.setText(f"Active on: {temps[1]}")
        self.ui.middle_floor_hvac_dial_split.setValue(temps[1])

        self.ui.bottom_floor_activate_on.setText(f"Active on: {temps[0]}")
        self.ui.bottom_floor_hvac_dial.setValue(temps[0])
        
        self.ui.bottom_floor_activate_on_split.setText(f"Active on: {temps[0]}")
        self.ui.bottom_floor_hvac_dial_split.setValue(temps[0])

        # Connect the dial value to the text label
        self.ui.top_floor_hvac_dial.valueChanged.connect(lambda: self.update_top_floor_dials())
        self.ui.top_floor_hvac_dial_split.valueChanged.connect(lambda: self.update_top_floor_dials_split())

        self.ui.middle_floor_hvac_dial.valueChanged.connect(
        lambda: self.ui.middle_floor_activate_on.setText(
        f"Cool to: {self.ui.middle_floor_hvac_dial.value()}"))

        self.ui.bottom_floor_hvac_dial.valueChanged.connect(
        lambda: self.ui.bottom_floor_activate_on.setText(
        f"Cool to: {self.ui.bottom_floor_hvac_dial.value()}"))

        # Debuggin print statements
        # ui.top_floor_hvac_dial.valueChanged.connect(lambda: print(f"Active on: {ui.top_floor_hvac_dial.value()}"))
        # ui.middle_floor_hvac_dial.valueChanged.connect(lambda: print(f"Active on: {ui.middle_floor_hvac_dial.value()}"))
            # ui.bottom_floor_hvac_dial.valueChanged.connect(lambda: print(f"Active on: {ui.bottom_floor_hvac_dial.value()}"))

    def setUpAlarm(self):
        """ 
        This method connects the alarm buttons to their corresponding 
        functions. 
        """

        self.ui.arm_alarm_button.clicked.connect(lambda: print("Alarm Armed!"))
        self.ui.disarm_alarm_button.clicked.connect(lambda: print("Alarm Disarmed!"))

    def setUpDoor(self):
        """ 
        This method connects the door buttons to their corresponding 
        functions. 
        """

        self.ui.lock_door_button.clicked.connect(self.door._close_lock)
        self.ui.unlock_door_button.clicked.connect(self.door._open_lock)

        self.ui.lock_door_button.clicked.connect(lambda: self.door._log_to_database(0, "close"))
        self.ui.unlock_door_button.clicked.connect(lambda: self.door._log_to_database(0, "open"))

        self.ui.lock_door_button.clicked.connect(self.set_up_logs)
        self.ui.unlock_door_button.clicked.connect(self.set_up_logs)

    def set_up_logs(self):
        """
        This method will query the database for new logs and update the list view. 
        """
        print("Setting up logs..")
        self.ui.logs_list.clear()
        logs = self.db.get_log_string_array()
        print("---")
        for log in logs:
            print(log)
        print("---")

        for log in logs:
            item = QtWidgets.QListWidgetItem()
            item.setText(log)
            self.ui.logs_list.addItem(item)