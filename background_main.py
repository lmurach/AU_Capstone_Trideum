import time
from PyQt5.QtCore import QRunnable, pyqtSlot

from RFID import RFIDSecurity

class BackgroundMain(QRunnable):
    '''This serves as the "main" function for everything that is not the GUI.
    Another file keeps all the threading functions related to the background 
    processes for seperation of concerns.
    
    Concurrency model: 2 threads, GUI and background. *Maybe* 3 with the arduino
    elevator. There is a maximum of 4 threads so keeping everything on different
    threads could lead to long delays and a high possibility of a non-responsive
    GUI (if 4 threads activate so the GUI is put on the queue)'''

    @pyqtSlot()
    def run(self):
        '''Main thread'''
        rfid = RFIDSecurity()
        # define a class instance for each motion sensor
        # and maybe the lights? idk
        while True:
            print("testing")
            if rfid.is_card_there():
                print("card detect")
                rfid.handle_read_card()
                for _ in range (0, 20):
                    rfid.is_card_there()
            time.sleep(0.25)
        # for floor in range(0, 3):
        #     if (check_motion(floor)):
        #         handle_motion(floor)
