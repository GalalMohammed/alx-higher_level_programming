#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module deletes State objects with a name containing letter a
from hbtn_0e_6_usa

Example:
    $ ./13-model_state_delete_a.py root root hbtn_0e_6_usa

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
    query = session.query(State).filter(State.name.like('%a%'))
    query.delete()
    session.commit()
    session.close()
    engine.dispose()
