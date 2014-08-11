import psycopg2
import sys


con = None

try:

    con = psycopg2.connect("dbname='Dzialki' user='postgres' host='localhost' password='postgres'")

    cur = con.cursor()

    cur.execute("CREATE TABLE cars2(id2 INT PRIMARY KEY, names VARCHAR(20), prices INT)")
    cur.execute("INSERT INTO cars VALUES(12,'Audi',52642)")
    cur.execute("INSERT INTO cars VALUES(22,'Mercedes',57127)")
    cur.execute("INSERT INTO cars VALUES(23,'Skoda',9000)")
    cur.execute("INSERT INTO cars VALUES(24,'Volvo',29000)")
    cur.execute("INSERT INTO cars VALUES(25,'Bentley',350000)")
    cur.execute("INSERT INTO cars VALUES(26,'Citroen',21000)")
    cur.execute("INSERT INTO cars VALUES(27,'Hummer',41400)")
    cur.execute("INSERT INTO cars VALUES(28,'Volkswagen',21600)")

    con.commit()


except psycopg2.DatabaseError, e:

    if con:
        con.rollback()

    print 'Error %s' % e
    sys.exit(1)


finally:

    if con:
        con.close()