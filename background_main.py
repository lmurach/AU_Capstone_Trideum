""" 
Author  : Lauren Murach
Date    : 02/27/2024
Purpose : This is the main class to operate as a scheduler. Later in time 
          concurrency will be added.
"""
import time
from typing import Tuple, List
from PyQt5.QtCore import QRunnable, pyqtSlot

from RFID import RFIDSecurity
from neo_pixel_motion import NeoPixelMotion
from door import Door
from database import Database

class BackgroundMain(QRunnable):
    '''This serves as the "main" function for everything that is not the GUI.
    Another file keeps all the threading functions related to the background 
    processes for seperation of concerns.
    
    Concurrency model: 2 threads, GUI and background. *Maybe* 3 with the arduino
    elevator. There is a maximum of 4 threads so keeping everything on different
    threads could lead to long delays and a high possibility of a non-responsive
    GUI (if 4 threads activate so the GUI is put on the queue)'''

    def __init__(self):
        super().__init__()
        self.rfid = RFIDSecurity()
        self.door = Door()
        self.door.GPIO_init()
        self.motion_sensor_0 = NeoPixelMotion(0, 23)
        self.motion_sensor_1 = NeoPixelMotion(1, 24)
        self.motion_sensor_2 = NeoPixelMotion(2, 25)
        self.motionsensors = [self.motion_sensor_0, self.motion_sensor_1, self.motion_sensor_2]

    @pyqtSlot()
    def run(self):
        '''Main thread'''
        # rfid = RFIDSecurity()
        # door = Door()
        # motion_sensor_0 = NeoPixelMotion(0, 23)
        # motion_sensor_1 = NeoPixelMotion(1, 24)
        # motion_sensor_2 = NeoPixelMotion(2, 25)
        # motionsensors = [motion_sensor_0, motion_sensor_1, motion_sensor_2]

        while True:
            # All door and RFID code is here
            # if rfid.is_card_there():
            #     (validity, id) = rfid.handle_read_card()
            #     for _ in range (0, 20):
            #         rfid.is_card_there()
            #     if validity:
            #         door.card_owner_id = id

            # if door.card_owner_id is not None:
            #     door.handle_lock()
            # for sensor in motionsensors:
            #     if sensor.motion_is_detected():
            #         sensor.turn_on_lights()
            #     else:
            #         sensor.turn_off_lights()
            self._RFID_handler()
            self._door_handler()
            self._light_handler()
            time.sleep(0.1)

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


    def _door_handler(self):
        if self.door.card_owner_id is not None:
            self.door.handle_lock()

    def _light_handler(self):
        for sensor in self.motionsensors:
            if sensor.motion_is_detected():
                sensor.turn_on_lights()
            else:
                sensor.turn_off_lights()
