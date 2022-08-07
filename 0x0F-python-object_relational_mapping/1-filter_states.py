#!/usr/bin/python3
""" states module """

if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    USER_IN = argv[1]
    PASSWD_IN = argv[2]
    DB_IN = argv[3]
    PORT = 3306

    db = MySQLdb.connect(host='localhost', port=PORT, user=USER_IN,
                         passwd=PASSWD_IN, db=DB_IN)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states \
                   WHERE name LIKE 'N%' \
                   ORDER BY states.id")
    states_query = cursor.fetchall()
    for state in states_query:
        if state[1][0] == 'N':
            print(state)

    # Close all cursors
    cursor.close()
    # Close all databases
    db.close()
