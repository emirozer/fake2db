import sys
import argparse
import socket
import getpass
import logging

from datetime import date
from sqlite_handler import fake2dbSqliteHandler
from mysql_handler import fake2dbMySqlHandler

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

    
try:
    fake_sqlite_handler = fake2dbSqliteHandler()
    fake_mysql_handler = fake2dbMySqlHandler()
except:
    raise InstanciateDBHandlerException

parser = argparse.ArgumentParser()
parser.add_argument("--rows", help="Amount of rows desired per table")
parser.add_argument("--db", help="Db type for creation: sqlite, mysql, postgresql, mongodb, couchdb, to be expanded")
args = parser.parse_args()

if not args.rows or not args.db:
    logger.error('Please use with --help argument for usage information!', extra=d)

if args.rows:
    if args.db:
        logger.info('arguments found(rows and db), starting faking!!', extra=d)
        logger.warning('Rows argument : %s', args.rows, extra=d)
        logger.info('DB argument : %s', args.db, extra=d)

        if args.db == 'sqlite':
            fake_sqlite_handler.fake2db_sqlite_initiator(int(args.rows))
        elif args.db == 'mysql':
            fake_sqlite_handler.fake2db_mysql_initiator(int(args.rows))
        else:
            logger.error('Please use with --help argument for usage information!', extra=d)
