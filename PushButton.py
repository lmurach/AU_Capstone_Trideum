""" 
Author  : Wesley Cooke
Date    : 02/11/2024
Purpose : The PushButton class represents a normally open push button.
          It has the functionality of reading the state of a push button 
          that is connected to GPIO pin "pinNum". Make sure the appropriate 
          pullup resistor is connected and corresponding ground and signal wire 
          is attached.  
"""

import RPi.GPIO as GPIO

class PushButton():
    """
    PushButton represents a normally open push button. 
    It can read it's own state and return 0 for low and 1 for high. 
    
    You can configure a PushButton as Active High or Active Low:
    Active High means the signal sits low, and will turn to high when the button is being pushed.
    Active Low means the signal sits high, and will turn to low when the button is being pushed. 
    The only difference is the circuit diagram. Make sure you know which one you are using. 

    Methods:
    GetState() : bool - Returns the current state of the push button 
    """

    def __init__(self, aPin:int):
        """
        Constructor for the PushButton class.

        params:
            aPin : int - The GPIO pin that the push button signal wire is connected to. 
        """
        self.pinNum = aPin
        
        # Set the pin as an Input pin. We plan to read the state. 
        GPIO.setup(self.pinNum, GPIO.IN)
    
    def GetState(self):
        """
        Get's the state of the signal wire for this push button. 
        Returns 0 for Low or 1 for High. 

        return : bool 
        """
        return GPIO.input(self.pinNum)

class ReedSwitch(PushButton): 
    """
    This class represents a normally open reed switch.
    When a magnet passes near the switch, it makes a connection.

    Reed Switches can be configured as Active High Or Active Low. 
    Active High means the signal normally sits low, and will turn to high when the button is being pushed.
    Active Low means the signal normally sits high, and will turn to low when the button is being pushed. 
    The only difference is the circuit diagram. Make sure you know which one you are using. 

    Methods:
        GetState() : bool - Returns the current state of the reed switch 
    """

    def __init__(self, aPin):
        """
        Constructor for the ReedSwitch class.

        params:
            aPin : int - The GPIO pin that the push button signal wire is connected to. 
        """

        # Super says to inherit all methods and properties of the parent class.
        super().__init__(aPin)