#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module lists all cities from the database hbtn_0e_4_usa.

Example:
    ./4-cities_by_state.py root root hbtn_0e_4_usa

"""


if __name__ == '__main__':
    import MySQLdb
    import sys
    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name\
            FROM cities, states WHERE cities.state_id=states.id\
            ORDER BY ctates.id")
    rows = cur.fetchall()
    for row in rows:
        if row[1] == sys.argv[4]:
            print(row)
    cur.close()
    db.close()
