""" 
Author  : Brycen Havens
Date    : 03/15/2024
Purpose : Turns HVAC system on and off depending on the temperature the floor 
is set too.(current code only reads temp)
"""

import smbus2
from datetime import datetime

from database import Database
from typing import Tuple

class TempControl:
    # Define I2C bus number
    bus_number = 1
    # Initialize I2C bus
    bus = smbus2.SMBus(bus_number)
    TEMP_ERROR_VAL = -65

    def __init__(self, floor:int, address:int):
        self.floor = floor
        self.address = address
        self.prev_temp = self.TEMP_ERROR_VAL
        self.prev_HVAC_state = 0
        self.is_connected = True
        self.database = Database()
    # Define I2C addresses of the TC74 sensors

    def get_temp_if_changed(self) -> Tuple[bool, int]:
        '''Returns a boolean if there was a log (error or update) to the
        database. This way the GUI can update the logs page or the
        temperature'''
        is_changed, temp = self._read_temperature()
        # TODO: HVAC STUFF HERE
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

    # '''The following loop is to demonstrate the temperature readings and will 
    # be used to test the accuracy of the sensors before implementation.'''
    # try:
    #     while True:
    #         # Read temperature from sensor 1
    #         temp1 = read_temperature(floor1_address)
    #         print("Temperature Floor 1: {:.2f}°F".format(temp1))

    #         # Read temperature from sensor 2
    #         temp2 = read_temperature(floor2_address)
    #         print("Temperature Floor 2: {:.2f}°F".format(temp2))

    #         time.sleep(1)  # Wait for 1 second before reading again

    # except KeyboardInterrupt:
    #     print("Exiting...")
