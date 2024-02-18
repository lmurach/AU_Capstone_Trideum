"""
Author  : Wesley Cooke
Date    : 01/31/2024
Purpose : This file shows how to drive a stepper motor using a 
          micro stepper. 
		  The switch states on the stepper motor are set to:
		  0b110110, where the MSB is switch 1 and LSB is siwtch 6. 
		  This sets the stepper to 200 pulses(steps)/rev
		  and 1.5 A max current draw. 
		  Three active high push buttons simulate the elevator and tell
		  the motor to go to a certain step that represent a floor.
"""

# Import the necessary Libararies
import time
import RPi.GPIO as GPIO

# Set the pins to use the BCM style of pinout.
GPIO.setmode(GPIO.BCM)

# Yellow wire connected to 6, to pulse pin on motor controller
# White  wire connected to 5, to direction pin on motor controller
PULSE = 6
DIR   = 5

# Active High Push Buttons. Signal coming from the resistor.
BUTTON_1 = 21
BUTTON_2 = 20
BUTTON_3 = 16

# Set the the pulse and direction pins to outputs
GPIO.setup(PULSE, GPIO.OUT)
GPIO.setup(DIR, GPIO.OUT)

# Set the push button signals as inputs.
GPIO.setup(BUTTON_1, GPIO.IN)
GPIO.setup(BUTTON_2, GPIO.IN)
GPIO.setup(BUTTON_3, GPIO.IN)

# What step is each floor on? 200 steps/revolution. (Configurable via microstepper).
FLOOR_3 = 200
FLOOR_2 = 100
FLOOR_1 = 0
current_floor = 0

def step(num_steps:int, direction:bool):
	""" 
	This method will step the motor num_steps times.
	
	params:
		num_steps:int  The number of steps to step
		direction:bool The direction the motor should go
    """

	# Set the direction
	GPIO.output(DIR, direction)
	# Step num_steps
	for _ in range(num_steps):
		GPIO.output(PULSE, True)
		time.sleep(0.0005)
		GPIO.output(PULSE, False)
		time.sleep(0.0005)


if __name__ == "__main__":
	try:
		while True:
			# Read the state of the buttons
			button_state_1 = GPIO.input(BUTTON_1)
			button_state_2 = GPIO.input(BUTTON_2)
			button_state_3 = GPIO.input(BUTTON_3)

			# If the first button was pressed
			if (button_state_1):

				# If the current step is above the first floor
				if(current_floor > FLOOR_1):
					# Step backwards
					step(current_floor - FLOOR_1, True)
				current_floor = 0

			# If the second button was pressed
			if (button_state_2):

				# If the current step is above the second floor
				if(current_floor > FLOOR_2):
					step(current_floor-FLOOR_2, True)

				# If the current step is below the second floor
				elif( current_floor < FLOOR_2):
					step(FLOOR_2 - current_floor, False)	
				current_floor = 100

			# If the third button was pressed
			if (button_state_3):

				# If the current step is below the thrid floor
				if(current_floor < FLOOR_3):
					step(FLOOR_3 - current_floor, False)
				current_floor = 200

	except KeyboardInterrupt as e:
		GPIO.cleanup()
