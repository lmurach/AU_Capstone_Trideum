import time
from rpi_hardware_pwm import HardwarePWM
import RPi.GPIO as GPIO

def open_servo():
    pwm = HardwarePWM(pwm_channel = 1, hz = 50, chip = 0)
    pwm.start(5)

def close_servo():
    pwm = HardwarePWM(pwm_channel = 1, hz = 50, chip = 0)
    pwm.start(10)

GPIO.setmode(GPIO.BOARD)
GPIO.setup((29,31), GPIO.OUT)

while True:
    GPIO.output(29, GPIO.HIGH)
    open_servo()
    time.sleep(1)
    close_servo()
    time.sleep(1)
    GPIO.output(29, GPIO.LOW)
    time.sleep(1)