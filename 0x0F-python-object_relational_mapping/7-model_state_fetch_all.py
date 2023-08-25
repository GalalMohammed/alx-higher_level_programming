#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module lists all State objects from the database hbtn_0e_6_usa

Example:
    $ ./7-model_state_fetch_all.py root root hbtn_0e_6_usa

"""


if __name__ == '__main__':
    from model_state import Base, State
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    import urllib.parse
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
                           sys.argv[1], urllib.parse.quote_plus(sys.argv[2]),
                           sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    for row in session.query(State).order_by(State.id):
        print(str(row.id) + ': ' + row.name)
    session.close()
    engine.dispose()
