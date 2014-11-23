import random
import uuid
import string
import logging
import getpass
import socket
import sys
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
    import mysql.connector
except ImportError:
    logger.error('MySql Connector/Python not found on sys, you need to get it : http://dev.mysql.com/downloads/connector/python/')
    sys.exit(0)

class fake2dbMySqlHandler():
        

    def str_generator(self):
        '''generates uppercase 6 chars
        '''
        return ''.join(random.choice(string.ascii_uppercase) for i in range(6))

    
    def _rnd_id_generator(self):
        '''generates a UUID such as :
        UUID('dd1098bd-70ac-40ea-80ef-d963f09f95a7')
        than gets rid of dashes
        '''
        return str(uuid.uuid4()).replace('-', '')

    def fake2db_mysql_initiator(self, number_of_rows):
        '''Main handler for the operation
        '''
        rows = number_of_rows
        conn = self.database_caller_creator()
        TABLES = self.mysql_table_creator()
        cursor = conn.cursor()

        for name, ddl in TABLES.iteritems():
            try:
                logger.info("Creating table {}: ".format(name), extra=d)
                cursor.execute(ddl)
            except mysql.connector.Error as err:
                logger.error(err.msg, extra=d)
            else:
                logger.info("OK", extra=d)

        self.data_filler_simple_registration(rows, conn)
        self.data_filler_detailed_registration(rows, conn)
        self.data_filler_company(rows, conn)
        self.data_filler_user_agent(rows, conn)
        conn.close()

    def database_caller_creator(self):
        '''creates a mysql db
        returns the related connection object
        which will be later used to spawn the cursor
        '''
        database = ''
        conn = None
        
        try:
            database = 'mysql_' + self.str_generator() + '.db'
            conn = mysql.connector.connect(user='admin', password='admin',
                              host='127.0.0.1',
                                           database=database)
            logger.warning('Database created and opened succesfully: %s' %database, extra=d)
        except mysql.connector.Error as err:
            logger.error(err.message, extra=d)
                
            
        return conn
        

    def mysql_table_creator(self):
        '''Create all the tables in one method
        '''
        TABLES = {}
        
        TABLES['simple_registration'] = (
            "CREATE TABLE `simple_registration` ("
            "  `id` int NOT NULL AUTO_INCREMENT,"
            "  `email` varchar NOT NULL,"
            "  `password` varchar NOT NULL,"
            "  PRIMARY KEY (`id`)"
            ") ENGINE=InnoDB")

        TABLES['detailed_registration'] = (
            "CREATE TABLE `simple_registration` ("
            "  `id` int NOT NULL AUTO_INCREMENT,"
            "  `email` varchar NOT NULL,"
            "  `password` varchar NOT NULL,"
            "  `lastname` varchar NOT NULL,"
            "  `name` varchar NOT NULL,"
            "  `adress` varchar NOT NULL,"
            "  `phone` varchar NOT NULL,"
            "  PRIMARY KEY (`id`)"
            ") ENGINE=InnoDB")

        TABLES['user_agent'] = (
            "CREATE TABLE `user_agent` ("
            "  `id` int NOT NULL AUTO_INCREMENT,"
            "  `ip` varchar NOT NULL,"
            "  `countrycode` varchar NOT NULL,"
            "  `useragent` varchar NOT NULL,"
            "  PRIMARY KEY (`id`)"
            ") ENGINE=InnoDB")

        TABLES['companies'] = (
            "CREATE TABLE `user_agent` ("
            "  `id` int NOT NULL AUTO_INCREMENT,"
            "  `name` varchar NOT NULL,"
            "  `sdate` varchar NOT NULL,"
            "  `email` varchar NOT NULL,"
            "  `domain` varchar NOT NULL,"
            "  `city` varchar NOT NULL,"
            "  PRIMARY KEY (`id`)"
            ") ENGINE=InnoDB")

        return TABLES

    def data_filler_simple_registration(self, number_of_rows, conn):
        '''creates and fills the table with simple regis. information
        '''
        # incoming data structure 
        # {'emails' : a_list_of_emails,
        # 'passwords': a_list_of_passwords
        # }
        db_patterns_instance = DbPatterns()
        data = db_patterns_instance.simple_registration(number_of_rows)
        cursor = conn.cursor()
        
        for password in data['passwords']:
            for email in data['emails']:
                try:
                    simple_registration_payload = ("INSERT INTO simple_registration "
                                                   "(id, email, password) "
                                                   "VALUES (%s, %s, %s)")
                    
                    simple_registration_data = (self._rnd_id_generator(), email, password)
                    cursor.execute(simple_registration_payload, simple_registration_data)
                    conn.commit()
                    
                except Exception as e:
                    logger.error(e, extra=d)

        logger.warning('simple_registration Commits are successful after write job!', extra=d)

    def data_filler_detailed_registration(self, number_of_rows, conn):
        '''creates and fills the table with detailed regis. information
        '''
        # incoming data structure
        #fake_data = {'names': list_of_names,
        #             'lastnames': list_of_lastnames,
        #             'addresses': list_of_lastnames,
        #             'phones': list_of_phones,
        #             'emails': list_of_emails,
        #             'passwords': list_of_passwords}

        db_patterns_instance = DbPatterns()
        data = db_patterns_instance.detailed_registration(number_of_rows)
        cursor = conn.cursor()
        
        # UGLY AS HELL , TODO: USE ITERTOOLS!!!!!!
        # TEMPORARY
        for password in data['passwords']:
            for email in data['emails']:
                for name in data['names']:
                    for lastname in data['lastnames']:
                        for phone in data['phones']:
                            for address in data['addresses']:
                                try:

                                    detailed_registration_payload = ("INSERT INTO detailed_registration "
                                                                     "(id, email, password, lastname, name, adress, phone) "
                                                                     "VALUES (%s, %s, %s, %s, %s, %s, %s)")
                                    detailed_registration_data = (self._rnd_id_generator(),email,password,lastname,name,address,phone)
                                    cursor.execute(detailed_registration_payload, detailed_registration_data)
                                    conn.commit()
                                    
                                except Exception as e:
                                    logger.error(e, extra=d)

        logger.warning('detailed_registration Commits are successful after write job!', extra=d)

    def data_filler_user_agent(self, number_of_rows, conn):
        '''creates and fills the table with user agent data
        '''
        # incoming data structure
        #fake_data = {'ips': list_of_ips,
        #             'countrycodes': list_of_countrycodes,
        #             'useragents': list_of_useragents}

        db_patterns_instance = DbPatterns()
        data = db_patterns_instance.user_agent(number_of_rows)
        cursor = conn.cursor()
        
        for ip in data['ips']:
            for countrycode in data['countrycodes']:
                for useragent in data['useragents']:
                    try:
                        user_agent_payload = ("INSERT INTO user_agent "
                                                   "(id, ip, countrycode, useragent) "
                                                   "VALUES (%s, %s, %s, %s)")
                        user_agent_data = (self._rnd_id_generator(), ip, countrycode, useragent)
                        cursor.execute(user_agent_payload, user_agent_data)
                        conn.commit()
                        
                    except Exception as e:
                        logger.error(e, extra=d)

        logger.warning('user_agent Commits are successful after write job!', extra=d)
        
    def data_filler_company(self, number_of_rows, conn):
        '''creates and fills the table with company data
        '''
        # incoming data structure
        #fake_data = {'names': list_of_names,
        #             'sdates': list_of_sdates,
        #             'emails': list_of_emails,
        #             'domains': list_of_domains,
        #             'cities': list_of_cities
        db_patterns_instance = DbPatterns()
        data = db_patterns_instance.company(number_of_rows)
        cursor = conn.cursor()
        
        for name in data['names']:
            for sdate in data['sdates']:
                for email in data['emails']:
                    for domain in data['domains']:
                        for city in data['cities']:
                            try:
                                companies_payload = ("INSERT INTO companies "
                                                     "(id, name, sdate, email, domain, city) "
                                                     "VALUES (%s, %s, %s, %s, %s, %s)")
                                companies_data = (self._rnd_id_generator(), name, sdate, email, domain, city)
                                cursor.execute(companies_payload, companies_data)
                                conn.commit()
                                
                                logger.warning('CLOSING CURSOR!', extra=d)
                                cursor.close()

                            except Exception as e:
                                logger.error(e, extra=d)
        logger.warning('companies Commits are successful after write job!', extra=d)
