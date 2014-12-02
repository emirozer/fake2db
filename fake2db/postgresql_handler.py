import random
import string
import logging
import getpass
import socket
import sys
import time
import subprocess
from db_patterns import DbPatterns


# Pull the local ip and username for meaningful logging
username = getpass.getuser()
local_ip = socket.gethostbyname(socket.gethostname())
# Set the logger
FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'
logging.basicConfig(format=FORMAT)
d = {'clientip': local_ip, 'user': username}
logger = logging.getLogger('fake2db_logger')
# --------------------

try:
    import psycopg2
except ImportError:
    logger.error('psycopg2 package not found onto python packages, please run : \
    pip install -r requirements.txt  \
    on the root of the project')
    sys.exit(0)


class Fake2dbPostgresqlHandler():
    def str_generator(self):
        '''generates uppercase 6 chars
        '''
        return ''.join(random.choice(string.ascii_uppercase) for i in range(10))

    def fake2db_postgresql_initiator(self, number_of_rows):
        '''Main handler for the operation
        '''
        rows = number_of_rows
        cursor, conn = self.database_caller_creator()

        self.data_filler_simple_registration(rows, cursor, conn)
        self.data_filler_detailed_registration(rows, cursor, conn)
        self.data_filler_company(rows, cursor, conn)
        self.data_filler_user_agent(rows, cursor, conn)
        cursor.close()
        conn.close()

    def database_caller_creator(self):
        '''creates a postgresql db
        returns the related connection object
        which will be later used to spawn the cursor
        '''
        cursor = None
        conn = None

        try:
            db = 'postgresql_' + self.str_generator()
            subprocess.Popen("createdb --no-password --owner " + username + " " + db, shell=True)
            time.sleep(1)
            conn = psycopg2.connect("dbname=" + db + " user=" + username)
            cursor = conn.cursor()
            logger.warning('Database created and opened succesfully: %s' % db, extra=d)
        except Exception as err:
            logger.error(err, extra=d)

        return cursor, conn

    def data_filler_simple_registration(self, number_of_rows, cursor, conn):
        '''creates and fills the table with simple regis. information
        '''
        # incoming data structure 
        # {'emails' : a_list_of_emails,
        # 'passwords': a_list_of_passwords
        # }
        db_patterns_instance = DbPatterns()
        data = db_patterns_instance.simple_registration(number_of_rows)

        cursor.execute("CREATE TABLE simple_registration (id serial PRIMARY KEY, email varchar, password varchar);")

        for password in data['passwords']:
            for email in data['emails']:
                try:
                    cursor.execute("INSERT INTO simple_registration "
                                   "(id, email, password) "
                                   "VALUES (%s, %s)", (email, password))
                    conn.commit()

                except Exception as e:
                    logger.error(e, extra=d)

        logger.warning('simple_registration Commits are successful after write job!', extra=d)

    def data_filler_detailed_registration(self, number_of_rows, cursor, conn):
        '''creates and fills the table with detailed regis. information
        '''
        # incoming data structure
        # fakedata = {'names': list_of_names,
        #             'lastnames': list_of_lastnames,
        #             'addresses': list_of_lastnames,
        #             'phones': list_of_phones,
        #             'emails': list_of_emails,
        #             'passwords': list_of_passwords}

        db_patterns_instance = DbPatterns()
        data = db_patterns_instance.detailed_registration(number_of_rows)
        cursor.execute(
            "CREATE TABLE detailed_registration "
            "(id serial PRIMARY KEY, email varchar, password varchar, "
            "lastname varchar, name varchar, adress varchar, phone varchar);")
        # UGLY AS HELL , TODO: USE ITERTOOLS!!!!!!
        # TEMPORARY
        for password in data['passwords']:
            for email in data['emails']:
                for name in data['names']:
                    for lastname in data['lastnames']:
                        for phone in data['phones']:
                            for address in data['addresses']:
                                try:

                                    cursor.execute("INSERT INTO detailed_registration "
                                                   "(email, password, lastname, name, adress, phone) "
                                                   "VALUES (%s, %s, %s, %s, %s, %s)",
                                                   (email, password, lastname, name, address, phone))

                                    conn.commit()

                                except Exception as e:
                                    logger.error(e, extra=d)

        logger.warning('detailed_registration Commits are successful after write job!', extra=d)

    def data_filler_user_agent(self, number_of_rows, cursor, conn):
        '''creates and fills the table with user agent data
        '''
        # incoming data structure
        # fake_data = {'ips': list_of_ips,
        #             'countrycodes': list_of_countrycodes,
        #             'useragents': list_of_useragents}

        db_patterns_instance = DbPatterns()
        data = db_patterns_instance.user_agent(number_of_rows)
        cursor.execute(
            "CREATE TABLE user_agent (id serial PRIMARY KEY, ip varchar, countrycode varchar, useragent varchar);")
        for ip in data['ips']:
            for countrycode in data['countrycodes']:
                for useragent in data['useragents']:
                    try:
                        cursor.execute("INSERT INTO user_agent "
                                       "(ip, countrycode, useragent) "
                                       "VALUES (%s, %s, %s)", (ip, countrycode, useragent))
                        conn.commit()

                    except Exception as e:
                        logger.error(e, extra=d)

        logger.warning('user_agent Commits are successful after write job!', extra=d)

    def data_filler_company(self, number_of_rows, cursor, conn):
        '''creates and fills the table with company data
        '''
        # incoming data structure
        # fake_data = {'names': list_of_names,
        #             'sdates': list_of_sdates,
        #             'emails': list_of_emails,
        #             'domains': list_of_domains,
        #             'cities': list_of_cities
        db_patterns_instance = DbPatterns()
        data = db_patterns_instance.company(number_of_rows)
        cursor.execute(
            "CREATE TABLE company (id serial PRIMARY KEY, "
            "name varchar, sdate date, email varchar, domain varchar, city varchar);")
        for name in data['names']:
            for sdate in data['sdates']:
                for email in data['emails']:
                    for domain in data['domains']:
                        for city in data['cities']:
                            try:
                                companies_payload = ("INSERT INTO companies "
                                                     "(name, sdate, email, domain, city) "
                                                     "VALUES (%s, %s, %s, %s, %s)", (name, sdate, email, domain, city))
                                conn.commit()

                            except Exception as e:
                                logger.error(e, extra=d)

        logger.warning('companies Commits are successful after write job!', extra=d)
