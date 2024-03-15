#!/usr/bin/python3

"""A module that lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)

    _cursor = db.cursor()
    _cursor.execute("""SELECT cities.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s""", (sys.argv[4],))

    r = _cursor.fetchall()
    temp = list(row[0] for row in r)
    print(*temp, sep=", ")

    _cursor.close()
    db.close()
