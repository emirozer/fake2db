import random
import string
import logging
import getpass
import socket
import sys
import time
import subprocess
from db_patterns import DbPatterns


# Pull the local ip and username for meaningful logging
username = getpass.getuser()
local_ip = socket.gethostbyname(socket.gethostname())
# Set the logger
FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'
logging.basicConfig(format=FORMAT)
d = {'clientip': local_ip, 'user': username}
logger = logging.getLogger('fake2db_logger')
# --------------------

try:
    import pymongo
except ImportError:
    logger.error('pymongo package not found onto python packages, please run : \
    pip install -r requirements.txt  \
    on the root of the project')
    sys.exit(0)
