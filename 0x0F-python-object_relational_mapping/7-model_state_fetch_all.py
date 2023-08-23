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
    engine = create_engine('mysql+mysqldb://{}:{}'
                           '@localhost/{}'.format(sys.argv[1], sys.argv[2],
                                                  sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    query = session.query(State).order_by(State.id)
    for _row in (query.all()):
        print(_row.id + ': ' + _row.name)
    session.close()
    engine.dispose()
