import logging
import sqlite3


class fake2dbSqliteHander():
    def str_generator(self):
        '''generates uppercase 6 chars
        '''
        return ''.join(random.choice(string.ascii_uppercase) for i in range(6))

    def database_caller_creator(self):
        '''creates a sqlite3 db
        '''
        try:
            database = self.str_generator() + '.db'
            conn=sqlite3.connect(database)
            conn.close()
            logging.info('Database created and opened succesfully: %s' %database)
        except:
            logging.error('Failed to connect or create database / sqlite3')
            
        return database

    def data_filler_simple_registration(self, data):
        '''creates and fills the table

        incoming data structure 
        {'emails' : a_list_of_emails,
        'passwords': a_list_of_passwords
        }

        '''
        database = self.database_caller_creator()
        conn = sqlite3.connect(database)
        cursor = conn.cursor()
        
        cursor.execute('''
        CREATE TABLE simple_registration(id INTEGER PRIMARY KEY, 
        email TEXT unique, password TEXT)
        ''')
        conn.commit()

        for email, password in data.iteritems()
            try:
                cursor.execute('''INSERT INTO simple_registration(email, password)
                VALUES(:email, :password)''',
                               {'email':email, 'password':password})
                conn.commit()
            except Exception as e:
                logging.error(e)

        conn.close()



