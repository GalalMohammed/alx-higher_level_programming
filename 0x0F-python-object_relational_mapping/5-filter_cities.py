#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module takes name of state as an arg and lists all cities of that state.

Example:
    $ ./5-filter_cities.py root root hbtn_0e_4_usa Texas

"""


if __name__ == '__main__':
    import MySQLdb
    import sys
    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities, states\
            WHERE cities.state_id=states.id and states.name = %s\
            ORDER BY cities.id", (sys.argv[4], ))
    rows = cur.fetchall()
    for row in rows:
        if row != rows[-1]:
            print(row[0] + ', ', end='')
        else:
            print(row[0], end='')
    print()
    cur.close()
    db.close()
