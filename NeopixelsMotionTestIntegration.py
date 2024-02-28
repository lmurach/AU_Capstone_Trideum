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
class NeoPixelMotion:
    '''Runs Lighting and motion sensor controls, pulling lockdown_state from an external source'''

    lockdown_state = False
    pixel_pin = board.D18
    strand_length = 30
    color_order = neopixel.GRB
    pixels = neopixel.NeoPixel(pixel_pin, strand_length, pixel_order = color_order, auto_write = False)
    #above code initializes the Neopixels
    time_dif = 5
    #initializing timer variables.
    def __init__ (self, floor, pir_pin):
        self.floor = floor
        self.pir_pin = pir_pin
        #The test strand we used is 30 LEDs long. D18 is GPIO18. For GPIO18 to work, audio must be disabled
        self.pir = MotionSensor(pir_pin)
        self.start_time = 0
        self.sense_time = 0
        #above code initializes the motion sensors on each floor.
        #GPIO 23 recieves data from the basement sensor
        #GPIO 24 recieves data from the first floor sensor
        #GPIO 25 recieves data from 2nd floor sensor.
    
        #the following code controls each floor based on motion sensor readings
        #There is a delay of 5 minutes between changes in lighting.
        #To test this easier, change timeDif to the number of seconds between changes you want.
        #in this example, floor 0 is pixels 0-9, floor 1 is pixels 10-19, and floor 2 is pixels 20-29
    def motion_is_detected(self):
        """Returns motion_detected"""
        return self.pir.motion_detected

    def floor_motion(self):
        """Function activiating lights on the target floor"""
        self.sense_time = time.time()                     #updates the sensetime0 variable to perform a comparison with starttime0
        if (self.sense_time - self.start_time >= self.time_dif):     #only activates if timeDif's value in seconds has passed since the last update
            if self.lockdown_state:
                for i in range(10):
                    self.pixels[i + (self.floor * 10)] = (255, 0, 0)          #lights turn red if motion is detected during a lockdown
            else:
                for i in range(10):
                    self.pixels[i + (self.floor * 10)] = (255, 255, 255)      #lights turn white if motion is detected during open hours
            self.pixels.show()
        self.start_time = time.time()                     #updates the starttime0 variable to reset timer.
    def floor_no_motion(self):
        """Function for determining if lights should turn off in the target floor"""
        self.sense_time = time.time()                     #updates the sensetime0 variable to perform a comparison with starttime0
        if (self.sense_time - self.start_time >= self.time_dif):     #only activates if timeDif's value in seconds has passed since the last update
            for i in range(10):
                self.pixels[i + (self.floor * 10)] = (0, 0, 0)                #lights turn off if motion is not detected for 5 minutes
            self.pixels.show()                            #does not update starttime0, since if motion is detected again lights should turn on

    #the following code tells the pi what to do based off what signals it recieves from each motion sensor
    

Floor0 = NeoPixelMotion(0, 23)
Floor1 = NeoPixelMotion(1, 24)
Floor2 = NeoPixelMotion(2, 25)

while True:
    if Floor0.motion_is_detected():
        Floor0.floor_motion()
        time.sleep(1)
    if not Floor0.motion_is_detected():
        Floor0.floor_no_motion()
        time.sleep(1)
    if Floor1.motion_is_detected():
        Floor1.floor_motion()
        time.sleep(1)
    if not Floor1.motion_is_detected():
        Floor1.floor_no_motion()
        time.sleep(1)
    if Floor2.motion_is_detected():
        Floor2.floor_motion()
        time.sleep(1)
    if not Floor2.motion_is_detected():
        Floor2.floor_no_motion()
        time.sleep(1)

'''
Floor0.pir0.when_motion = Floor0.floor_motion()
Floor0.pir0.when_no_motion = Floor0.floor_no_motion()
Floor1.pir1.when_motion = Floor1.floor_motion()
Floor1.pir1.when_no_motion = Floor1.floor_no_motion()
Floor2.pir2.when_motion = Floor2.floor_motion()
Floor2.pir2.when_no_motion = Floor2.floor_no_motion()

pause()     #prevents the program from closing to allow sensors to check for motion after program runs
'''