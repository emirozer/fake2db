import redis
from helpers import fake2db_logger, rnd_id_generator


logger, extra_information = fake2db_logger()
d = extra_information

try:
    from faker import Factory
except ImportError:
    logger.error('faker package not found onto python packages, please run : \
    pip install -r requirements.txt  \
    on the root of the project')


class Fake2dbRedisHandler():
    faker = Factory.create()

    def fake2db_mongodb_initiator(self, host, port, number_of_rows, name=None):
        '''Main handler for the operation
        '''

        if name:
            db = self.database_caller_creator(host, port, name)
        else:
            db = self.database_caller_creator(host, port)

        self.data_filler_simple_registration(number_of_rows, db)
        self.data_filler_detailed_registration(number_of_rows, db)
        self.data_filler_company(number_of_rows, db)
        self.data_filler_user_agent(number_of_rows, db)
        self.data_filler_customer(number_of_rows, db)

    def database_caller_creator(self, host, port, name=None):
        '''creates a redis connection object
        which will be later used to modify the db
        '''
        name = name or 0
        client = redis.StrictRedis(host=host, port=port, db=name)
        pipe = client.pipeline(transaction=False)

        return pipe

    def data_filler_simple_registration(self, number_of_rows, pipe):
        '''creates keys with simple regis. information
        '''

        try:
            for i in range(0, number_of_rows):
                pipe.mset({'simple_registration:%s:id' % i: rnd_id_generator(self),
                           'simple_registration:%s:email' % i: self.faker.safe_email(),
                           'simple_registration:%s:password' % i: self.faker.md5(raw_output=False)})
            pipe.execute()
            logger.warning('simple_registration Commits are successful after write job!', extra=d)

        except Exception as e:
            logger.error(e, extra=d)

    def data_filler_detailed_registration(self, number_of_rows, pipe):
        '''creates keys with detailed regis. information
        '''

        try:
            for i in range(0, number_of_rows):
                pipe.mset({'detailed_registration:%s:id' % i: rnd_id_generator(self),
                           'detailed_registration:%s:email' % i: self.faker.safe_email(),
                           'detailed_registration:%s:password' % i: self.faker.md5(raw_output=False),
                           'detailed_registration:%s:lastname' % i: self.faker.last_name(),
                           'detailed_registration:%s:name' % i: self.faker.name(),
                           'detailed_registration:%s:address' % i: self.faker.address(),
                           'detailed_registration:%s:phone' % i: self.faker.phone_number()})
            pipe.execute()
            logger.warning('detailed_registration Commits are successful after write job!', extra=d)

        except Exception as e:
            logger.error(e, extra=d)

    def data_filler_user_agent(self, number_of_rows, pipe):
        '''creates keys with user agent data
        '''

        try:
            for i in range(0, number_of_rows):
                pipe.mset({'user_agent:%s:id' % i: rnd_id_generator(self),
                           'user_agent:%s:ip' % i: self.faker.ipv4(),
                           'user_agent:%s:countrycode' % i: self.faker.country_code(),
                           'user_agent:%s:useragent' % i: self.faker.user_agent()})
            pipe.execute()
            logger.warning('user_agent Commits are successful after write job!', extra=d)

        except Exception as e:
            logger.error(e, extra=d)

    def data_filler_company(self, number_of_rows, pipe):
        '''creates keys with company data
        '''

        try:
            for i in range(0, number_of_rows):
                pipe.mset({'company:%s:id' % i: rnd_id_generator(self),
                           'company:%s:name' % i: self.faker.company(),
                           'company:%s:date' % i: self.faker.date(pattern="%d-%m-%Y"),
                           'company:%s:email' % i: self.faker.safe_email(),
                           'company:%s:domain' % i: self.faker.safe_email(),
                           'company:%s:city' % i: self.faker.city()})
            pipe.execute()
            logger.warning('companies Commits are successful after write job!', extra=d)

        except Exception as e:
            logger.error(e, extra=d)

    def data_filler_customer(self, number_of_rows, pipe):
        '''creates keys with customer data
        '''

        try:
            for i in range(0, number_of_rows):
                pipe.mset({'customer:%s:id' % i: rnd_id_generator(self),
                           'customer:%s:name' % i: self.faker.name(),
                           'customer:%s:lastname' % i: self.faker.last_name(),
                           'customer:%s:address' % i: self.faker.address(),
                           'customer:%s:country' % i: self.faker.country(),
                           'customer:%s:city' % i: self.faker.city(),
                           'customer:%s:registry_date' % i: self.faker.date(pattern="%d-%m-%Y"),
                           'customer:%s:birthdate' % i: self.faker.date(pattern="%d-%m-%Y"),
                           'customer:%s:email' % i: self.faker.safe_email(),
                           'customer:%s:phone_number' % i: self.faker.phone_number(),
                           'customer:%s:locale' % i: self.faker.locale()})
            pipe.execute()
            logger.warning('customer Commits are successful after write job!', extra=d)

        except Exception as e:
            logger.error(e, extra=d)
