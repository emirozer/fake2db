import argparse
import getpass
import subprocess
import time
import sys
from custom import faker_options_container
from helpers import fake2db_logger

logger, extra_information = fake2db_logger()


class InstantiateDBHandlerException(Exception):
    '''An Exception at the instantiation of the handler '''


class MissingDependencyException(Exception):
    '''An Exception to be thrown if the dependencies are missing'''


def _mysqld_process_checkpoint():
    '''this helper method checks if
    mysql server is available in the sys
    if not fires up one
    '''
    try:
        subprocess.check_output("pgrep mysqld", shell=True)
    except Exception:
        logger.warning(
            'Your mysql server is offline, fake2db will try to launch it now!',
            extra=extra_information)
        # close_fds = True argument is the flag that is responsible
        # for Popen to launch the process completely independent
        subprocess.Popen("mysqld", close_fds=True, shell=True)
        time.sleep(3)


def _mongodb_process_checkpoint():
    '''this helper method checks if
    mongodb server is available in the sys
    if not fires up one
    '''
    try:
        subprocess.check_output("pgrep mongod", shell=True)
    except Exception:
        logger.warning(
            'Your mongodb server is offline, fake2db will try to launch it now!',
            extra=extra_information)
        # close_fds = True argument is the flag that is responsible
        # for Popen to launch the process completely independent
        subprocess.Popen("mongod", close_fds=True, shell=True)
        time.sleep(3)


def _couchdb_process_checkpoint():
    '''this helper method checks if
    couchdb server is available in the sys
    if not fires up one
    '''
    try:
        subprocess.check_output("curl localhost:5984", shell=True)
    except Exception:
        logger.warning('Your couchdb server is offline',
                       extra=extra_information)
        # close_fds = True argument is the flag that is responsible
        # for Popen to launch the process completely independent
        subprocess.Popen("couchdb", close_fds=True, shell=True)
        time.sleep(3)


def _redis_process_checkpoint(host, port):
    '''this helper method checks if
    redis server is available in the sys
    if not fires up one
    '''
    try:
        subprocess.check_output("pgrep redis", shell=True)
    except Exception:
        logger.warning(
            'Your redis server is offline, fake2db will try to launch it now!',
            extra=extra_information)
        # close_fds = True argument is the flag that is responsible
        # for Popen to launch the process completely independent
        subprocess.Popen("redis-server --bind %s --port %s" % (host, port),
                         close_fds=True,
                         shell=True)
        time.sleep(3)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--rows", help="Amount of rows desired per table",
                        type=int)
    parser.add_argument(
        "--db",
        help=
        "Db type for creation: sqlite, mysql, postgresql, mongodb, redis, couchdb, to be expanded")
    parser.add_argument("--name", help="The name to the db to be generated")
    parser.add_argument("--host", help="Hostname of db")
    parser.add_argument("--port", help="Port of db", type=int)
    parser.add_argument("--username", help="Username")
    parser.add_argument("--password", help="Password")
    parser.add_argument("--custom", nargs='+', help="Custom schema for db generation, supports functions that fake-factory provides, see fake2db github repository for options https://github.com/emirozer/fake2db")
    parser.add_argument("--locale", help="The locale of the data to be generated: {bg_BG,cs_CZ,...,zh_CN,zh_TW}. 'en_US' as default")
    parser.add_argument("--seed", help="Seed value for the random generator", type=int)


    args = parser.parse_args()

    if not args.rows or not args.db:
        logger.error('Please use with --help argument for usage information!',
                     extra=extra_information)

    else:
        logger.info('arguments found(rows and db), starting faking!!',
                    extra=extra_information)
        logger.warning('Rows argument : %s', args.rows,
                       extra=extra_information)
        logger.info('DB argument : %s', args.db, extra=extra_information)

        if args.custom:
            custom_d = faker_options_container()
            for c in args.custom:
                if custom_d.get(c):
                    logger.info("fake2db found valid custom key provided: %s" % c, extra=extra_information)
                else:
                    logger.error("fake2db does not support the custom key you provided: %s" % c, extra=extra_information )
                    sys.exit(1)
                
        if args.db == 'sqlite':
            try:
                from sqlite_handler import Fake2dbSqliteHandler
                fake_sqlite_handler = Fake2dbSqliteHandler(args.locale, args.seed)
            except Exception:
                raise InstantiateDBHandlerException
            if args.name and args.custom:
                fake_sqlite_handler.fake2db_sqlite_initiator(args.rows,
                                                             args.name, args.custom)
            elif args.custom:
                fake_sqlite_handler.fake2db_sqlite_initiator(args.rows, None, args.custom)
            else:
                fake_sqlite_handler.fake2db_sqlite_initiator(args.rows)

        elif args.db == 'mysql':
            try:
                from mysql_handler import Fake2dbMySqlHandler
                fake_mysql_handler = Fake2dbMySqlHandler(args.locale, args.seed)
            except Exception:
                raise InstantiateDBHandlerException
            _mysqld_process_checkpoint()
            host = args.host or "127.0.0.1"
            port = args.port or 3306
            username = args.username or getpass.getuser()
            if args.name and args.custom:
                fake_mysql_handler.fake2db_mysql_initiator(
                    host, port, args.password, username, args.rows, args.name, args.custom)
            elif args.custom:
                fake_mysql_handler.fake2db_mysql_initiator(
                    host, port, args.password, username, args.rows, None, args.custom)
            else:
                fake_mysql_handler.fake2db_mysql_initiator(
                    host, port, args.password, username, args.rows, None, None)

        elif args.db == 'postgresql':
            try:
                import psycopg2
            except ImportError:
                raise MissingDependencyException(
                    'psycopg2 package not found on the python packages, please run: pip install psycopg2')

            try:
                from postgresql_handler import Fake2dbPostgresqlHandler
                fake_postgresql_handler = Fake2dbPostgresqlHandler(args.locale, args.seed)
            except Exception:
                raise InstantiateDBHandlerException
            host = args.host or "localhost"
            port = args.port or 5432
            username = args.username or getpass.getuser()
            custom = args.custom or None
            fake_postgresql_handler.fake2db_initiator(host=host, port=port,
                                                      username=username,
                                                      password=args.password,
                                                      number_of_rows=args.rows,
                                                      name=args.name,
                                                      custom=custom)

        elif args.db == 'mongodb':
            try:
                import pymongo
            except ImportError:
                raise MissingDependencyException(
                    'pymongo package not found on the python packages, please run: pip install pymongo')

            try:
                from mongodb_handler import Fake2dbMongodbHandler
                fake_mongodb_handler = Fake2dbMongodbHandler(args.locale, args.seed)
            except Exception:
                raise InstantiateDBHandlerException
            _mongodb_process_checkpoint()
            host = args.host or "localhost"
            port = args.port or 27017

            if args.name and args.custom:
                fake_mongodb_handler.fake2db_mongodb_initiator(
                    host, port, args.rows, args.name, args.custom)
            elif args.custom:
                fake_mongodb_handler.fake2db_mongodb_initiator(
                    host, port, args.rows, None, args.custom)
            else:
                fake_mongodb_handler.fake2db_mongodb_initiator(host, port,
                                                               args.rows)

        elif args.db == 'couchdb':
            try:
                import couchdb
            except ImportError:
                raise MissingDependencyException(
                    'couchdb package not found on the python packages, please run: pip install couchdb')

            try:
                from couchdb_handler import Fake2dbCouchdbHandler
                fake_couchdb_handler = Fake2dbCouchdbHandler(args.locale, args.seed)
            except Exception:
                raise InstantiateDBHandlerException
            _couchdb_process_checkpoint()
            
            if args.name and args.custom:
                fake_couchdb_handler.fake2db_couchdb_initiator(
                    args.rows, args.name, args.custom)
            elif args.custom:
                fake_couchdb_handler.fake2db_couchdb_initiator(
                    args.rows, None, args.custom)
            else:
                fake_couchdb_handler.fake2db_couchdb_initiator(args.rows)
                
        elif args.db == 'redis':
            if args.name and (not args.name.isdigit() or int(args.name) < 0):
                logger.error('redis db name must be a non-negative integer',
                             extra=extra_information)
                return

            try:
                import redis
            except ImportError:
                raise MissingDependencyException(
                    'redis package not found on the python packages, please run: pip install redis')

            try:
                from redis_handler import Fake2dbRedisHandler
                fake_redis_handler = Fake2dbRedisHandler(args.locale, args.seed)
            except Exception:
                raise InstantiateDBHandlerException
            host = args.host or "localhost"
            port = args.port or 6379
            _redis_process_checkpoint(host, port)
            if args.name and args.custom:
                fake_redis_handler.fake2db_redis_initiator(
                    host, port, args.rows, args.name, args.custom)
            elif args.custom:
                fake_redis_handler.fake2db_redis_initiator(
                    host, port, args.rows, None, args.custom)
            else:
                fake_redis_handler.fake2db_redis_initiator(host, port,
                                                           args.rows)

        else:
            logger.error(
                'Wrong arg for db parameter. Valid ones : sqlite - mysql - postgresql - mongodb - redis',
                extra=extra_information)


if __name__ == '__main__':
    main()
