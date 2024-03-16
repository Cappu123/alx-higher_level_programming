#!/usr/bin/python3
""" takes in an argument
    displays all values in the states
    table of hbtn_0e_0_usa
    where name matches the argument.
    But this time, write one that is
    safe from MySQL injections!
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c =db.cursor()
    match = sys.argv[4]
    query1 = c.execute("""SELECT * FROM states
                        WHERE name LIKE %s""", (match, ))
                        
    rows = c.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()

