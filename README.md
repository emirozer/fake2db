![Screenshot](https://raw.github.com/emirozer/fake2db/master/docs/fake2db_logo_screenshot.png)
===========
This is a WIP
------
***
##### About

Create test databases using most popular patterns(AFAIK).
Current support is sqlite, mysql, postgresql, mongodb.

##### Installation

The installation also retrieves 'requirements'.
Which are : *faker, fake-factory, pymongo, psycopg2*
> pip install fake2db

###### non-PYPI included req

mysql connector:
> http://dev.mysql.com/downloads/connector/python/


##### Usage

It is as follows, at this point in time, fake2db accepts rows and db argument.
rows is pretty clear...
db argument takes 4 possible options : sqlite, mysql, postgresql, mongodb

> fake2db --rows 200 --db sqlite
