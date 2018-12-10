# http://www.postgresqltutorial.com/export-postgresql-table-to-csv-file/
"""

MySQL is one of the most widely used open source databasesself.

Here is where you can download and install it on your machine.
https://dev.mysql.com/downloads/mysql/

Here is some documentation in postgresql10 on how to create a dump file.
https://dev.mysql.com/doc/refman/8.0/en/mysqldump.html

To dump a database into a custom-format archive file:
https://dev.mysql.com/doc/refman/8.0/en/mysqldump-sql-format.html
$ mysqldump [options] > file_name

The easiest way to work with a MySQL dump file may be to actually restore it
and then from the restored file within a MySQL database, extract to a CSV file.

Here is some documentation on how to restore a dump file.
https://www.postgresql.org/docs/10/app-pgrestore.html

To reload the dump into a new database called newdb:
$ createdb -T template0 newdb
$ pg_restore -d newdb db.dump

Export to csv
http://www.mysqltutorial.org/mysql-export-table-to-csv/

"""
