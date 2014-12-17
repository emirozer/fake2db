![Screenshot](https://raw.github.com/emirozer/fake2db/master/docs/fake2db_logo_screenshot.png)
===========
This is a WIP
------
***


##### About

Generate fake but valid data filled databases for test purposes using most popular patterns(AFAIK).
Current support is *sqlite, mysql, postgresql, mongodb*.



##### Installation

The installation through pypi also retrieves 'requirements'.
Which are : *fake-factory, pymongo, psycopg2*
> pip install fake2db



###### non-PYPI included REQUIREMENT

For psycopg2 to install you need *pg_config* in your system.

On Mac, the solution is to install *postgresql*:
> brew install postgresql

On CentOS, the solution is to install *postgresql-devel*:
> sudo yum install postgresql-devel



###### Optional - if you are going to use mysql

mysql connector is needed for mysql db generation:
> http://dev.mysql.com/downloads/connector/python/




##### Usage

It is as follows, at this point in time, fake2db accepts rows and db argument.
*--rows* argument is pretty clear...
*--db* argument takes 4 possible options : sqlite, mysql, postgresql, mongodb
*--name* argument is OPTIONAL. When it is absent fake2db will name db's randomly.

> fake2db --rows 200 --db sqlite
> fake2db --rows 1500 --db postgresql --name test_database_postgre



##### Sample output - sqlite
![Screenshot](https://raw.github.com/emirozer/fake2db/master/docs/fake2db_example_sqlite.png)




#### TODO
    * Add more DB types
    * Fix db patterns / add more
