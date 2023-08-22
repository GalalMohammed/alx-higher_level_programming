#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.

Example:
    $ ./2-my_filter_states.py root root hbtn_0e_0_usa 'Arizona'

"""


if __name__ == '__main__':
    import MySQLdb
    import sys
    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name='{}' ORDER BY id".format(
                sys.argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
