import xlwt
import os
import psycopg2
import sys

plik = open('krotki.txt','r')
lista = []
calosc = ""
try:
        for i in plik:
            i = i.strip('\n')
            lista.append(i)
lista = list(set(lista))
finally:
	plik.close()

try:
    con = psycopg2.connect("dbname='Dzialki' user='postgres' host='localhost' password='postgres'")
    print "Opened database successfully"
    cur = con.cursor()
    cur.execute("CREATE TABLE wycena(ID INT  PRIMARY KEY     NOT NULL)")
    for krot in lista:
        cur.execute("ALTER TABLE wycena ADD lista[n] VARCHAR()")
    con.commit()


except psycopg2.DatabaseError, e:

    if con:
        con.rollback()

    print 'Error %s' % e
    sys.exit(1)


finally:

    if con:
        con.close()

