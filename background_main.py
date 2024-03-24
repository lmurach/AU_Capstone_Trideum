""" 
Author  : Lauren Murach
Date    : 02/27/2024
Purpose : This is the main class to operate as a scheduler. Later in time 
          concurrency will be added.
"""
import time
from typing import Tuple, List
from PyQt5.QtCore import QRunnable, pyqtSlot, pyqtSignal, QObject, QThread

from RFID import RFIDSecurity
from neo_pixel_motion import NeoPixelMotion
from door import Door
from database import Database
from tempSensor import TempControl

class BackgroundMain(QObject):
    '''This serves as the "main" function for everything that is not the GUI.
    Another file keeps all the threading functions related to the background 
    processes for seperation of concerns.
    
    Concurrency model: 2 threads, GUI and background. *Maybe* 3 with the arduino
    elevator. There is a maximum of 4 threads so keeping everything on different
    threads could lead to long delays and a high possibility of a non-responsive
    GUI (if 4 threads activate so the GUI is put on the queue)'''

    card_detected = pyqtSignal(str)
    temp_signal = pyqtSignal(int, int)

    rfid = RFIDSecurity()
    door = Door()
    door.GPIO_init()
    temp_sensor = TempControl()

    def __init__(self):
        super().__init__()
        self.motion_sensor_0 = NeoPixelMotion(0, 23)
        self.motion_sensor_1 = NeoPixelMotion(1, 24)
        self.motion_sensor_2 = NeoPixelMotion(2, 25)
        self.motionsensors = [
            self.motion_sensor_0,
            self.motion_sensor_1,
            self.motion_sensor_2
        ]
        self.temp_sesors = [
            self.temp_sensor.floor1_address,
            self.temp_sensor.floor2_address
        ]

    def run(self):
        '''Main thread'''

        while True:
            self._RFID_handler()
            self._door_handler()
            self._light_handler()
            self._temp_handler()
            time.sleep(0.2)

    # @pyqtSlot()
    # def run(self):
    #     '''Main thread'''
    #     while True:
    #         # All door and RFID code is here
    #         self._RFID_handler()
    #         self._door_handler()
    #         self._light_handler()
    #         time.sleep(0.1)

    #     # while True:
    #     #     Database.set_temperature(0, 72)
    #     #     time.sleep(0.1)

    def _RFID_handler(self):
        if self.rfid.is_card_there():
            (validity, e_id) = self.rfid.handle_read_card()
            for _ in range (0, 20):
                self.rfid.is_card_there()
            if validity:
                self.door.card_owner_id = e_id
                self.card_detected.emit("Hello?")

    def _door_handler(self):
        if self.door.card_owner_id is not None:
            self.door.handle_lock()

    def _light_handler(self):
        for sensor in self.motionsensors:
            if sensor.motion_is_detected():
                sensor.turn_on_lights()
            else:
                sensor.turn_off_lights()

    def _temp_handler(self):
        temp = self.temp_sensor.read_fake_temp(self.temp_sensor.floor1_address)
        self.temp_signal.emit(1, temp)
        temp = self.temp_sensor.read_fake_temp(self.temp_sensor.floor2_address)
        self.temp_signal.emit(2, temp)
