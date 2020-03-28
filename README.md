---
page_type: sample
description: "This is a minimal sample app that demonstrates how to run a Python Flask application on Azure App Service on Linux."
languages:
- python
products:
- azure
- azure-app-service
---

# Python Flask sample for Azure App Service (Linux)

This is a minimal sample app that demonstrates how to run a Python Flask application on Azure App Service on Linux.

For more information, please see the [Python on App Service quickstart](https://docs.microsoft.com/azure/app-service/containers/quickstart-python).

## Contributing

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.


---
From the running sample app, let's continue with Flask Mega Tutorial by Miguel Grinberg
---

# Flask Mega Tutorial by Miguel Grinberg
[Miguel Grinberg](https://blog.miguelgrinberg.com/author/Miguel%20Grinberg)
[The Flask Mega Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)




## Connect to mysqlremote.com
From Chapter 5 (User Logins), when deploying to Microsoft Azure App Service (Free Tier) I ran into error when registering new user. So I switch from sqlite to MySQL database, using the free service [https://remotemysql.com/](https://remotemysql.com/).
- Register free account at [https://remotemysql.com/](https://remotemysql.com/)
- Sign in and create a new database. Take note of newly created database (databasename, username, password, port) to update DATABASE_URL in .env file (on local dev) and Settings > Configuration (on Azure Web App)

```
DATABASE_URL=mysql+pymysql://username:password@remotemysql.com:3306/databasename?charset=utf8m4
```

```
(env) PS F:\Projects\github\iflask> flask db migrate
f:\projects\github\iflask\env\lib\site-packages\pymysql\cursors.py:170: Warning: (3719, "'utf8' is currently an alias for the character set UTF8MB3, but will be an alias
for UTF8MB4 in a future release. Please consider using UTF8MB4 in order to be unambiguous.")
  result = self._query(query)
INFO  [alembic.runtime.migration] Context impl MySQLImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
ERROR [root] Error: Target database is not up to date.
(env) PS F:\Projects\github\iflask>
``` 
```
(env) PS F:\Projects\github\iflask> flask db upgrade
f:\projects\github\iflask\env\lib\site-packages\pymysql\cursors.py:170: Warning: (371
9, "'utf8' is currently an alias for the character set UTF8MB3, but will be an alias
for UTF8MB4 in a future release. Please consider using UTF8MB4 in order to be unambig
uous.")
  result = self._query(query)
INFO  [alembic.runtime.migration] Context impl MySQLImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade  -> 5413c6b66b4b, users table
INFO  [alembic.runtime.migration] Running upgrade 5413c6b66b4b -> 2b5c002359fd, posts
 table
(env) PS F:\Projects\github\iflask>
```