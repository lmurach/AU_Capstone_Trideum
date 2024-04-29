from signal import pause
import time
from gpiozero import MotionSensor
#these three imports are used for the motion sensors.
#The gpiozero library should come preinstalled on the Raspberry Pi OS
#if gpiozero is not on your Pi, run "python3 -m pip install gpiozero" in cmd to install it
import board
import neopixel
#these two imports require the Adafruit_Blinka and Adafruit_Blinka_Neopixel libraries to function
#For more information on these libraries, please check https://learn.adafruit.com/neopixels-on-raspberry-pi/python-usage

from database import Database

class NeoPixelMotion:
    '''Runs Lighting and motion sensor controls, pulling lockdown_state 
    from an external source'''

    lockdown_state = False
    pixel_pin = board.D21
    strand_length = 90
    color_order = neopixel.GRB
    pixels = neopixel.NeoPixel(
        pixel_pin,
        strand_length,
        pixel_order = color_order,
        auto_write = False
    )
    #above code initializes the Neopixels
    time_dif = 5
    #initializing timer variables.
    def __init__ (self, floor, pir_pin):
        self.floor = floor
        self.pir_pin = pir_pin
        #The test strand we used is 30 LEDs long. D18 is GPIO18.
        #For GPIO18 to work, audio must be disabled
        self.pir = MotionSensor(pir_pin)
        self.start_time = 0
        self.sense_time = 0
        #above code initializes the motion sensors on each floor.
        #GPIO 23 recieves data from the basement sensor
        #GPIO 24 recieves data from the first floor sensor
        #GPIO 25 recieves data from 2nd floor sensor.

        #the following code controls each floor based on motion sensor readings
        #There is a delay of 5 minutes between changes in lighting.
        #To test this easier, change timeDif to the number of seconds 
        #between changes you want.
        #in this example, floor 0 is pixels 0-9, floor 1 is pixels 10-19, 
        #and floor 2 is pixels 20-29

        # L: added a database class instance here for all db calls
        self.db = Database()

    def motion_is_detected(self):
        """Returns motion_detected"""
        return self.pir.motion_detected

    def is_time(self) -> bool:
        '''Returns true if enough time has passed for the lights to turn on
        or off'''
        if self.sense_time - self.start_time >= self.time_dif:
            return True
        return False

    def turn_on_lights(self):
        """Function activiating lights on the target floor"""
        if self.is_time():     #only activates if timeDif's value in seconds has passed since the last update
            if self.lockdown_state:
                for i in range(30):
                    self.pixels[i + (self.floor * 30)] = (100, 0, 0)          #lights turn red if motion is detected during a lockdown
            else:
                for i in range(30):
                    self.pixels[i + (self.floor * 30)] = (100, 100, 100)      #lights turn white if motion is detected during open hours
            # L: added a database call here so that the motion alert is changed
            self.db.create_motion_log(self.floor, self.lockdown_state)          
            self.pixels.show()
        self.start_time = time.time()                     #updates the starttime0 variable to reset timer.

    # def turn_on_lights_raw(self):
    #     """Function activiating lights on the target floor"""
    #     if self.lockdown_state:
    #         for i in range(10):
    #             self.pixels[i + (self.floor * 10)] = (255, 0, 0)          #lights turn red if motion is detected during a lockdown
    #     else:
    #         for i in range(10):
    #             self.pixels[i + (self.floor * 10)] = (255, 255, 255)      #lights turn white if motion is detected during open hours
    #     # L: added a database call here so that the motion alert is changed        
    #     self.pixels.show()

    def turn_off_lights(self):
        """Function for determining if lights should turn off in the target floor"""
        self.sense_time = time.time()                     #updates the sensetime0 variable to perform a comparison with starttime0
        if self.is_time():     #only activates if timeDif's value in seconds has passed since the last update
            for i in range(30):
                self.pixels[i + (self.floor * 30)] = (0, 0, 0)                #lights turn off if motion is not detected for 5 minutes
            self.pixels.show()                            #does not update starttime0, since if motion is detected again lights should turn on

    #the following code tells the pi what to do based off what signals it recieves from each motion sensor

if __name__ == "__main__":

    Floor0 = NeoPixelMotion(0, 23)
    Floor1 = NeoPixelMotion(1, 24)
    Floor2 = NeoPixelMotion(2, 25)

    while True:
        if Floor0.motion_is_detected():
            Floor0.turn_on_lights()
            time.sleep(1)
        if not Floor0.motion_is_detected():
            Floor0.turn_off_lights()
            time.sleep(1)
        if Floor1.motion_is_detected():
            Floor1.turn_on_lights()
            time.sleep(1)
        if not Floor1.motion_is_detected():
            Floor1.turn_off_lights()
            time.sleep(1)
        if Floor2.motion_is_detected():
            Floor2.turn_on_lights()
            time.sleep(1)
        if not Floor2.motion_is_detected():
            Floor2.turn_off_lights()
            time.sleep(1)