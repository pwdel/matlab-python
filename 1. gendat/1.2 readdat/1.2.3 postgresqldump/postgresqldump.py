# http://www.postgresqltutorial.com/export-postgresql-table-to-csv-file/
"""

Postgresql is one of the simplest, most common database forms out thereself.
Backups for postgresql files are known as "dumps" which are essentially raw text files.

Here is some documentation in postgresql10 on how to create a dump file.
https://www.postgresql.org/docs/10/app-pgdump.html

To dump a database into a custom-format archive file:
$ pg_dump -Fc mydb > db.dump

The easiest way to work with a PostGresql dump file may be to actually restore it
and then from the restored file within a Postgres database, extract to a CSV file.

Here is some documentation on how to restore a dump file.
https://www.postgresql.org/docs/10/app-pgrestore.html

To reload the dump into a new database called newdb:
$ createdb -T template0 newdb
$ pg_restore -d newdb db.dump


"""
