#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module lists all states with a name starting with N

Example:
    $ ./1-filter_states.py root root hbtn_0e_0_usa

"""


if __name__ == '__main__':
    import MySQLdb
    import sys
    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    numrows = cur.execute("SELECT * FROM states ORDER BY id 'N%'")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
