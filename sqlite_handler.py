import logging
import sqlite3

class fake2dbSqliteHander():
    def str_generator(self):
        return ''.join(random.choice(string.ascii_uppercase) for i in range(6))

        try:
            database = self.str_generator() + '.db'
            conn=sqlite3.connect()
            logging.info('Database created and opened succesfully: %s' %database)
        except:
            logging.error('Failed to connect or create database / sqlite3')





