""" 
Author  : Lauren Murach
Date    : 02/13/2024
Purpose : The RFID class handles all security and utility related to the RFID 
          module. 
"""

from datetime import datetime, timedelta
from rpi_hardware_pwm import HardwarePWM
import RPi.GPIO as GPIO

from database import Database

class Door:
    '''The door has a locking mechanism controlled by a servomotor. This locking mechanism 
    only locks after a certain amount of time or when the door is shut. This is 
    accomplished with a magnatic reed switch switch, which detects if the 
    door is closed (active low). There is also a light and alert which is triggered 
    when the door is open too long.'''

    def __init__(self, card_owner_id):
        self.card_owner_id = card_owner_id
        self.state:str = "ready_to_open"
        self.time_until_run:datetime = datetime.now()
        self.seconds_door_open:int = 0
        self.alert_sent:bool = False
        self.pin = 27

    def GPIO_init(self):
        '''Initilaizes the correct GPIO board type and makes the pin for the 
        alert LED an output pin'''
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
        GPIO.output(self.pin, 0)

    def handle_lock(self):
        '''The locking mechanism is normally blocking. To get around this, a 
        state machine is used. The class manages state and performs very short
        tasks and then allows the Pi to run other code until a certain time is
        passed. This time is non-critical so no critical interrupts need to be
        used for these operations.
        
        The states are:
                            V--┐
        ready_to_open ---> open ┘--> ready_to_close ---> closed --> ...'''
        if self.state == "ready_to_open":
            Door._open_lock()
            self._add_wait_time(4, 0)
            self.state = "open"
            self.seconds_door_open += 4
            return 1
        if self.state == "open":
            if Door._is_door_closed():
                self._add_wait_time(0, 500)
                self.state = "ready_to_close"
                self._log_to_database(0, "open")
            elif self.seconds_door_open >= 10 and not self.alert_sent:
                self._alert_door_ajar()
            else:
                seconds_to_wait = 1
                self._add_wait_time(seconds_to_wait, 0)
                self.seconds_door_open += seconds_to_wait
            return 1
        if self.state == "ready_to_close":
            Door._close_lock()
            self._add_wait_time(1, 0)
            self.state = "closed"
            return 1
        if self.state == "closed":
            self._clear_alert()
            self._log_to_database(0, "close")
            self.state = "ready_to_open"
            return 0

    def _add_wait_time(self, seconds:int, milliseconds:int):
        '''Adds a set amount of time to wait until the next state 
        can be activated. The seconds must be an integer so any
        fraction of a second must bleed into the milliseconds variable'''

        self.time_until_run = datetime.now() + \
            timedelta(seconds=seconds, milliseconds=milliseconds)

    def _alert_door_ajar(self):
        '''If the door is open too long, the alert is logged to the database
        to ensure that people are not holding the secure door open too long.'''
        self.alert_sent = True
        GPIO.output(self.pin, 1)
        self._log_to_database(1, "open")

    def _clear_alert(self):
        '''This function is called after the door is closed to finalize the alert
        state by logging to the database again and turning off the lights'''
        self.alert_sent = False
        GPIO.output(self.pin, 0)
        print("door closed")

    def _log_to_database(self, is_alert:int, state:str):
        Database.create_door_log(datetime.now(), self.card_owner_id, is_alert, state)

    @staticmethod
    def _open_lock():
        '''The servomotor accepts a 50hz signal with a 1-2 ms pulse,
        so this function generates a duty cycle of 5% (1ms) for
        a degree of 0 turn (open)'''
        pwm = HardwarePWM(pwm_channel = 0, hz = 50, chip = 0)
        pwm.start(5)

    @staticmethod
    def _close_lock():
        '''The servomotor accepts a 50hz signal with a 1-2 ms pulse,
        so this function generates a duty cycle of 10% (2ms) for
        a degree of 90 turn (closed)'''
        pwm = HardwarePWM(pwm_channel = 0, hz = 50, chip = 0)
        pwm.start(10)

    @staticmethod
    def _is_door_closed():
        pin = 17
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        state = GPIO.input(pin)
        # reed_switch = push_button.PushButton(21)
        # state = reed_switch.GetState()
        return state

def fake_loop(rfid_obj:Door):
    '''A test demo of the concurrency functionality'''
    while 1:
        if rfid_obj.time_until_run < datetime.now():
            if rfid_obj.handle_lock() == 0:
                return
        for i in range(1, 10):
            print(i)

def debug_console(rfid_obj:Door):
    '''A test method to show the open_lock and close_lock functions
    in a demo.'''
    rfid_obj.GPIO_init()
    while 1:
        response = input("Enter your door command: ")
        if response == "open":
            fake_loop(rfid_obj)

if __name__ == '__main__':
    rfid_obj = Door("Someone")
    debug_console(rfid_obj)
