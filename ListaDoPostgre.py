import xlwt
import os
import psycopg2
import sys
import codecs

plik = codecs.open("krotki.txt","r","utf-8")
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
    #con.set_client_encoding('utf-8')
    print "Opened database successfully"
    cur = con.cursor()
    cur.execute("CREATE TABLE wycena(id INT  PRIMARY KEY     NOT NULL)")
    for n in lista:
        #print n
        #SQL ="ALTER TABLE wycena ADD %s VARCHAR()"
        #data = (n,)
        #cur.execute(SQL, data)
        n = " "+ n + " " + "VARCHAR(30)"
        cur.execute("ALTER TABLE wycena ADD" + n)
    con.commit()

except psycopg2.DatabaseError, e:

    if con:
        con.rollback()

    print 'Error %s' % e
    sys.exit(1)


finally:

    if con:
        con.close()

#cur.execute('INSERT INTO %s (day, elapsed_time, net_time, length, average_speed, geometry) VALUES (%s, %s, %s, %s, %s, %s)', (escaped_name, day, time_length, time_length_net, length_km, avg_speed, myLine_ppy))