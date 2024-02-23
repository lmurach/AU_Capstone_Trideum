""" 
Author  : Lauren Murach
Date    : 02/13/2024
Purpose : The RFID class handles all security and utility related to the RFID 
          module. 
"""

from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from mfrc522 import SimpleMFRC522
from typing import Tuple

from database import Database
from door import Door

class RFID:
    '''A class to handle signing and reading cards with calls to the database 
    class. Cards are encrypted with RSA using the PKSC#1 format. The downloaded
    library is pycryptodome, NOT pycrypto. (Pycryptodome is maintained 
    for python 3). All library methods call OpenSSL, a very widely-used 
    cryptography toolkit standard'''

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

    @staticmethod
    def _read_card() -> Tuple[str, str]:
        '''reads from the card to return an id and the message on the card
        in a tuple'''
        reader = SimpleMFRC522()
        id, text = reader.read()
        return (id, text)

    @staticmethod
    def _write_card(text:str):
        writer = SimpleMFRC522()
        id, text_written = writer.write(text)
        print(f"ID: {id}")
        print(f"Text Written: {text_written}")

    @staticmethod
    def sign_card(name:str) -> bool:
        if not Database.does_employee_have_access(name):
            print("invalid user")
            return False
        read_tuple = RFID._read_card()
        # read_tuple = ("45", "dsgdf")
        uid = read_tuple[0]
        Database.add_employee_card_uid(name, uid)
        # sig = RFID._get_signature(name)
        # print(sig)
        RFID._write_card(name)
        return True
        # look for employee validity
        # read the uid off the card
        # add to the database the uid
        # get a signature of the name
        # flash the card with the employee data

    @staticmethod
    def _get_signature(message):
        '''Takes the unencrypted message (likely a name and id combo)
        and encrypts it. The message MUST be encoded to a utf-8 format first.
        Code is taken from the pycryptodome example code.'''

        message = message.encode('utf-8')
        key = RSA.import_key(open("private.pem", encoding="'utf-8'").read())
        h = SHA256.new(message)
        signature = pkcs1_15.new(key).sign(h)
        return signature

    @staticmethod
    def is_authentic_card() -> bool:
        '''Takes the encrypted signature on the card and decrypts it with the 
        public key. It is then checked against the original message.
        Code is taken from the pycryptodome example code.'''

        read_tuple = RFID._read_card()
        print(read_tuple)
        uid = read_tuple[0]
        name = read_tuple[1].strip()
        is_auth = Database.does_employee_have_uid(name, uid)
        print(is_auth)
        return is_auth
        # if name == "":
        #     print("invalid")
        #     return False
        # return True
        # signature = read_tuple[1]
        # name = name.encode('utf-8')
        # key = RSA.import_key(open("receiver.pem", encoding="'utf-8'").read())
        # h = SHA256.new(name)
        # try:
        #     pkcs1_15.new(key).verify(h, signature)
        #     print ("The signature is valid.")
        # except (ValueError, TypeError):
        #     print ("The signature is not valid.")

    # @staticmethod
    # def debug_console():
    #     '''A test method to show the open_lock and close_lock functions
    #     in a demo.'''
    #     while 1:
    #         response = input("Enter your door command: ")
    #         if response == "open":
    #             RFID._open_lock()
    #         elif response == "close":
    #             RFID._close_lock()

if __name__ == "__main__":
    Database.initialize_db()
    name = input("Enter the card owner's name:  ")
    if (RFID.sign_card(name)):
        if(RFID.is_authentic_card()):
            rfid_obj = Door("Someone")
            Door.debug_console(rfid_obj)

