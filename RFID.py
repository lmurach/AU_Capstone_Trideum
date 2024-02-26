""" 
Author  : Lauren Murach
Date    : 02/13/2024
Purpose : The RFID class handles all security and utility related to the RFID 
          module. 
"""
from typing import Tuple
import time
import RPi.GPIO as GPIO

from datetime import datetime, timedelta
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from PIRC522.pirc522.rfid import RFID

from database import Database
from door import Door

class RFIDSecurity(RFID):
    '''A class to handle signing and reading cards with calls to the database 
    class. Cards are encrypted with RSA using the PKSC#1 format. The downloaded
    library is pycryptodome, NOT pycrypto. (Pycryptodome is maintained 
    for python 3). All library methods call OpenSSL, a very widely-used 
    cryptography toolkit standard'''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.time_until_run:datetime = datetime.now()
        self.irq.clear()
        self.irq_flag = False
        self.util_obj = self.util()

    @staticmethod
    def generate_keys():
        '''Public and private keys are generated in seperate files.
        These are to NEVER be posted on github and only ever accessed
        by these read file functions. The .pem file extension is necessary
        for Cryptographic signatures encoding convention rules
        https://serverfault.com/questions/9708/what-is-a-pem-file-and-how-does-it-differ-from-other-openssl-generated-key-file'''

        key = RSA.generate(2048)
        private_key = key.export_key()
        with open("private.pem", "wb") as f:
            f.write(private_key)

        public_key = key.publickey().export_key()
        with open("receiver.pem", "wb") as f:
            f.write(public_key)

    def is_card_there(self):
        self.init()
        self.irq.clear()
        self.dev_write(0x04, 0x00)
        self.dev_write(0x02, 0xA0)
        self.dev_write(0x09, 0x26)
        self.dev_write(0x01, 0x0C)
        self.dev_write(0x0D, 0x87)
        if self.irq_flag:
            self.irq_flag = False
            self.irq.clear()
            return True
        return False

    def handle_read_card(self):
        if self.time_until_run < datetime.now():
            (name, uid) = self.read_card()
            if not name is None:
                name = name.strip()
                if Database.does_employee_have_access(name):
                    print("Employee has access")
                else:
                    print("Employee does not have access")

    def _add_wait_time(self, seconds:int, milliseconds:int):
        '''Adds a set amount of time to wait until the next state 
        can be activated. The seconds must be an integer so any
        fraction of a second must bleed into the milliseconds variable'''

        self.time_until_run = datetime.now() + \
            timedelta(seconds=seconds, milliseconds=milliseconds)


    def read_card(self):
        self.init()
        (error, data) = self.request()
        print(error)
        print(data)
        if not error:
            print("\nDetected: " + format(data, "02x"))
            (error, uid) = self.anticoll()
            s_uid = f"{uid[0]}{uid[1]}{uid[2]}{uid[3]}"
            print(f"Card read UID: {s_uid}")

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
            return (name, uid)
        return (None, None)

    # @staticmethod
    # def _read_card() -> Tuple[str, str]:
    #     '''reads from the card to return an id and the message on the card
    #     in a tuple'''
    #     reader = SimpleMFRC522()
    #     id, text = reader.read()
    #     return (id, text)

    # @staticmethod
    # def _write_card(text:str):
    #     writer = SimpleMFRC522()
    #     id, text_written = writer.write(text)
    #     print(f"ID: {id}")
    #     print(f"Text Written: {text_written}")

    # @staticmethod
    # def sign_card(emp_name:str) -> bool:
    #     '''The function should be ran when the card is against the RFID reader.
    #     It first checks for if an employee exists under a given name and has 
    #     door permissions. (Returns false if they do not). Then the RFID is read
    #     for the uid on the card. This uid is written to the employees database
    #     so that it can be validated later. Finally, the card is written.
    #     TODO: look into if the data needs to be encrypted'''

    #     if not Database.does_employee_have_access(emp_name):
    #         print("invalid user")
    #         return False
    #     read_tuple = RFIDSecurity._read_card()
    #     uid = read_tuple[0]
    #     Database.add_employee_card_uid(emp_name, uid)
    #     RFIDSecurity._write_card(emp_name)
    #     return True

    # @staticmethod
    # def _get_signature(message):
    #     '''Takes the unencrypted message (likely a name and id combo)
    #     and encrypts it. The message MUST be encoded to a utf-8 format first.
    #     Code is taken from the pycryptodome example code.'''

    #     message = message.encode('utf-8')
    #     key = RSA.import_key(open("private.pem", encoding="'utf-8'").read())
    #     h = SHA256.new(message)
    #     signature = pkcs1_15.new(key).sign(h)
    #     return signature

    # @staticmethod
    # def is_authentic_card() -> bool:
    #     '''Takes the encrypted signature on the card and decrypts it with the 
    #     public key. It is then checked against the original message.
    #     Code is taken from the pycryptodome example code.'''

    #     try:
    #         read_tuple = RFIDSecurity._read_card()
    #         print("read")
    #     finally:
    #         RPi.GPIO.cleanup()
    #     print(read_tuple)
    #     uid = read_tuple[0]
    #     name = read_tuple[1].strip()
    #     is_auth = Database.does_employee_have_uid(name, uid)
    #     print(is_auth)
    #     return is_auth
    #     # if name == "":
    #     #     print("invalid")
    #     #     return False
    #     # return True
    #     # signature = read_tuple[1]
    #     # name = name.encode('utf-8')
    #     # key = RSA.import_key(open("receiver.pem", encoding="'utf-8'").read())
    #     # h = SHA256.new(name)
    #     # try:
    #     #     pkcs1_15.new(key).verify(h, signature)
    #     #     print ("The signature is valid.")
    #     # except (ValueError, TypeError):
    #     #     print ("The signature is not valid.")

if __name__ == "__main__":
    # Database.initialize_db()
    # name = input("Enter the card owner's name:  ")
    # if (RFIDSecurity.sign_card(name)):
    #     if(RFIDSecurity.is_authentic_card()):
    #         rfid_obj = Door("Someone")
    #         Door.debug_console(rfid_obj)

    rfid = RFIDSecurity()
    while True:
        if (rfid.is_card_there()):
            rfid.handle_read_card()
            for x in range (0, 20):
                rfid.is_card_there()
        time.sleep(0.25)

    # rdr = RFIDSecurity()
    # util = rdr.util()
    # util.debug = True

    # print("Starting")
    # while not rdr.is_card_there():
    #     time.sleep(0.5)
    # print("Card!")
    # time.sleep(2)
    # (error, data) = rdr.request()
    # print(error)
    # print(data)
    # if not error:
    #     print("\nDetected: " + format(data, "02x"))

    # (error, uid) = rdr.anticoll()
    # if not error:
    #     print("Card read UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3]))

    #     print("Setting tag")
    #     util.set_tag(uid)
    #     print("\nAuthorizing")
    #     #util.auth(rdr.auth_a, [0x12, 0x34, 0x56, 0x78, 0x96, 0x92])
    #     util.auth(rdr.auth_b, [0x74, 0x00, 0x52, 0x35, 0x00, 0xFF])
    #     print("\nReading")
    #     util.read_out(4)
    #     print("\nDeauthorizing")
    #     util.deauth()
