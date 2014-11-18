import sys
import argparse

from datetime import date
from logging import getLogger

from sqlite_handler import fake2dbSqliteHandler

logger = getLogger(__name__)


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
    logger.error('Please use with --help argument for usage information!')

if args.rows:
    if args.db:
        logger.info('arguments found(rows and db), starting faking!!')
        logger.warning('Rows argument : %s', args.rows)
        logger.info('DB argument : %s', args.db)
        fake_sqlite_handler.data_filler_simple_registration(int(args.rows))
        
