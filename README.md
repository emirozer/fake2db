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

###### non-PYPI included req

mysql connector is needed for mysql db generation:
> http://dev.mysql.com/downloads/connector/python/


##### Usage

It is as follows, at this point in time, fake2db accepts rows and db argument.
rows are pretty clear...
db argument takes 4 possible options : sqlite, mysql, postgresql, mongodb

> fake2db --rows 200 --db sqlite


##### Sample output - sqlite
![Screenshot](https://raw.github.com/emirozer/fake2db/master/docs/fake2db_example_sqlite.png)


#### TODO
    * Add more DB types
    * Add optional parameter 'name' to fake2db other than random name generation
    * Fix db patterns / add more
