![Screenshot](https://raw.github.com/emirozer/fake2db/master/docs/fake2db_logo_screenshot.png)
===========
This is a WIP
------
***


##### About

Generate fake but valid data filled databases for test purposes using most popular patterns(AFAIK).
Current support is *sqlite, mysql, postgresql, mongodb*. <br>

##### Installation

The installation through pypi also retrieves 'requirements'.
Which are : *fake-factory, pymongo, psycopg2*
> pip install fake2db
<br>

###### non-PYPI included REQUIREMENT

For psycopg2 to install you need *pg_config* in your system.

On Mac, the solution is to install *postgresql*:
> brew install postgresql

On CentOS, the solution is to install *postgresql-devel*:
> sudo yum install postgresql-devel
<br>


###### Optional - if you are going to use mysql

mysql connector is needed for mysql db generation:
> http://dev.mysql.com/downloads/connector/python/
<br>

##### Usage

It is as follows, at this point in time, fake2db accepts rows and db argument.

*--rows* argument is pretty clear...

*--db* argument takes 4 possible options : sqlite, mysql, postgresql, mongodb

*--name* argument is OPTIONAL. When it is absent fake2db will name db's randomly.

*--host* argument is OPTIONAL. Hostname to use for database connection. Not used for sqlite.

*--port* argument is OPTIONAL. Port to use for database connection. Not used for sqlite.

*--password* argument is OPTIONAL. Password for root. Only supported for mysql.

> fake2db --rows 200 --db sqlite
<br>
> fake2db --rows 1500 --db postgresql --name test_database_postgre

In addition to the databases supported in the db argument, you can also run fake2db with FoundationDB SQL Layer. Once SQL Layer is installed, simply use the postgresql generator and specify the SQL Layer port. For example:

> fake2db --rows --db postgresql --port 15432

<br>
##### Sample output - sqlite
![Screenshot](https://raw.github.com/emirozer/fake2db/master/docs/fake2db_example_sqlite.png)


<br>
#### TODO
    * Add more DB types
    * Fix db patterns / add more
