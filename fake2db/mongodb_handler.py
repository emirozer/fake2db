from helpers import fake2db_logger, str_generator, rnd_id_generator


logger, extra_information = fake2db_logger()
d = extra_information

try:
    import pymongo
except ImportError:
    logger.error('pymongo package not found onto python packages, please run : \
    pip install -r requirements.txt  \
    on the root of the project')

try:
    from faker import Factory
except ImportError:
    logger.error('faker package not found onto python packages, please run : \
    pip install -r requirements.txt  \
    on the root of the project')


class Fake2dbMongodbHandler():
    faker = Factory.create()

    def fake2db_mongodb_initiator(self, host, port, number_of_rows, name=None):
        '''Main handler for the operation
        '''
        rows = number_of_rows
        
        if name:
            db = self.database_caller_creator(host, port, name)
        else:
            db = self.database_caller_creator(host, port)

        self.data_filler_simple_registration(rows, db)
        self.data_filler_detailed_registration(rows, db)
        self.data_filler_company(rows, db)
        self.data_filler_user_agent(rows, db)
        self.data_filler_customer(rows, db)
        
        
    def database_caller_creator(self, host, port, name=None):
        '''creates a mongodb database
        returns the related connection object
        which will be later used to spawn the cursor
        '''
                
        client = pymongo.MongoClient(host, port)
        
        if name:
            db = client[name]
        else:
            db = client['mongodb_' + str_generator(self)]
        
        return db
    
    def data_filler_simple_registration(self, number_of_rows, db):
        '''creates and fills the table with simple regis. information
        '''
                
        try:
            simple_registration = db.simple_registration
            
            for i in range(0, number_of_rows):
                post_simple_reg = {"id": rnd_id_generator(self),
                                   "email": self.faker.safe_email(),
                                   "password": self.faker.md5(raw_output=False)
                                   }
                
                simple_registration.insert(post_simple_reg)
                
            logger.warning('simple_registration Commits are successful after write job!', extra=d)
            
        except Exception as e:
            logger.error(e, extra=d)

    def data_filler_detailed_registration(self, number_of_rows, db):
        '''creates and fills the table with detailed regis. information
        '''
                
        try:
            detailed_registration = db.detailed_registration
            
            for i in range(0, number_of_rows):
                post_det_reg = {"id": rnd_id_generator(self),
                               "email": self.faker.safe_email(),
                                "password": self.faker.md5(raw_output=False),
                                "lastname": self.faker.last_name(),
                                "name": self.faker.name(),
                                "adress": self.faker.address(),
                                "phone": self.faker.phone_number()
                            }
                detailed_registration.insert(post_det_reg)
                
            logger.warning('detailed_registration Commits are successful after write job!', extra=d)
            
        except Exception as e:
            logger.error(e, extra=d)

    def data_filler_user_agent(self, number_of_rows, db):
        '''creates and fills the table with user agent data
        '''

        try:
            user_agent = db.user_agent
            
            for i in range(0, number_of_rows):
                post_uo_reg={"id": rnd_id_generator(self),
                             "ip": self.faker.ipv4(),
                             "countrycode": self.faker.country_code(),
                            "useragent": self.faker.user_agent()
                }
                user_agent.insert(post_uo_reg)
                
            logger.warning('user_agent Commits are successful after write job!', extra=d)
        except Exception as e:
            logger.error(e, extra=d)

    def data_filler_company(self, number_of_rows, db):
        '''creates and fills the table with company data
        '''

        try:
            company = db.company
            
            for i in range(0, number_of_rows):
                post_comp_reg = {"id": rnd_id_generator(self),
                                 "name": self.faker.name(),
                                 "date": self.faker.date(pattern="%d-%m-%Y"),
                                 "email": self.faker.company_email(),
                                 "domain": self.faker.safe_email(),
                                 "city": self.faker.city()
                }
                company.insert(post_comp_reg)
            logger.warning('companies Commits are successful after write job!', extra=d)
        except Exception as e:
            logger.error(e, extra=d)

        
    def data_filler_customer(self, number_of_rows, db):
        '''creates and fills the table with customer data
        '''
        
        try:
            customer = db.customer
            for i in range(0, number_of_rows):
                post_cus_reg = {"id": rnd_id_generator(self),
                                "name": self.faker.name(),
                                "lastname": self.faker.last_name(),
                                "address": self.faker.address(),
                                "country": self.faker.country(),
                                "city": self.faker.city(),
                                "registry_date": self.faker.date(pattern="%d-%m-%Y"),
                                "birthdate": self.faker.date(pattern="%d-%m-%Y"),
                                "email": self.faker.safe_email(),
                                "phone_number": self.faker.phone_number(),
                                "locale": self.faker.locale()
                }
                
                customer.insert(post_cus_reg)
                
            logger.warning('customer Commits are successful after write job!', extra=d)
        except Exception as e:
            logger.error(e, extra=d)
