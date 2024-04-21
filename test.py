import time
from rpi_hardware_pwm import HardwarePWM
import RPi.GPIO as GPIO

from RFID import RFIDSecurity

def open_servo():
    pwm = HardwarePWM(pwm_channel = 0, hz = 50, chip = 0)
    pwm.start(5)

def close_servo():
    pwm = HardwarePWM(pwm_channel = 0, hz = 50, chip = 0)
    pwm.start(10)

if __name__ == "__main__":
    rfid = RFIDSecurity()
    while True:
        if rfid.read_id() is None:
            print("no card")
        else:
            print("card")
        time.sleep(0.3)
