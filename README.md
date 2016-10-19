![Screenshot](https://raw.github.com/emirozer/fake2db/master/docs/fake2db_logo_screenshot.png)
===========
***

[![Latest Version](https://img.shields.io/pypi/v/fake2db.svg)](https://img.shields.io/pypi/v/fake2db.svg)
[![Downloads](https://img.shields.io/pypi/dm/fake2db.svg)](https://img.shields.io/pypi/dm/fake2db.svg)
[![Status](https://img.shields.io/pypi/status/fake2db.svg)](https://img.shields.io/pypi/status/fake2db.svg)



##### About

Generate fake but valid data filled databases for test purposes using most popular patterns(AFAIK).
Current support is *sqlite, mysql, postgresql, mongodb, redis, couchdb*. <br>

##### Installation

The installation through pypi retrieves 'fake-factory' as a main dependency.
> pip install fake2db
<br>

###### Optional requirements

###### PostgreSQL

    pip install psycopg2

For psycopg2 to install you need *pg_config* in your system.

On Mac, the solution is to install *postgresql*:
> brew install postgresql

On CentOS, the solution is to install *postgresql-devel*:
> sudo yum install postgresql-devel
<br>

###### Mongodb

    pip install pymongo

###### Redis

    pip install redis

###### MySQL

mysql connector is needed for mysql db generation:
> http://dev.mysql.com/downloads/connector/python/
<br>

##### CouchDB

	pip install couchdb

##### Usage


*--rows* argument is pretty clear :) integer

*--db* argument takes 6 possible options : sqlite, mysql, postgresql, mongodb, redis, couchdb

*--name* argument is OPTIONAL. When it is absent fake2db will name db's randomly.

*--host* argument is OPTIONAL. Hostname to use for database connection. Not used for sqlite.

*--port* argument is OPTIONAL. Port to use for database connection. Not used for sqlite.

*--username* argument is OPTIONAL. Username for the database user.

*--password* argument is OPTIONAL. Password for database user. Only supported for mysql & postgresql.

*--locale* argument is OPTIONAL. The localization of data to be generated ('en_US' as default).

*--seed* argument is OPTIONAL. Integer for seeding random generator to produce the same data set between runs. Note: uuid4 values still generated randomly.


> fake2db --rows 200 --db sqlite
<br>
> fake2db --rows 1500 --db postgresql --name test_database_postgre
<br>
> fake2db --db postgresql --rows 2500 --host container.local --password password --user docker
<br>
> fake2db --rows 200 --db sqlite --locale cs_CZ --seed 1337
<br>

In addition to the databases supported in the db argument, you can also run fake2db with FoundationDB SQL Layer. Once SQL Layer is installed, simply use the postgresql generator and specify the SQL Layer port. For example:

> fake2db --rows --db postgresql --port 15432


##### Custom Database Generation

If you want to create a custom db/table, you have to provide **--custom** parameter followed by the column item you want. At the point in time, i mapped all the possible column items you can use here:

<https://github.com/emirozer/fake2db/blob/master/fake2db/custom.py>

Feed any keys you want to the custom flag:

> fake2db.py --rows 250 --db mysql --username mysql --password somepassword --custom name date country
<br>
>fake2db.py --rows 1500 --db mysql --password randompassword --custom currency_code credit_card_full credit_card_provider
<br>
>fake2db.py --rows 20 --db mongodb --custom name date country


<br>
##### Sample output - sqlite
![Screenshot](https://raw.github.com/emirozer/fake2db/master/docs/fake2db_example_sqlite.png)
<br>
![Screenshot](https://raw.github.com/emirozer/fake2db/master/docs/mysql_fake2db.png)
<br>
![Screenshot](https://raw.github.com/emirozer/fake2db/master/docs/pg_fake2db.png)

<br>
