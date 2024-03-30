""" 
Author  : Brycen Havens
Date    : 03/15/2024
Purpose : Turns HVAC system on and off depending on the temperature the floor is set too.(current code only reads temp)
"""

import smbus2
import time
from random import Random


class TempControl:
    rand = Random()
    # Define I2C bus number
    bus_number = 1

    # Define I2C addresses of the TC74 sensors
    floor1_address = 0x48  # Address of the TC74A0
    floor2_address = 0x4D  # Address of the TC74A5

    # Initialize I2C bus
    bus = smbus2.SMBus(bus_number)

    '''The purpose of the following function is to return the 
    temperature of a requested Floor's sensor'''
    def read_temperature(self, sensor_address):
        temperature_data = self.bus.read_byte_data(sensor_address, 0x00) # Read temperature register (0x00)
        temperature_fahrenheit = temperature_data * 9/5 + 32 # Read temp data and convert it to F, (each LSB represents 1 degree Celsius)
        return temperature_fahrenheit
    
    def read_fake_temp(self, sensor_address) -> int:
        '''ONLY FOR TESTING INTEGRATION FOR WHEN THE HARDWARE IS GONE. 
        Returns a random integer between 70 and 79'''
        return self.rand.randint(70, 80)

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
