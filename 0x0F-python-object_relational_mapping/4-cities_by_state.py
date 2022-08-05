#!/usr/bin/python3
""" states module """
import MySQLdb
from sys import argv

if __name__ == '__main__':
    USER_IN = argv[1]
    PASSWD_IN = argv[2]
    DB_IN = argv[3]
    PORT = 3306

    # Init db & cur --
    db = MySQLdb.connect(host='localhost', port=PORT, user=USER_IN,
                         passwd=PASSWD_IN, db=DB_IN)
    cursor = db.cursor()

    # Query --
    query_statement = "SELECT cities.id, cities.name, states.name FROM cities\
                        JOIN states\
                        ON states.id = cities.state_id\
                        ORDER BY cities.id"
    cursor.execute(query_statement)
    cities_query = cursor.fetchall()
    for city in cities_query:
        print(city)

    # Cleanup --
    cursor.close()
    db.close()
