#!/usr/bin/python3
""" states module """
import MySQLdb
from sys import argv

if __name__ == '__main__':
    USER_IN = argv[1]
    PASSWD_IN = argv[2]
    DB_IN = argv[3]
    STATE_IN = argv[4]
    PORT = 3306

    # Init db & cur --
    db = MySQLdb.connect(host='localhost', port=PORT, user=USER_IN,
                         passwd=PASSWD_IN, db=DB_IN)
    cursor = db.cursor()

    # Query --
    query_statement = "SELECT cities.name\
                        FROM cities, states\
                        WHERE cities.state_id = states.id AND states.name = %(state)s\
                        ORDER BY cities.id"
    # ToDo: request state.id corresponding
    # to STATE_IN
    cursor.execute(query_statement, {'state' : STATE_IN})
    cities_query = cursor.fetchall()
    for i in range(len(cities_query) - 1):
        print(cities_query[i][0], end=', ')
    print(cities_query[i + 1][0])

    # Cleanup --
    cursor.close()
    db.close()
