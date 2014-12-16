import sqlite3

from helpers import fake2db_logger, str_generator, rnd_id_generator

logger, extra_information = fake2db_logger()
d = extra_information

try:
    from faker import Factory
except ImportError:
    logger.error('faker package not found onto python packages, please run : \
    pip install -r requirements.txt  \
    on the root of the project', extra=d)


class DbConnException(Exception):
    """Database Connection or Creation Exception"""


class Fake2dbSqliteHandler():
    faker = Factory.create()

    def fake2db_sqlite_initiator(self, number_of_rows, name=None):
        '''Main handler for the operation
        '''
        rows = number_of_rows
        
        if name:
            conn = self.database_caller_creator(name)
        else:
            conn = self.database_caller_creator()
            
        self.data_filler_simple_registration(rows, conn)
        self.data_filler_detailed_registration(rows, conn)
        self.data_filler_company(rows, conn)
        self.data_filler_user_agent(rows, conn)
        self.data_filler_customer(rows, conn)
        conn.close()

    def database_caller_creator(self, name=None):
        '''creates a sqlite3 db
        returns the related connection object
        which will be later used to spawn the cursor
        '''
        database = ''
        try:
            if name:
                database = name + '.db'
            else:
                database = 'sqlite_' + str_generator(self) + '.db'
                
            conn = sqlite3.connect(database)
            logger.warning('Database created and opened succesfully: %s' % database, extra=d)
        except:
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
        try:
            for i in range(0, number_of_rows):
                cursor.execute('insert into simple_registration values(?,?,?)',
                               (rnd_id_generator(self), self.faker.safe_email(), self.faker.md5(raw_output=False)))
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

        try:
            for i in range(0, number_of_rows):
                cursor.execute('insert into detailed_registration values(?,?,?,?,?,?,?)', (
                    rnd_id_generator(self), self.faker.safe_email(), self.faker.md5(raw_output=False),
                    self.faker.last_name(), self.faker.name(), self.faker.address(), self.faker.phone_number()))
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

        try:
            for i in range(0, number_of_rows):
                cursor.execute('insert into user_agent values(?,?,?,?)',
                               (rnd_id_generator(self), self.faker.ipv4(), self.faker.country_code(),
                                self.faker.user_agent()))
                conn.commit()
            logger.warning('user_agent Commits are successful after write job!', extra=d)
        except Exception as e:
            logger.error(e, extra=d)

    def data_filler_company(self, number_of_rows, conn):
        '''creates and fills the table with company data
        '''
        cursor = conn.cursor()

        cursor.execute('''
        CREATE TABLE companies(id TEXT PRIMARY KEY, 
        name TEXT, sdate TEXT, email TEXT, domain TEXT, city TEXT)
        ''')
        conn.commit()
        try:
            for i in range(0, number_of_rows):
                cursor.execute('insert into companies values (?,?,?,?,?,?)',
                               (rnd_id_generator(self), self.faker.name(), self.faker.date(pattern="%d-%m-%Y"),
                                self.faker.company_email(), self.faker.safe_email(), self.faker.city()))
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
        try:
            for i in range(0, number_of_rows):
                cursor.execute('insert into customer values (?,?,?,?,?,?,?,?,?,?,?)',
                               (rnd_id_generator(self), self.faker.name(), self.faker.last_name(), self.faker.address(),
                                self.faker.country(), self.faker.city(), self.faker.date(pattern="%d-%m-%Y"),
                                self.faker.date(pattern="%d-%m-%Y"), self.faker.safe_email(), self.faker.phone_number(),
                                self.faker.locale()))
            conn.commit()
            logger.warning('customer Commits are successful after write job!', extra=d)
        except Exception as e:
            logger.error(e, extra=d)
