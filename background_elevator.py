""" 
Author  : Wesley Cooke
Date    : 04/09/2024
Purpose : This thread will talk to the elevator and alert the GUI
          of the state of the elevator. 
"""

from PyQt5.QtCore import pyqtSignal, QObject
import serial

class BGElevator(QObject):
    """
    This class represents a connection to our Elevator system that is running on the Arudino.
    
    The arduino must be connected to the raspberry pi over one of the USB connections.
    """

    # button signal object to signal GUI 
    button_signal = pyqtSignal(list)

    def __init__(self):
        super().__init__()
        # Connect to this serial port and clear out any junk that may already be there
        self.ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
        self.ser.reset_input_buffer()

    def run(self):
        """ Main loop of the thread """

        while True:
            self._update_requested()

    def _update_requested(self):
        """ This handler will read the state of the requested queue from the Arduino and signal the GUI. """
        
        # If there are messages to read.
        if (self.ser.in_waiting>0):

            # Read the starting bit.
            start = self.ser.readline().decode('utf-8').rstrip()

            # check to ensure the start is the start.
            if (start == "S"):

                # Read the next three lines that represent the state of our requested queue.
                bs1 = self.ser.readline().decode('utf-8').rstrip()
                bs2 = self.ser.readline().decode('utf-8').rstrip()
                bs3 = self.ser.readline().decode('utf-8').rstrip()
                current_floor = self.ser.readline().decode('utf-8').rstrip()

                # read the last byte and make sure it is the ending byte. 
                end = self.ser.readline().decode('utf-8').rstrip()

                if (end == "E"):
                    # Emit the queue to the GUI
                    self.button_signal.emit([int(bs1), int(bs2), int(bs3), int(current_floor)])
