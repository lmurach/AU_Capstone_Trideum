"""
Author  : Brycen Havens, Lauren Murach
Date    : 03/15/2024
Purpose : Turns HVAC system on and off depending on the temperature the floor 
is set too.
"""

import time
from datetime import datetime
from rpi_hardware_pwm import HardwarePWM
import RPi.GPIO as GPIO
import smbus2

from database import Database
from typing import Tuple

class TempControl:
    '''This class controls all of the temperature readings from the temperature
    sensors, the vent servomotors, and the HVAC cooler unit turning on or off.
    '''
    # Define I2C bus number
    bus_number = 1
    # Initialize I2C bus
    bus = smbus2.SMBus(bus_number)
    TEMP_ERROR_VAL = -65
    HVAC_cooler_pin = 6
    and_gate_input_pins = [13, 23, 26]
    set_temps = [75, 75, 75]
    servo_turn = 1
    servo_busy_counter = 0
    pwm = HardwarePWM(pwm_channel=1, hz=50, chip=0)

    def __init__(self, floor:int, address:int):
        self.floor = floor
        self.address = address
        self.prev_temp = self.TEMP_ERROR_VAL
        # ^ random high value so it doesn't try to turn on when the program
        # starts up
        self.prev_HVAC_is_on = False
        self.is_connected = True
        self.database = Database()
        print(GPIO.getmode())
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(TempControl.and_gate_input_pins[self.floor], GPIO.OUT)
        GPIO.setup(self.HVAC_cooler_pin, GPIO.OUT)

    def get_temp_if_changed(self) -> Tuple[bool, int]:
        '''Returns a boolean if there was a log (error or update) to the
        database. This way the GUI can update the logs page or the
        temperature. The floor_turn is a very simple implementation of a
        mutex algorithm'''
        is_changed, temp = self._read_temperature()
        if (temp > TempControl.set_temps[self.floor]+2 and
            self.floor == TempControl.servo_turn and
            TempControl.servo_busy_counter == 0 and
            self.prev_HVAC_is_on is False
            ):
            self.change_HVAC_vent_state(True)
            self.prev_HVAC_is_on = True
            is_changed = True
            TempControl.servo_busy_counter = 2
        if (temp <= TempControl.set_temps[self.floor]-2 and
            self.floor == TempControl.servo_turn and
            TempControl.servo_busy_counter == 0 and
            self.prev_HVAC_is_on is True
            ):
            self.change_HVAC_vent_state(False)
            self.prev_HVAC_is_on = False
            is_changed = True
            TempControl.servo_busy_counter = 2
        return (is_changed, temp)

    def _read_temperature(self) -> Tuple[bool, int]:
        '''The purpose of the following function is to return the 
        temperature of a requested Floor's sensor'''
        try:
            temperature_data = self.bus.read_byte_data(self.address, 0x00)
            # Read temperature register (0x00)
        except IOError:
            if self.is_connected:
                self.is_connected = False
                self._log_HVAC_error(0)
            return (True, self.TEMP_ERROR_VAL)
        temperature_fahrenheit = temperature_data * 9/5 + 32
        if not self.is_connected:
            self._log_HVAC_error(1)
            self.is_connected = True
            return (True, temperature_fahrenheit)
        # Read temp data and convert it to F,
        # (each LSB represents 1 degree Celsius)
        return (False, temperature_fahrenheit)

    def _log_HVAC_error(self, state:int) -> None:
        '''logs if the temperature sensor is disconnected/reconnected from/to
        the bus. This is possible by seeing if the I2C address is missing'''
        self.database.create_HVAC_log(
            datetime.now(),
            self.floor,
            1,
            state
        )

    def change_HVAC_vent_state(self, is_on:bool) -> bool:
        '''Controls the GPIO pins so that the HVAC vent can open or close.
        First, the PWM signal stops while the pins are changing to reduce jitter
        on the vents. Then the select pins change to high or low depending on
        the floor, then the correct servo moves with a PWM signal.'''
        if is_on:
            self._open_servo()
        else:
            self._close_servo()

    @staticmethod
    def change_HVAC_cooler_state(is_on:bool) -> None:
        '''If all vents are closed, the HVAC turns off.'''
        GPIO.output(TempControl.HVAC_cooler_pin, is_on)

    def _open_servo(self):
        '''The PWM is shared so the output must set all other GPIO pins
        to low that are connected to other AND gates and then set the correct
        pin high for its own AND gate. 5.25 is 20 degrees
        (0 is 5 and 180 is 10)'''
        GPIO.output(TempControl.and_gate_input_pins, GPIO.LOW)
        GPIO.output(TempControl.and_gate_input_pins[self.floor], GPIO.HIGH)
        TempControl.pwm.start(5.25)


    def _close_servo(self):
        '''The PWM is shared so the output must set all other GPIO pins
        to low that are connected to other AND gates and then set the correct
        pin high for its own AND gate. 8.3 is 120 degrees
        (0 is 5 and 180 is 10)'''
        GPIO.output(TempControl.and_gate_input_pins, GPIO.LOW)
        GPIO.output(TempControl.and_gate_input_pins[self.floor], GPIO.HIGH)
        TempControl.pwm.start(8.3)
