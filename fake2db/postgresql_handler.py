import sys
import time
import getpass
import subprocess

from helpers import fake2db_logger, str_generator

logger, extra_information = fake2db_logger()
d = extra_information

try:
    from faker import Factory
except ImportError:
    logger.error('faker package not found onto python packages, please run : \
    pip install -r requirements.txt  \
    on the root of the project')

try:
    import psycopg2
except ImportError:
    logger.error('psycopg2 package not found onto python packages, please run : \
    pip install -r requirements.txt  \
    on the root of the project')


class Fake2dbPostgresqlHandler():
    faker = Factory.create()

    def fake2db_postgresql_initiator(self, host, port, number_of_rows, name=None):
        '''Main handler for the operation
        '''
        rows = number_of_rows
        
        if name:
            cursor, conn = self.database_caller_creator(host, port, name)
        else:
            cursor, conn = self.database_caller_creator(host, port)
        
        self.data_filler_simple_registration(rows, cursor, conn)
        self.data_filler_detailed_registration(rows, cursor, conn)
        self.data_filler_company(rows, cursor, conn)
        self.data_filler_user_agent(rows, cursor, conn)
        self.data_filler_customer(rows, cursor, conn)
        cursor.close()
        conn.close()

    def database_caller_creator(self, host, port, name=None):
        '''creates a postgresql db
        returns the related connection object
        which will be later used to spawn the cursor
        '''
        cursor = None
        conn = None
        username = getpass.getuser()

        try:
            if name:
                db = name
            else:
                db = 'postgresql_' + str_generator(self)
                
            subprocess.Popen("createdb --no-password --owner " + username + " " + db, shell=True)
            time.sleep(1)
            conn = psycopg2.connect("dbname=" + db + " user=" + username + " host=" + host + " port=" + port)
            cursor = conn.cursor()
            logger.warning('Database created and opened succesfully: %s' % db, extra=d)
        except Exception as err:
            logger.error(err, extra=d)

        return cursor, conn

    def data_filler_simple_registration(self, number_of_rows, cursor, conn):
        '''creates and fills the table with simple regis. information
        '''

        cursor.execute("CREATE TABLE simple_registration (id serial PRIMARY KEY, email varchar(300), password varchar(300));")
        conn.commit()

        try:

            for i in range(0, number_of_rows):
                cursor.execute("INSERT INTO simple_registration "
                               "(email, password) "
                               "VALUES (%s, %s)", (self.faker.safe_email(), self.faker.md5(raw_output=False)))
                conn.commit()

            logger.warning('simple_registration Commits are successful after write job!', extra=d)

        except Exception as e:
            logger.error(e, extra=d)

    def data_filler_detailed_registration(self, number_of_rows, cursor, conn):
        '''creates and fills the table with detailed regis. information
        '''

        cursor.execute(
            "CREATE TABLE detailed_registration "
            "(id serial PRIMARY KEY, email varchar(300), password varchar(300), "
            "lastname varchar(300), name varchar(300), adress varchar(300), phone varchar(300));")
        conn.commit()
        try:

            for i in range(0, number_of_rows):
                cursor.execute("INSERT INTO detailed_registration "
                               "(email, password, lastname, name, adress, phone) "
                               "VALUES (%s, %s, %s, %s, %s, %s)",
                               (self.faker.safe_email(), self.faker.md5(raw_output=False), self.faker.last_name(),
                                self.faker.name(), self.faker.address(), self.faker.phone_number()))
                conn.commit()

            logger.warning('detailed_registration Commits are successful after write job!', extra=d)

        except Exception as e:
            logger.error(e, extra=d)

    def data_filler_user_agent(self, number_of_rows, cursor, conn):
        '''creates and fills the table with user agent data
        '''

        cursor.execute(
            "CREATE TABLE user_agent (id serial PRIMARY KEY, ip varchar(300), countrycode varchar(300), useragent varchar(300));")
        try:

            for i in range(0, number_of_rows):
                cursor.execute("INSERT INTO user_agent "
                               "(ip, countrycode, useragent) "
                               "VALUES (%s, %s, %s)",
                               (self.faker.ipv4(), self.faker.country_code(),
                                self.faker.user_agent()))
                conn.commit()

            logger.warning('user_agent Commits are successful after write job!', extra=d)
        except Exception as e:
            logger.error(e, extra=d)

    def data_filler_company(self, number_of_rows, cursor, conn):
        '''creates and fills the table with company data
        '''

        cursor.execute(
            "CREATE TABLE company (id serial PRIMARY KEY, "
            "name varchar(300), sdate date, email varchar(300), domain varchar(300), city varchar(300));")
        conn.commit()
        try:
            for i in range(0, number_of_rows):
                companies_payload = ("INSERT INTO companies "
                                     "(name, sdate, email, domain, city) "
                                     "VALUES (%s, %s, %s, %s, %s)",
                                     (self.faker.name(), self.faker.date(pattern="%d-%m-%Y"),
                                      self.faker.company_email(), self.faker.safe_email(), self.faker.city()))
                conn.commit()

            logger.warning('companies Commits are successful after write job!', extra=d)
        except Exception as e:
            logger.error(e, extra=d)

    def data_filler_customer(self, number_of_rows, cursor, conn):
        '''creates and fills the table with customer data
        '''

        cursor.execute(
            "CREATE TABLE customer (id serial PRIMARY KEY, "
            "name varchar(300), lastname varchar(300), address varchar(300), country varchar(300), "
            "city varchar(300), registry_date varchar(300), birthdate varchar(300), email varchar(300), "
            "phone_number varchar(300), locale varchar(300));")
        conn.commit()
        try:
            for i in range(0, number_of_rows):
                cursor.execute("INSERT INTO customer "
                               "(name, lastname, address, country, city, registry_date, "
                               "birthdate, email, phone_number, locale)"
                               "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                               (self.faker.name(), self.faker.last_name(), self.faker.address(),
                                self.faker.country(), self.faker.city(), self.faker.date(pattern="%d-%m-%Y"),
                                self.faker.date(pattern="%d-%m-%Y"), self.faker.safe_email(), self.faker.phone_number(),
                                self.faker.locale()))
            conn.commit()
            logger.warning('customer Commits are successful after write job!', extra=d)
        except Exception as e:
            logger.error(e, extra=d)
