import logging
import sqlite3

class fake2dbSqliteHander():
    def str_generator(self):
        '''generates uppercase 6 chars
        '''
        return ''.join(random.choice(string.ascii_uppercase) for i in range(6))

    def database_creator(self):
        '''creates a sqlite3 db
        '''
        try:
            database = self.str_generator() + '.db'
            conn=sqlite3.connect()
            logging.info('Database created and opened succesfully: %s' %database)
        except:
            logging.error('Failed to connect or create database / sqlite3')





