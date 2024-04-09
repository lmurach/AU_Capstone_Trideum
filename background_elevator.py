""" 
Author  : Wesley Cooke
Date    : 04/09/2024
Purpose :
"""

from PyQt5.QtCore import pyqtSignal, QObject
import serial 

class BGElevator(QObject):

    button_signal = pyqtSignal(int, int, int)
    
    def __init__(self):
        super().__init__()
        self.ser = serial.Serial('/dev/tty/ACM0', 9600, timeout=1)
        self.ser.reset_input_buffer()

    def run(self):
        '''Main thread'''

        while True:
            self._button_handler()

    def _button_handler(self):

        if (self.ser.in_waiting>0):
            start = self.ser.readline().decode('utf-8').rstrip()
        
            if (start == "S"):
                bs1 = self.ser.readline().decode('utf-8').rstrip()
                bs2 = self.ser.readline().decode('utf-8').rstrip()
                bs3 = self.ser.readline().decode('utf-8').rstrip()

                end = self.ser.readline().decode('utf-8').rstrip()

                if (end == "E"):
                    self.button_signal.emit(bs1, bs2, bs3)
