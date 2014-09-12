import sys

from datetime import date
from logging import getLogger

from sqlite_handler import fake2dbSqliteHandler

logger = getLogger(__name__)
CLI_TAG = 'fake2db >>'

class InstanciateDBHandlerException(Exception):
    '''An Exception at the instantiation of the handler '''

class fake2db:
    
    def exit(self):
        sys.exit(0)

    def help(self):
        print('WORK IN PROGRESS')

while True:
    user_input = raw_input(CLI_TAG)

    try:
        fake_sqlite_handler = fake2dbSqliteHandler()
    except:
        raise InstanciateDBHandlerException

    if user_input == 'exit' or user_input == 'quit':
        fake2db().exit()

    elif user_input.startswith('sqlite'):
        # sqlite -simple_registration -3
        splitted = user_input.split('-')
        # ['sqlite ', 'simple_registration ', '3']
        db_pattern = splitted[1].strip()
        number_of_rows = splitted[2]
        if db_pattern == 'simple_registration':
            fake_sqlite_handler.data_filler_simple_registration(number_of_rows)

    elif user_input.startswith('postgresql'):
        pass
    elif user_input.startswith('mongodb'):
        pass
    elif user_input.startswith('couchdb'):
        pass
    elif user_input.startswith('mysql'):
        pass
    elif user_input == '':
        pass
    else:
        print("You have entered a wrong command or argument , please type help")
