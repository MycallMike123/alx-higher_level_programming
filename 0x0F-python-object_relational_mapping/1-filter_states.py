#!/usr/bin/python3
"""This script lists all states with a name starting with 'N'
(uppercase) from the database hbtn_0e_0_usa"""

import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    _cursor = db.cursor()
    _cursor.execute("""SELECT * FROM states WHERE name
                LIKE BINARY 'N%' ORDER BY states.id""")

    r = _cursor.fetchall()
    for row in r:
        print(row)

    _cursor.close()
    db.close()
