""" 
Author  : Lauren Murach
Date    : 02/13/2024
Purpose : The RFID class handles all security and utility related to the RFID 
          module. 
"""
from typing import Tuple
import time
import RPi.GPIO as GPIO
from door_lights import DoorLights

from datetime import datetime, timedelta
# from Crypto.PublicKey import RSA
# from Crypto.Signature import pkcs1_15
# from Crypto.Hash import SHA256
from PIRC522.pirc522.rfid import RFID

from database import Database

class RFIDSecurity(RFID):
    '''A class to handle signing and reading cards with calls to the database 
    class. Cards are encrypted with RSA using the PKSC#1 format. The downloaded
    library is pycryptodome, NOT pycrypto. (Pycryptodome is maintained 
    for python 3). All library methods call OpenSSL, a very widely-used 
    cryptography toolkit standard'''

    def __init__(self, *args, **kwargs):
        super().__init__(pin_mode=GPIO.BCM, pin_rst=25, pin_irq=6)
        # original RFID library is in BOARD, but it MUST be in BCM to play nice
        # with the Adafruit neopixel library
        self.time_until_run:datetime = datetime.now()
        self.irq.clear()
        self.irq_flag = False
        self.util_obj = self.util()
        self.db = Database()

    def is_card_there(self) -> bool:
        '''Writes a command to the board and if an interrupt is sent back, then
        the card is known to be there.'''
        eid = self.read_id()
        if eid is None:
            return False
        return True
        # self.init()
        # self.irq.clear()
        # self.dev_write(0x04, 0x00)
        # self.dev_write(0x02, 0xA0)
        # self.dev_write(0x09, 0x26)
        # self.dev_write(0x01, 0x0C)
        # self.dev_write(0x0D, 0x87)
        # if self.irq_flag:
        #     self.irq_flag = False
        #     self.irq.clear()
        #     return True
        # return False

    def handle_read_card(self) -> Tuple[bool, int]:
        '''Reads the card and returns a tuple. The first value being a 
        boolean designating if the employee has access or not. The second value
        is the employee database id (if it valid).'''
        if self.time_until_run < datetime.now():
            (name, uid) = self.read_card()
            if not name is None:
                name = name.strip()
                e_id = self.db.does_employee_have_access(name)
                if e_id != -1:
                    if self.db.does_employee_have_uid(e_id, uid):
                        return (True, e_id)
                    DoorLights.turn_on(False)
                    return (False, 0)
        DoorLights.turn_on(False)
        return (False, 0)

    def _add_wait_time(self, seconds:int, milliseconds:int):
        '''Adds a set amount of time to wait until the next state 
        can be activated. The seconds must be an integer so any
        fraction of a second must bleed into the milliseconds variable'''

        self.time_until_run = datetime.now() + \
            timedelta(seconds=seconds, milliseconds=milliseconds)


    def read_card(self) -> Tuple[str, str]:
        '''Reads the error, data, and uid from the card and returns a tuple
        with the name and uid,'''
        self.init()
        (error, data) = self.request()
        if not error:
            (error, uid) = self.anticoll()
            str_uid = ""
            for num in uid:
                str_uid += str(num)
            # Setting tag
            self.util_obj.set_tag(uid)
            # Authorizing")
            #util.auth(rdr.auth_a, [0x12, 0x34, 0x56, 0x78, 0x96, 0x92])
            # self.util_obj.auth(self.auth_b, [0x74, 0x00, 0x52, 0x35, 0x00, 0xFF])
            self.util_obj.auth(self.auth_a, [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF])
            # Reading
            name = self.util_obj.read_out_ASCI(8)
            # Deauthorizing
            self.util_obj.deauth()
            if not name is None:
                self._add_wait_time(10,0)
            return (name, str_uid)
        return (None, None)

if __name__ == "__main__":
    rfid = RFIDSecurity()
    while True:
        if (rfid.is_card_there()):
            rfid.handle_read_card()
            for x in range (0, 20):
                rfid.is_card_there()
        time.sleep(0.25)
