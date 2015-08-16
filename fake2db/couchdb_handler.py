import couchdb
from helpers import fake2db_logger, lower_str_generator, rnd_id_generator


logger, extra_information = fake2db_logger()
d = extra_information

try:
    from faker import Factory
except ImportError:
    logger.error('faker package not found onto python packages, please run : \
    pip install -r requirements.txt  \
    on the root of the project')


class Fake2dbCouchdbHandler():
    faker = Factory.create()

    def fake2db_couchdb_initiator(self, number_of_rows, name=None):
        '''Main handler for the operation
        '''
        rows = number_of_rows
        db = self.database_caller_creator(name)

        self.data_filler_simple_registration(rows, db)
        self.data_filler_detailed_registration(rows, db)
        self.data_filler_company(rows, db)
        self.data_filler_user_agent(rows, db)
        self.data_filler_customer(rows, db)

    def database_caller_creator(self, name=None):
        '''creates a couchdb database
        returns the related connection object
        which will be later used to spawn the cursor
        '''

        couch = couchdb.Server()

        if name:
            db = couch.create(name) 
        else:
            n = 'couchdb_' + lower_str_generator(self)
            db = couch.create(n)
            logger.warning('couchdb database created with the name: %s',n, extra=d)
            

        return db

    def data_filler_simple_registration(self, number_of_rows, db):
        '''creates and fills the table with simple regis. information
        '''

        try:
            simple_registration = db.simple_registration
            data_list = list()
            for i in range(0, number_of_rows):
                post_simple_reg = {"id": rnd_id_generator(self),
                                   "email": self.faker.safe_email(),
                                   "password": self.faker.md5(raw_output=False)
                                   }
                data_list.append(post_simple_reg)

            simple_registration.save(data_list)
            logger.warning('simple_registration Commits are successful after write job!', extra=d)

        except Exception as e:
            logger.error(e, extra=d)

    def data_filler_detailed_registration(self, number_of_rows, db):
        '''creates and fills the table with detailed regis. information
        '''

        try:
            detailed_registration = db.detailed_registration
            data_list = list()
            for i in range(0, number_of_rows):
                post_det_reg = {"id": rnd_id_generator(self),
                                "email": self.faker.safe_email(),
                                "password": self.faker.md5(raw_output=False),
                                "lastname": self.faker.last_name(),
                                "name": self.faker.first_name(),
                                "adress": self.faker.address(),
                                "phone": self.faker.phone_number()}
                data_list.append(post_det_reg)
            detailed_registration.save(data_list)

            logger.warning('detailed_registration Commits are successful after write job!', extra=d)

        except Exception as e:
            logger.error(e, extra=d)

    def data_filler_user_agent(self, number_of_rows, db):
        '''creates and fills the table with user agent data
        '''

        try:
            user_agent = db.user_agent
            data_list = list()
            for i in range(0, number_of_rows):
                post_uo_reg = {"id": rnd_id_generator(self),
                               "ip": self.faker.ipv4(),
                               "countrycode": self.faker.country_code(),
                               "useragent": self.faker.user_agent()}
                data_list.append(post_uo_reg)
            user_agent.save(data_list)

            logger.warning('user_agent Commits are successful after write job!', extra=d)
        except Exception as e:
            logger.error(e, extra=d)

    def data_filler_company(self, number_of_rows, db):
        '''creates and fills the table with company data
        '''

        try:
            company = db.company
            data_list = list()
            for i in range(0, number_of_rows):
                post_comp_reg = {"id": rnd_id_generator(self),
                                 "name": self.faker.company(),
                                 "date": self.faker.date(pattern="%d-%m-%Y"),
                                 "email": self.faker.company_email(),
                                 "domain": self.faker.safe_email(),
                                 "city": self.faker.city()}
                data_list.append(post_comp_reg)
            company.save(data_list)
            logger.warning('companies Commits are successful after write job!', extra=d)
        except Exception as e:
            logger.error(e, extra=d)

    def data_filler_customer(self, number_of_rows, db):
        '''creates and fills the table with customer data
        '''

        try:
            customer = db.customer
            data_list = list()
            for i in range(0, number_of_rows):
                post_cus_reg = {"id": rnd_id_generator(self),
                                "name": self.faker.first_name(),
                                "lastname": self.faker.last_name(),
                                "address": self.faker.address(),
                                "country": self.faker.country(),
                                "city": self.faker.city(),
                                "registry_date": self.faker.date(pattern="%d-%m-%Y"),
                                "birthdate": self.faker.date(pattern="%d-%m-%Y"),
                                "email": self.faker.safe_email(),
                                "phone_number": self.faker.phone_number(),
                                "locale": self.faker.locale()}
                data_list.append(post_cus_reg)
            customer.save(data_list)

            logger.warning('customer Commits are successful after write job!', extra=d)
        except Exception as e:
            logger.error(e, extra=d)
