import sqlite3
import random
import string

from db_patterns import db_patterns
from logging import getLogger

logger = getLogger(__name__)

class DbConnException(Exception):
    """Database Connection or Creation Exception"""

class fake2dbSqliteHandler():

    def str_generator(self):
        '''generates uppercase 6 chars
        '''
        return ''.join(random.choice(string.ascii_uppercase) for i in range(6))

    def database_caller_creator(self):
        '''creates a sqlite3 db
        '''
        database = ''
        
        try:
            database = self.str_generator() + '.db'
            conn=sqlite3.connect(database)
            conn.close()
            logger.warning('Database created and opened succesfully: %s' %database)
        except:
            logger.error('Failed to connect or create database / sqlite3')
            raise DbConnException
            
        return database

    def data_filler_simple_registration(self, number_of_rows):
        '''creates and fills the table
        '''

        # incoming data structure 
        # {'emails' : a_list_of_emails,
        # 'passwords': a_list_of_passwords
        # }
        db_patterns_instance = db_patterns()
        data = db_patterns_instance.simple_registration(number_of_rows)

        database = self.database_caller_creator()
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        
        cursor.execute('''
        CREATE TABLE simple_registration(id INTEGER PRIMARY KEY, 
        email TEXT unique, password TEXT)
        ''')
        conn.commit()

        for email, password in data.iteritems():
            try:
                cursor.execute('''INSERT INTO simple_registration(email, password)
                VALUES(:email, :password)''',
                               {'email':email, 'password':password})
                conn.commit()
                logger.warning('Commit successful after write job!')
            except Exception as e:
                logger.error(e)

        conn.close()



