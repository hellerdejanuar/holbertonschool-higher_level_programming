#!/usr/bin/python3
""" states module """
import MySQLdb
from sys import argv

if __name__ == '__main__':
    USER_IN = argv[1]
    PASSWD_IN = argv[2]
    DB_IN = argv[3]
    PORT = 3306

    db = MySQLdb.connect(host='localhost', port=PORT, user=USER_IN,
                         passwd=PASSWD_IN, db=DB_IN)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC")
    states_query = cursor.fetchall()
    for state in states_query:
        print(state)
