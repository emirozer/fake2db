import argparse
import subprocess
import time

from helpers import fake2db_logger

logger, extra_information = fake2db_logger()


class InstantiateDBHandlerException(Exception):
    '''An Exception at the instantiation of the handler '''


def _postgresql_process_checkpoint():
    '''this helper method checks if
    postgresql server is available in the sys
    if not fires up one
    '''
    try:
        subprocess.check_output("pgrep postgres", shell=True)
    except:
        logger.warning('Your postgresql server is offline, fake2db will try to launch it now!', extra=extra_information)
        # close_fds = True argument is the flag that is responsible
        # for Popen to launch the process completely independent
        subprocess.Popen("postgres -D /usr/local/pgsql/data", close_fds=True, shell=True)
        time.sleep(3)


def _mysqld_process_checkpoint():
    '''this helper method checks if 
    mysql server is available in the sys
    if not fires up one
    '''
    try:
        subprocess.check_output("pgrep mysqld", shell=True)
    except:
        logger.warning('Your mysql server is offline, fake2db will try to launch it now!', extra=extra_information)
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
    except:
        logger.warning('Your mongodb server is offline, fake2db will try to launch it now!', extra=extra_information)
        # close_fds = True argument is the flag that is responsible
        # for Popen to launch the process completely independent
        subprocess.Popen("mongod", close_fds=True, shell=True)
        time.sleep(3)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--rows", help="Amount of rows desired per table")
    parser.add_argument("--db",
                        help="Db type for creation: sqlite, mysql, postgresql, mongodb, couchdb, to be expanded")
    parser.add_argument("--name", help="OPTIONAL : Give a name to the db to be generated. ")
    parser.add_argument("--host", help="OPTIONAL : Hostname of db. ")
    parser.add_argument("--port", help="OPTIONAL : Port of db. ")
    parser.add_argument("--password", help="OPTIONAL : Password for root. ")

    args = parser.parse_args()

    if not args.rows or not args.db:
        logger.error('Please use with --help argument for usage information!', extra=extra_information)

    else:
        logger.info('arguments found(rows and db), starting faking!!', extra=extra_information)
        logger.warning('Rows argument : %s', args.rows, extra=extra_information)
        logger.info('DB argument : %s', args.db, extra=extra_information)

        if args.db == 'sqlite':
            try:
                from sqlite_handler import Fake2dbSqliteHandler
                fake_sqlite_handler = Fake2dbSqliteHandler()
            except:
                raise InstantiateDBHandlerException
            if args.name:
                fake_sqlite_handler.fake2db_sqlite_initiator(int(args.rows), str(args.name))
            else:
                fake_sqlite_handler.fake2db_sqlite_initiator(int(args.rows))

        elif args.db == 'mysql':
            try:
                from mysql_handler import Fake2dbMySqlHandler
                fake_mysql_handler = Fake2dbMySqlHandler()
            except:
                raise InstantiateDBHandlerException
            _mysqld_process_checkpoint()
            host = args.host or "127.0.0.1"
            port = args.port or "3306"
            if args.name:
                fake_mysql_handler.fake2db_mysql_initiator(host, port, args.password, int(args.rows), str(args.name))
            else:
                fake_mysql_handler.fake2db_mysql_initiator(host, port, args.password, int(args.rows))

        elif args.db == 'postgresql':
            try:
                from postgresql_handler import Fake2dbPostgresqlHandler
                fake_postgresql_handler = Fake2dbPostgresqlHandler()
            except:
                raise InstantiateDBHandlerException
            _postgresql_process_checkpoint()
            host = args.host or "localhost"
            port = args.port or "5432"
            if args.name:
                fake_postgresql_handler.fake2db_postgresql_initiator(host, port, int(args.rows), str(args.name))
            else:
                fake_postgresql_handler.fake2db_postgresql_initiator(host, port, int(args.rows))

        elif args.db == 'mongodb':
            try:
                from mongodb_handler import Fake2dbMongodbHandler
                fake_mongodb_handler = Fake2dbMongodbHandler()
            except:
                raise InstantiateDBHandlerException
            _mongodb_process_checkpoint()
            host = args.host or "localhost"
            port = args.port or 27017
            if args.name:
                fake_mongodb_handler.fake2db_mongodb_initiator(host, int(port), int(args.rows), str(args.name))
            else:
                fake_mongodb_handler.fake2db_mongodb_initiator(host, int(port), int(args.rows))

        else:
            logger.error('Wrong arg for db parameter. Valid ones : sqlite - mysql - postgresql - mongodb',
                         extra=extra_information)


if __name__ == '__main__':
    main()
