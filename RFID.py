""" 
Author  : Lauren Murach
Date    : 02/13/2024
Purpose : The RFID class handles all security and utility related to the RFID 
          module. 
"""

from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from rpi_hardware_pwm import HardwarePWM

class RFID:
    '''A class to handle signing and reading cards with calls to the database 
    class. Cards are encrypted with RSA using the PKSC#1 format. The downloaded
    library is pycryptodome, NOT pycrypto. (Pycryptodome is maintained 
    for python 3). All library methods call OpenSSL, a very widely-used 
    cryptography toolkit standard'''

    @staticmethod
    def _open_lock():
        '''The servomotor accepts a 50hz signal with a 1-2 ms pulse,
        so this function generates a duty cycle of 5% (1ms) for
        a degree of 0 turn (open)'''
        pwm = HardwarePWM(pwm_channel = 0, hz = 50, chip = 0)
        pwm.start(5)

    @staticmethod
    def _close_lock():
        '''The servomotor accepts a 50hz signal with a 1-2 ms pulse,
        so this function generates a duty cycle of 10% (2ms) for
        a degree of 90 turn (closed)'''
        pwm = HardwarePWM(pwm_channel = 0, hz = 50, chip = 0)
        pwm.start(10)

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
    def sign_card(message):
        '''Takes the unencrypted message (likely a name and id combo)
        and encrypts it. The message MUST be encoded to a utf-8 format first.
        Code is taken from the pycryptodome example code.'''

        message = message.encode('utf-8')
        key = RSA.import_key(open("private.pem", encoding="'utf-8'").read())
        h = SHA256.new(message)
        signature = pkcs1_15.new(key).sign(h)
        return signature

    @staticmethod
    def authenticate_card(message, signature):
        '''Takes the encrypted signature on the card and decrypts it with the 
        public key. It is then checked against the original message.
        Code is taken from the pycryptodome example code.'''

        message = message.encode('utf-8')
        key = RSA.import_key(open("receiver.pem", encoding="'utf-8'").read())
        h = SHA256.new(message)
        try:
            pkcs1_15.new(key).verify(h, signature)
            print ("The signature is valid.")
        except (ValueError, TypeError):
            print ("The signature is not valid.")

    @staticmethod
    def debug_console():
        '''A test method to show the open_lock and close_lock functions
        in a demo.'''
        while 1:
            response = input("Enter your door command: ")
            if response == "open":
                RFID._open_lock()
            elif response == "close":
                RFID._close_lock()
