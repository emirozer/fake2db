import sys
import argparse
import socket
import getpass
import logging

from datetime import date
from sqlite_handler import fake2dbSqliteHandler


# Pull the local ip and username for meaningful logging
username = getpass.getuser()
local_ip = socket.gethostbyname(socket.gethostname())
# Set the logger
FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'
logging.basicConfig(format=FORMAT)
d = {'clientip': local_ip, 'user': username}
logger = logging.getLogger('fake2db_logger')
# --------------------

class InstanciateDBHandlerException(Exception):
    '''An Exception at the instantiation of the handler '''

class Fake2Db:
    
    def exit(self):
        sys.exit(0)

    def help(self):
        print('WORK IN PROGRESS')


try:
    fake_sqlite_handler = fake2dbSqliteHandler()
except:
    raise InstanciateDBHandlerException

parser = argparse.ArgumentParser()
parser.add_argument("--rows", help="Amount of rows desired per table")
parser.add_argument("--db", help="Db type for creation: sqlite, mysql, postgresql, mongodb, couchdb, to be expanded")
args = parser.parse_args()

if not args.rows and not args.db:
    logger.error('Please use with --help argument for usage information!', extra=d)

if args.rows:
    if args.db:
        logger.info('arguments found(rows and db), starting faking!!', extra=d)
        logger.warning('Rows argument : %s', args.rows, extra=d)
        logger.info('DB argument : %s', args.db, extra=d)
        fake_sqlite_handler.data_filler_simple_registration(int(args.rows))
        
