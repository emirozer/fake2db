import sys

from sqlite_handler import fake2dbSqliteHandler
from logging import getLogger
from datetime import date

logger = getLogger(__name__)
CLI_TAG = 'fake2db >>'

class fake2db:
    
    def exit(self):
        sys.exit(0)

    def help(self):
        print('WORK IN PROGRESS')

while True:
    user_input = raw_input(CLI_TAG)
    fake_sqlite_handler = fake2dbSqliteHandler()
    if user_input == 'exit' or user_input == 'quit':
        fake2db().exit()
    elif user_input == 'sqlite':
        fake_sqlite_handler.data_filler_simple_registration(3)
    else:
        print("You have entered a wrong command or argument , please type help")
