#!/usr/bin/python3
""" states module """
import MySQLdb
from sys import argv

if __name__ == '__main__':
    USER_IN = argv[1]
    PASSWD_IN = argv[2]
    DB_IN = argv[3]
    STATE_IN = ' '.join(argv[4:])
    PORT = 3306

    # Init db & cur --
    db = MySQLdb.connect(host='localhost', port=PORT, user=USER_IN,
                         passwd=PASSWD_IN, db=DB_IN)
    cursor = db.cursor()

    # Query --
    query_statement = "SELECT cities.name\
                        FROM cities, states\
                        WHERE cities.state_id = states.id\
                        AND states.name = %(state)s\
                        ORDER BY cities.id"
    cursor.execute(query_statement, {'state': STATE_IN})
    cities_query = cursor.fetchall()

    # Print results --
    if cities_query:
        for i, city in enumerate(cities_query):
            print(city[0], end='')
            if i != len(cities_query) - 1:
                print(', ', end='')
            else:
                print()


    # Cleanup --
    cursor.close()
    db.close()
