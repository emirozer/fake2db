
import logging
import getpass
import string
import random
import uuid


def fake2db_logger():
    '''creates a logger obj'''
    # Pull the local ip and username for meaningful logging
    username = getpass.getuser()
    
    # Set the logger
    FORMAT = '%(asctime)-15s %(user)-8s %(message)s'
    logging.basicConfig(format=FORMAT)
    extra_information = {'user': username}
    logger = logging.getLogger('fake2db_logger')
    # --------------------
    return logger, extra_information


def str_generator(self):
    '''generates uppercase 8 chars
    '''
    return ''.join(random.choice(string.ascii_uppercase) for i in range(8))

def lower_str_generator(self):
    '''generates lowercase 8 chars
    '''
    return ''.join(random.choice(string.ascii_lowercase) for i in range(8))


def rnd_id_generator(self):
    '''generates a UUID such as :
    UUID('dd1098bd-70ac-40ea-80ef-d963f09f95a7')
    than gets rid of dashes
    '''
    return str(uuid.uuid4()).replace('-', '')
