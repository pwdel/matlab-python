# read postgres in Python

# PostgreSQL Python: Connect To PostgreSQL Database Server
# http://www.postgresqltutorial.com/postgresql-python/connect/

# https://wiki.postgresql.org/wiki/Psycopg2_Tutorial


import psycopg2
try:
conn = psycopg2.connect("host=localhost dbname=postgres user=postgres")
except:
    print "I am unable to connect to the postgres database"
