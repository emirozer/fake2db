import sys
from helpers import fake2db_logger

logger, extra_information = fake2db_logger()
d = extra_information

try:
    from faker import Factory
except ImportError:
    logger.error('faker package not found onto python packages, please run : \
    pip install -r requirements.txt  \
    on the root of the project', extra=d)
    sys.exit(1)


class BaseHandler(object):

    def __init__(self, locale=None, seed=None):
        '''Base class for DB handlers
        '''

        # Validating locale specified by user:
        # If specified locale not in faker.config.AVAILABLE_LOCALES
        # then faker.Factory will initialized with default locale ('en_US')
        if not locale:
            self.faker = Factory.create()
        else:
            try:
                self.faker = Factory.create(locale)
            except Exception:
                logger.warning("Specified locale is wrong or unsupported: '%s'; 'en_US' will be used!" % locale, extra=d)
                self.faker = Factory.create()

        # Setting the seed value for the random generator
        if seed is not None:
            self.faker.seed(seed)
