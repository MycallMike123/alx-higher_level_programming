#!/usr/bin/python3

"""This script lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

def list_states(username, password, database):
    """Connects to the MySQL database and lists all states"""

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                        passwd=password, db=database)

    # Create a cursor object using cursor() method
    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    states = cursor.fetchall()

    for state in states:
        print(state)


    cursor.close()
    db.close()

    if __name__ == "__main__":
        if len(sys.argv) != 4:
            print("Usage: ./list_states.py <username> <password> <database>")
            sys.exit(1)

        username, password, database = sys.argv[1:]
        list_states(username, password, database)
