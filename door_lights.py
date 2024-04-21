from datetime import datetime, timedelta
import RPi.GPIO as GPIO

class DoorLights:
    '''This class controls the lights for the 2nd floor RFID door scanner.
    The method is fully static so that a single instance can easily be edited
    by several modules.'''

    green_pin = 17
    red_pin = 27
    wait_time = datetime.now()

    @staticmethod
    def initialize_door_lights()-> None:
        '''The door should call this before anything else to initialize the
        GPIO settings of each pin.'''
        GPIO.setup((DoorLights.green_pin, DoorLights.red_pin), GPIO.OUT)

    @staticmethod
    def turn_on(is_green:bool):
        '''Turns off the correct light depending on the input and turns off the
        other light.'''
        if is_green:
            GPIO.output(DoorLights.red_pin, GPIO.LOW)
            GPIO.output(DoorLights.green_pin, GPIO.HIGH)
        else:
            GPIO.output(DoorLights.green_pin, GPIO.LOW)
            GPIO.output(DoorLights.red_pin, GPIO.HIGH)
        DoorLights._set_light_delay()

    @staticmethod
    def _set_light_delay():
        '''Adds a set amount of time to wait until the next state 
        can be activated. The seconds must be an integer so any
        fraction of a second must bleed into the milliseconds variable'''
        DoorLights.wait_time = datetime.now() + timedelta(seconds=3)

    @staticmethod
    def handle_turning_off_lights():
        '''Polls if the required amount of time has passed then turns off
        both lights'''
        if datetime.now() > DoorLights.wait_time:
            GPIO.output(DoorLights.green_pin, GPIO.LOW)
            GPIO.output(DoorLights.red_pin, GPIO.LOW)
