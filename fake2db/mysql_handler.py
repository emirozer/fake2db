import sys

from helpers import fake2db_logger, str_generator, rnd_id_generator


logger, extra_information = fake2db_logger()

try:
    import mysql.connector
except ImportError:
    logger.error(
        'MySql Connector/Python not found on sys, '
        'you need to get it : http://dev.mysql.com/downloads/connector/python/', extra=extra_information)

try:
    from faker import Factory
except ImportError:
    logger.error('faker package not found onto python packages, please run : \
    pip install -r requirements.txt  \
    on the root of the project', extra=extra_information)


class Fake2dbMySqlHandler():
    faker = Factory.create()

    def fake2db_mysql_initiator(self, host, port, number_of_rows, name=None):
        '''Main handler for the operation
        '''
        rows = number_of_rows

        if name:
            cursor, conn = self.database_caller_creator(host, port, name)
        else:
            cursor, conn = self.database_caller_creator(host, port)

        tables = self.mysql_table_creator()
        keys = tables.keys()

        for key in keys:
            try:
                cursor.execute(tables[key])
                conn.commit()
            except mysql.connector.Error as err:
                logger.error(err.msg, extra=extra_information)
            else:
                logger.info("OK", extra=extra_information)

        logger.warning('Table creation ops finished', extra=extra_information)
        self.data_filler_simple_registration(rows, cursor, conn)
        self.data_filler_detailed_registration(rows, cursor, conn)
        self.data_filler_company(rows, cursor, conn)
        self.data_filler_user_agent(rows, cursor, conn)
        self.data_filler_customer(rows, cursor, conn)
        cursor.close()
        conn.close()

    def database_caller_creator(self, host, port, name=None):
        '''creates a mysql db
        returns the related connection object
        which will be later used to spawn the cursor
        '''
        cursor = None
        conn = None

        try:
            if name:
                db = name
            else:
                db = 'mysql_' + str_generator(self)

            conn = mysql.connector.connect(user='root', host=host, port=port)
            cursor = conn.cursor()
            cursor.execute('CREATE DATABASE IF NOT EXISTS ' + db)
            cursor.execute('USE ' + db)
            logger.warning('Database created and opened succesfully: %s' % db, extra=extra_information)

        except mysql.connector.Error as err:
            logger.error(err.msg, extra=extra_information)
            sys.exit(1)

        return cursor, conn

    def mysql_table_creator(self):
        '''Create all the tables in one method
        '''
        tables = {}

        tables['simple_registration'] = (
            "CREATE TABLE `simple_registration` ("
            "  `id` varchar(300) NOT NULL,"
            "  `email` varchar(300) NOT NULL,"
            "  `password` varchar(300) NOT NULL,"
            "  PRIMARY KEY (`id`)"
            ") ENGINE=InnoDB")

        tables['detailed_registration'] = (
            "CREATE TABLE `detailed_registration` ("
            "  `id` varchar(300) NOT NULL,"
            "  `email` varchar(300) NOT NULL,"
            "  `password` varchar(300) NOT NULL,"
            "  `lastname` varchar(300) NOT NULL,"
            "  `name` varchar(300) NOT NULL,"
            "  `address` varchar(300) NOT NULL,"
            "  `phone` varchar(300) NOT NULL,"
            "  PRIMARY KEY (`id`)"
            ") ENGINE=InnoDB")

        tables['user_agent'] = (
            "CREATE TABLE `user_agent` ("
            "  `id` varchar(300) NOT NULL,"
            "  `ip` varchar(300) NOT NULL,"
            "  `countrycode` varchar(300) NOT NULL,"
            "  `useragent` varchar(300) NOT NULL,"
            "  PRIMARY KEY (`id`)"
            ") ENGINE=InnoDB")

        tables['company'] = (
            "CREATE TABLE `company` ("
            "  `id` varchar(300) NOT NULL,"
            "  `name` varchar(300) NOT NULL,"
            "  `sdate` date NOT NULL,"
            "  `email` varchar(300) NOT NULL,"
            "  `domain` varchar(300) NOT NULL,"
            "  `city` varchar(300) NOT NULL,"
            "  PRIMARY KEY (`id`)"
            ") ENGINE=InnoDB")

        tables['customer'] = (
            "CREATE TABLE `customer` ("
            "  `id` varchar(300) NOT NULL,"
            "  `name` varchar(300) NOT NULL,"
            "  `lastname` varchar(300) NOT NULL,"
            "  `address` varchar(300) NOT NULL,"
            "  `country` varchar(300) NOT NULL,"
            "  `city` varchar(300) NOT NULL,"
            "  `registry_date` varchar(300) NOT NULL,"
            "  `birthdate` varchar(300) NOT NULL,"
            "  `email` varchar(300) NOT NULL,"
            "  `phone_number` varchar(300) NOT NULL,"
            "  `locale` varchar(300) NOT NULL,"
            "  PRIMARY KEY (`id`)"
            ") ENGINE=InnoDB")

        return tables

    def data_filler_simple_registration(self, number_of_rows, cursor, conn):
        '''creates and fills the table with simple regis. information
        '''

        try:
            for i in range(0, number_of_rows):
                simple_registration_payload = ("INSERT INTO simple_registration "
                                               "(id, email, password) "
                                               "VALUES (%s, %s, %s)")

                simple_registration_data = (
                    rnd_id_generator(self), self.faker.safe_email(), self.faker.md5(raw_output=False))
                cursor.execute(simple_registration_payload, simple_registration_data)
                conn.commit()

            logger.warning('simple_registration Commits are successful after write job!', extra=extra_information)
        except Exception as e:
            logger.error(e, extra=extra_information)

    def data_filler_detailed_registration(self, number_of_rows, cursor, conn):
        '''creates and fills the table with detailed regis. information
        '''

        try:
            for i in range(0, number_of_rows):
                detailed_registration_payload = ("INSERT INTO detailed_registration "
                                                 "(id, email, password, lastname, name,"
                                                 "address, phone) "
                                                 "VALUES (%s, %s, %s, %s, %s, %s, %s)")
                detailed_registration_data = (
                    rnd_id_generator(self), self.faker.safe_email(), self.faker.md5(raw_output=False),
                    self.faker.last_name(), self.faker.name(), self.faker.address(), self.faker.phone_number())

                cursor.execute(detailed_registration_payload, detailed_registration_data)
                conn.commit()

            logger.warning('detailed_registration Commits are successful after write job!', extra=extra_information)

        except Exception as e:
            logger.error(e, extra=extra_information)

    def data_filler_user_agent(self, number_of_rows, cursor, conn):
        '''creates and fills the table with user agent data
        '''
        try:
            for i in range(0, number_of_rows):
                user_agent_payload = ("INSERT INTO user_agent "
                                      "(id, ip, countrycode, useragent) "
                                      "VALUES (%s, %s, %s, %s)")
                user_agent_data = (rnd_id_generator(self), self.faker.ipv4(), self.faker.country_code(),
                                   self.faker.user_agent())
                cursor.execute(user_agent_payload, user_agent_data)
                conn.commit()

            logger.warning('user_agent Commits are successful after write job!', extra=extra_information)
        except Exception as e:
            logger.error(e, extra=extra_information)

    def data_filler_company(self, number_of_rows, cursor, conn):
        '''creates and fills the table with company data
        '''
        try:
            for i in range(0, number_of_rows):
                companies_payload = ("INSERT INTO company "
                                     "(id, name, sdate, email, domain, city) "
                                     "VALUES (%s, %s, %s, %s, %s, %s)")
                companies_data = (rnd_id_generator(self), self.faker.company(), self.faker.date(pattern="%Y-%m-%d"),
                                  self.faker.company_email(), self.faker.safe_email(), self.faker.city())
                cursor.execute(companies_payload, companies_data)
                conn.commit()
            logger.warning('companies Commits are successful after write job!', extra=extra_information)
        except Exception as e:
            logger.error(e, extra=extra_information)

    def data_filler_customer(self, number_of_rows, cursor, conn):
        '''creates and fills the table with customer
        '''

        try:
            for i in range(0, number_of_rows):
                customer_payload = ("INSERT INTO customer "
                                    "(id, name, lastname, address, country, city, registry_date, birthdate, email, "
                                    "phone_number, locale)"
                                    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
                customer_data = (
                    rnd_id_generator(self), self.faker.name(), self.faker.last_name(), self.faker.address(),
                    self.faker.country(), self.faker.city(), self.faker.date(pattern="%d-%m-%Y"),
                    self.faker.date(pattern="%d-%m-%Y"), self.faker.safe_email(), self.faker.phone_number(),
                    self.faker.locale())

                cursor.execute(customer_payload, customer_data)

                conn.commit()

            logger.warning('detailed_registration Commits are successful after write job!', extra=extra_information)
        except Exception as e:
            logger.error(e, extra=extra_information)
