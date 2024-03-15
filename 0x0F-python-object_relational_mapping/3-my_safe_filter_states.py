#!/usr/bin/python3

"""This script takes in an argument and displays all values in the states table of hbtn_0e_0_usa"""

import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)

    _cursor = db.cursor()
    match = sys.argv[4]
    _cursor.execute("SELECT * FROM states WHERE name LIKE %s", (match, ))

    r = _cursor.fetchall()
    for row in r:
        print(row)

    _cursor.close()
    db.close()
