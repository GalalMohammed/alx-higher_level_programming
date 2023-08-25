#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module prints the first State object from the database hbtn_0e_6_usa

Example:
    $ ./8-model_state_fetch_first.py root root hbtn_0e_6_usa

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
    row = session.query(State).order_by(State.id).first()
    if row:
        print(str(row.id) + ': ' + row.name)
    else:
        print("Nothing")
    session.close()
    engine.dispose()
