from helpers import fake2db_logger, str_generator


logger, extra_information = fake2db_logger()
d = extra_information

try:
    import pymongo
except ImportError:
    logger.error('pymongo package not found onto python packages, please run : \
    pip install -r requirements.txt  \
    on the root of the project')
    sys.exit(0)

try:
    from faker import Factory
except ImportError:
    logger.error('faker package not found onto python packages, please run : \
    pip install -r requirements.txt  \
    on the root of the project')
