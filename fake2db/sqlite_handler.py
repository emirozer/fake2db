import sqlite3
import sys
from base_handler import BaseHandler
from custom import faker_options_container
from helpers import fake2db_logger, str_generator, rnd_id_generator

logger, extra_information = fake2db_logger()
d = extra_information


class DbConnException(Exception):
    """Database Connection or Creation Exception"""


class Fake2dbSqliteHandler(BaseHandler):

    def fake2db_sqlite_initiator(self, number_of_rows, name=None, custom=None):
        '''Main handler for the operation
        '''
        rows = number_of_rows
        conn = self.database_caller_creator(name)

        if custom:
            self.custom_db_creator(rows, conn, custom)
            conn.close()
            sys.exit(0)
            
        self.data_filler_simple_registration(rows, conn)
        self.data_filler_detailed_registration(rows, conn)
        self.data_filler_company(rows, conn)
        self.data_filler_user_agent(rows, conn)
        self.data_filler_customer(rows, conn)
        conn.close()

    def custom_db_creator(self, number_of_rows, conn, custom):
        '''creates and fills the table with simple regis. information
        '''
        cursor = conn.cursor()
        custom_d = faker_options_container()
        sqlst = '''
        CREATE TABLE custom(id TEXT PRIMARY KEY,'''

        # first one is always ID primary key
        exec_many = 'insert into custom values(?,'
        
        for c in custom:
            if custom_d.get(c):
                sqlst += " " + c + " TEXT, "
                exec_many += '?,'
                logger.warning("fake2db found valid custom key provided: %s" % c, extra=d)
            else:
                logger.error("fake2db does not support the custom key you provided.", extra=d )
                sys.exit(1)
                
        sqlst = sqlst[:-2] + ")"
        cursor.execute(sqlst)   
        conn.commit()
        multi_lines = []
        exec_many = exec_many[:-1] +')'
        
        try:
            for i in range(0, number_of_rows):
                multi_lines.append([rnd_id_generator(self)])
                for c in custom:
                    multi_lines[i].append(getattr(self.faker, c)())
            
            cursor.executemany(exec_many, multi_lines)
            conn.commit()
            logger.warning('custom Commits are successful after write job!', extra=d)
        except Exception as e:
            logger.error(e, extra=d)

    def database_caller_creator(self, name=None):
        '''creates a sqlite3 db
        returns the related connection object
        which will be later used to spawn the cursor
        '''

        try:
            if name:
                database = name + '.db'
            else:
                database = 'sqlite_' + str_generator(self) + '.db'

            conn = sqlite3.connect(database)
            logger.warning('Database created and opened succesfully: %s' % database, extra=d)
        except Exception:
            logger.error('Failed to connect or create database / sqlite3', extra=d)
            raise DbConnException

        return conn
    
    def data_filler_simple_registration(self, number_of_rows, conn):
        '''creates and fills the table with simple regis. information
        '''
        cursor = conn.cursor()

        cursor.execute('''
        CREATE TABLE simple_registration(id TEXT PRIMARY KEY,
        email TEXT , password TEXT)
        ''')
        conn.commit()
        multi_lines = []
        
        try:
            for i in range(0, number_of_rows):
                multi_lines.append((rnd_id_generator(self), self.faker.safe_email(), self.faker.md5(raw_output=False)))
            cursor.executemany('insert into simple_registration values(?,?,?)',multi_lines)
            conn.commit()
            logger.warning('simple_registration Commits are successful after write job!', extra=d)
        except Exception as e:
            logger.error(e, extra=d)

    def data_filler_detailed_registration(self, number_of_rows, conn):
        '''creates and fills the table with detailed regis. information
        '''
        cursor = conn.cursor()

        cursor.execute('''
        CREATE TABLE detailed_registration(id TEXT PRIMARY KEY,
        email TEXT, password TEXT, lastname TEXT,
        name TEXT, adress TEXT, phone TEXT)
        ''')
        conn.commit()
        multi_lines = []
        
        try:
            for i in range(0, number_of_rows):
                multi_lines.append((rnd_id_generator(self), self.faker.safe_email(),
                                    self.faker.md5(raw_output=False), self.faker.last_name(),
                                    self.faker.first_name(), self.faker.address(), self.faker.phone_number()))
                
            cursor.executemany('insert into detailed_registration values(?,?,?,?,?,?,?)', multi_lines)
            conn.commit()
            logger.warning('detailed_registration Commits are successful after write job!', extra=d)

        except Exception as e:
            logger.error(e, extra=d)

    def data_filler_user_agent(self, number_of_rows, conn):
        '''creates and fills the table with user agent data
        '''
        cursor = conn.cursor()

        cursor.execute('''
        CREATE TABLE user_agent(id TEXT PRIMARY KEY,
        ip TEXT, countrycode TEXT, useragent TEXT)
        ''')
        conn.commit()
        multi_lines = []
        
        try:
            for i in range(0, number_of_rows):
                multi_lines.append((rnd_id_generator(self), self.faker.ipv4(), self.faker.country_code(),
                                    self.faker.user_agent()))
                
            cursor.executemany('insert into user_agent values(?,?,?,?)', multi_lines)
            conn.commit()
            logger.warning('user_agent Commits are successful after write job!', extra=d)
        except Exception as e:
            logger.error(e, extra=d)

    def data_filler_company(self, number_of_rows, conn):
        '''creates and fills the table with company data
        '''
        cursor = conn.cursor()

        cursor.execute('''
        CREATE TABLE company(id TEXT PRIMARY KEY,
        name TEXT, sdate TEXT, email TEXT, domain TEXT, city TEXT)
        ''')
        conn.commit()
        multi_lines = []
        
        try:
            for i in range(0, number_of_rows):
                
                multi_lines.append((rnd_id_generator(self), self.faker.company(),
                                    self.faker.date(pattern="%d-%m-%Y"),
                                    self.faker.company_email(), self.faker.safe_email(),
                                    self.faker.city()))
                
            cursor.executemany('insert into company values (?,?,?,?,?,?)', multi_lines)
            conn.commit()
            logger.warning('companies Commits are successful after write job!', extra=d)
        except Exception as e:
            logger.error(e, extra=d)

    def data_filler_customer(self, number_of_rows, conn):
        '''creates and fills the table with customer data
        '''
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE customer(id TEXT PRIMARY KEY,
        name TEXT, lastname TEXT, address TEXT, country TEXT, city TEXT, registry_date TEXT, birthdate TEXT, email TEXT,
         phone_number TEXT, locale TEXT)
        ''')
        conn.commit()
        multi_lines = []
        
        try:
            for i in range(0, number_of_rows):
                
                multi_lines.append((rnd_id_generator(self), self.faker.first_name(), self.faker.last_name(), self.faker.address(),
                                    self.faker.country(), self.faker.city(), self.faker.date(pattern="%d-%m-%Y"),
                                    self.faker.date(pattern="%d-%m-%Y"), self.faker.safe_email(), self.faker.phone_number(),
                                    self.faker.locale()))
                               
            cursor.executemany('insert into customer values (?,?,?,?,?,?,?,?,?,?,?)', multi_lines)
            conn.commit()
            logger.warning('customer Commits are successful after write job!', extra=d)
        except Exception as e:
            logger.error(e, extra=d)
