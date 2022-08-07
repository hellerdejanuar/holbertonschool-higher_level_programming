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

    db = MySQLdb.connect(host='localhost', port=PORT, user=USER_IN,
                         passwd=PASSWD_IN, db=DB_IN)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states \
                   WHERE name = '{}' \
                   ORDER BY states.id ASC".format(STATE_IN))
    states_query = cursor.fetchall()
    if states_query:
        for state in states_query:
            print(state)
    else:
        print()

    # Close all cursors
    cursor.close()
    # Close all databases
    db.close()
