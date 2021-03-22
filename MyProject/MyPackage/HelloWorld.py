'''
Created on Mar 20, 2021

@author: tiffany
'''
import django

print(django.get_version())


from sqlalchemy import create_engine

# Lanuch new PostgreSQL server
import testing.postgresql

with testing.postgresql.Postgresql() as postgresql:
    # connect to PostgreSQL
    engine = create_engine(postgresql.url())

    # if you use postgresql or other drivers:
    import psycopg2
    
#def setUp(self):
    postgresql = testing.postgresql.Postgresql(port=7654)
    # Get the url to connect to with psycopg2 or equivalent
    conn = psycopg2.connect(**postgresql.dsn())
    cursor = conn.cursor()
    #cursor.execute("ALTER ROLE postgres WITH PASSWORD 'postgres'")
    cursor.execute("CREATE TABLE hello(id int, value varchar(256))")
    cursor.execute("INSERT INTO hello values(1, 'hello'), (2, 'ciao')")
    conn.commit()
    
    cursor.execute("select * from pg_catalog.pg_user")
    
    print(cursor.fetchone())
    cursor.close()
    conn.commit()
    conn.close()
    #

# PostgreSQL server is terminated here

# Standard import
from pydoc import locate

myMetal = "Gold"

MyCoin = locate("MyPackage." + myMetal + ".MyCoin")

myMetal = "Silver"

MyCoin = locate("MyPackage." + myMetal + ".MyCoin")
postgresql.stop()

print("finished")
