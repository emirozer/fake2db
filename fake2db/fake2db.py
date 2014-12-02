import sys
import argparse
import socket
import getpass
import logging
import subprocess
import time

from sqlite_handler import Fake2dbSqliteHandler
from mysql_handler import Fake2dbMySqlHandler
from postgresql_handler import Fake2dbPostgresqlHandler

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


def _postgresql_process_checkpoint():
    '''this helper method checks if
    postgresql server is available in the sys
    if not fires up one
    '''
    try:
        postgresql_check = subprocess.check_output("pgrep postgres", shell=True)
    except:
        logger.warning('Your postgresql server is offline, fake2db will try to launch it now!', extra=d)
        # close_fds = True argument is the flag that is responsible
        # for Popen to launch the process completely independent
        subprocess.Popen("postgres -D /usr/local/pgsql/data", close_fds=True, shell=True)
        time.sleep(3)


def _mysqld_process_checkpoint():
    '''this helper method checks if 
    mysql server is available in the sys
    if not fires up one
    '''
    try:
        mysqld_check = subprocess.check_output("pgrep mysqld", shell=True)
    except:
        logger.warning('Your mysql server is offline, fake2db will try to launch it now!', extra=d)
        # close_fds = True argument is the flag that is responsible
        # for Popen to launch the process completely independent
        subprocess.Popen("mysqld", close_fds=True, shell=True)
        time.sleep(3)


try:
    fake_sqlite_handler = Fake2dbSqliteHandler()
    fake_mysql_handler = Fake2dbMySqlHandler()
    fake_postgresql_handler = Fake2dbPostgresqlHandler()
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
            _mysqld_process_checkpoint()
            fake_mysql_handler.fake2db_mysql_initiator(int(args.rows))
        elif args.db == 'postgresql':
            _postgresql_process_checkpoint()
            fake_postgresql_handler.fake2db_postgresql_initiator(int(args.rows))
        else:
            logger.error('Please use with --help argument for usage information!', extra=d)
