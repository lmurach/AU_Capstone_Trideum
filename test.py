import time
from rpi_hardware_pwm import HardwarePWM
import RPi.GPIO as GPIO

from neo_pixel_motion import NeoPixelMotion as NPM

def open_servo():
    pwm = HardwarePWM(pwm_channel = 0, hz = 50, chip = 0)
    pwm.start(5)

def close_servo():
    pwm = HardwarePWM(pwm_channel = 0, hz = 50, chip = 0)
    pwm.start(10)

if __name__ == "__main__":
    npm = NPM(0, 16)
    while True:
        npm.turn_on_lights_raw()
        time.sleep(0.4)
