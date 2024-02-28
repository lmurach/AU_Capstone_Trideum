import board
import neopixel
#these two imports require the Adafruit_Blinka and Adafruit_Blinka_Neopixel libraries to function
#For more information on these libraries, please check https://learn.adafruit.com/neopixels-on-raspberry-pi/python-usage
from gpiozero import MotionSensor
from signal import pause
#these two imports are used for the motion sensors. The gpiozero library should come preinstalled on the Raspberry Pi OS
#if gpiozero is not on your Pi, run "python3 -m pip install gpiozero" in the command line to install it
import time
pixel_pin = board.D18
strand_length = 30
motion_detected = True
lockdown_state = False
Color_Order = neopixel.GRB
#The test strand we used is 30 LEDs long. D18 is GPIO18. For GPIO18 to work, audio must be disabled
pixels = neopixel.NeoPixel(pixel_pin, strand_length, pixel_order = Color_Order, auto_write = False)
#above code initializes the Neopixels
pir0 = MotionSensor(23)
pir1 = MotionSensor(24)
pir2 = MotionSensor(25)
#above code initializes the motion sensors on each floor. 
#GPIO 23 recieves data from the basement sensor, GPIO 24 recieves data from the first floor sensor, and GPIO 25 recieves data from 2nd floor sensor.
starttime0 = 0
sensetime0 = 0
starttime1 = 0
sensetime1 = 0
starttime2 = 0
sensetime2 = 0
timeDif = 5
#initializing timer variables.
#the following code controls each floor based on motion sensor readings, with a delay of 5 minutes between changes in lighting. 
#To test this easier, change timeDif to the number of seconds between changes you want.
#in this example, floor 0 is pixels 0-9, floor 1 is pixels 10-19, and floor 2 is pixels 20-29
def floor0_motion():
    global sensetime0
    global starttime0
    global timeDif
    sensetime0 = time.time()                     #updates the sensetime0 variable to perform a comparison with starttime0
    if (sensetime0 - starttime0 >= timeDif):     #only activates if timeDif's value in seconds has passed since the last update
        if lockdown_state:
            for i in range(10):
                pixels[i] = (255, 0, 0)          #lights turn red if motion is detected during a lockdown
        else:
            for i in range(10):
                pixels[i] = (255, 255, 255)      #lights turn white if motion is detected during open hours
        pixels.show()
    starttime0 = time.time()                     #updates the starttime0 variable to reset timer.
def floor0_noMotion():
    global sensetime0
    global starttime0
    global timeDif
    sensetime0 = time.time()                     #updates the sensetime0 variable to perform a comparison with starttime0
    if (sensetime0 - starttime0 >= timeDif):     #only activates if timeDif's value in seconds has passed since the last update
        for i in range(10):
            pixels[i] = (0, 0, 0)                #lights turn off if motion is not detected for 5 minutes
        pixels.show()                            #does not update starttime0, since if motion is detected again lights should turn on

def floor1_motion():
    global sensetime1
    global starttime1
    global timeDif
    sensetime1 = time.time()                     #updates the sensetime1 variable to perform a comparison with starttime1
    if (sensetime1 - starttime1 >= timeDif):     #only activates if timeDif's value in seconds has passed since the last update
        if lockdown_state:
            for i in range(10):
                pixels[i + 10] = (255, 0, 0)     #lights turn red if motion is detected during a lockdown
        else:
            for i in range(10):
                pixels[i + 10] = (255, 255, 255) #lights turn white if motion is detected during open hours
        pixels.show()
    starttime1 = time.time()                     #updates the starttime1 variable to reset timer.
def floor1_noMotion():
    global sensetime1
    global starttime1
    global timeDif
    sensetime1 = time.time()                     #updates the sensetime1 variable to perform a comparison with starttime1
    if (sensetime1 - starttime1 >= timeDif):     #only activates if timeDif's value in seconds has passed since the last update
        for i in range(10):
            pixels[i + 10] = (0, 0, 0)           #lights turn off if motion is not detected for 5 minutes
        pixels.show()                            #does not update starttime1, since if motion is detected again lights should turn on

def floor2_motion():
    global sensetime2
    global starttime2
    global timeDif
    sensetime2 = time.time()                     #updates the sensetime2 variable to perform a comparison with starttime2
    if (sensetime2 - starttime2 >= timeDif):     #only activates if timeDif's value in seconds has passed since the last update
        if lockdown_state:
            for i in range(10):
                pixels[i + 20] = (255, 0, 0)     #lights turn red if motion is detected during a lockdown
        else:
            for i in range(10):
                pixels[i + 20] = (255, 255, 255) #lights turn white if motion is detected during open hours
        pixels.show()
    starttime2 = time.time()                     #updates the starttime2 variable to reset timer.
def floor2_noMotion():
    global sensetime2
    global starttime2
    global timeDif
    sensetime2 = time.time()                     #updates the sensetime2 variable to perform a comparison with starttime2
    if (sensetime2 - starttime2 >= timeDif):     #only activates if timeDif's value in seconds has passed since the last update
        for i in range(10):
            pixels[i + 20] = (0, 0, 0)           #lights turn off if motion is not detected for 5 minutes
        pixels.show()                            #does not update starttime2, since if motion is detected again lights should turn on

#the following code tells the pi what to do based off what signals it recieves from each motion sensor
pir0.when_motion = floor0_motion
pir0.when_no_motion = floor0_noMotion
pir1.when_motion = floor1_motion
pir1.when_no_motion = floor1_noMotion
pir2.when_motion = floor2_motion
pir2.when_no_motion = floor2_noMotion

pause()     #prevents the program from closing to allow sensors to check for motion after program runs


#The following is test code for the Neopixels. Uncomment them to test the Neopixels.
'''
if motion_detected and not lockdown_state:
    pixels.fill((255, 255, 255))
    pixels.show()
    #Lights turn on when motion detected during open hours
elif not motion_detected:
    pixels.fill((0, 0, 0))
    pixels.show()
    #Lights turn off when there is no motion
elif motion_detected and lockdown_state:
    pixels.fill((255, 0, 0))
    pixels.show()
    #ensure color order format is set properly or the lights will be green when movement is detected during a lockdown.
while True:
    pixels.fill((255, 255, 255))
    pixels.show()
    time.sleep(3)
    pixels.fill((0, 0, 0))
    pixels.show()
    time.sleep(3)
    pixels.fill((255, 0, 0))
    pixels.show()
    time.sleep(3)
'''
