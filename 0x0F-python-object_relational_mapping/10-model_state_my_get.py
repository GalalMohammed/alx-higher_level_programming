#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module prints State object with name passed as arg from hbtn_0e_6_usa

Example:
    $ ./10-model_state_my_get.py root root hbtn_0e_6_usa Texas

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
    row = session.query(State).filter(State.name == sys.argv[4]).first()
    if row:
        print(row.id)
    else:
        print("Not found")
    session.close()
    engine.dispose()
