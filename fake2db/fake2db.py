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
from mongodb_handler import Fake2dbMongodbHandler
from helpers import fake2db_logger

logger, extra_information = fake2db_logger()

class InstantiateDBHandlerException(Exception):
    '''An Exception at the instantiation of the handler '''


def _postgresql_process_checkpoint():
    '''this helper method checks if
    postgresql server is available in the sys
    if not fires up one
    '''
    try:
        postgresql_check = subprocess.check_output("pgrep postgres", shell=True)
    except:
        logger.warning('Your postgresql server is offline, fake2db will try to launch it now!', extra=extra_information)
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
        logger.warning('Your mysql server is offline, fake2db will try to launch it now!', extra=extra_information)
        # close_fds = True argument is the flag that is responsible
        # for Popen to launch the process completely independent
        subprocess.Popen("mysqld", close_fds=True, shell=True)
        time.sleep(3)

def _mongodb_process_checkpoint():
    '''this helper method checks if 
    mongodb server is available in the sys
    if not fires up one
    '''
    try:
        mongodb_check = subprocess.check_output("pgrep mongod", shell=True)
    except:
        logger.warning('Your mongodb server is offline, fake2db will try to launch it now!', extra=extra_information)
        # close_fds = True argument is the flag that is responsible
        # for Popen to launch the process completely independent
        subprocess.Popen("mongod", close_fds=True, shell=True)
        time.sleep(3)

try:
    fake_sqlite_handler = Fake2dbSqliteHandler()
    fake_mysql_handler = Fake2dbMySqlHandler()
    fake_postgresql_handler = Fake2dbPostgresqlHandler()
    fake_mongodb_handler = Fake2dbMongodbHandler()
except:
    raise InstantiateDBHandlerException

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--rows", help="Amount of rows desired per table")
    parser.add_argument("--db", help="Db type for creation: sqlite, mysql, postgresql, mongodb, couchdb, to be expanded")
    args = parser.parse_args()

    if not args.rows or not args.db:
        logger.error('Please use with --help argument for usage information!', extra=extra_information)

    if args.rows:
        if args.db:
            logger.info('arguments found(rows and db), starting faking!!', extra=extra_information)
            logger.warning('Rows argument : %s', args.rows, extra=extra_information)
            logger.info('DB argument : %s', args.db, extra=extra_information)
            
            if args.db == 'sqlite':
                fake_sqlite_handler.fake2db_sqlite_initiator(int(args.rows))
            elif args.db == 'mysql':
                _mysqld_process_checkpoint()
                fake_mysql_handler.fake2db_mysql_initiator(int(args.rows))
            elif args.db == 'postgresql':
                _postgresql_process_checkpoint()
                fake_postgresql_handler.fake2db_postgresql_initiator(int(args.rows))
            elif args.db == 'mongodb':
                _mongodb_process_checkpoint()
                fake_mongodb_handler.fake2db_mongodb_initiator(int(args.rows))
            else:
                logger.error('Wrong arg for db parameter. Valid ones : sqlite - mysql - postgresql - mongodb', extra=extra_information)
                    
if __name__ == '__main__':
    main()
