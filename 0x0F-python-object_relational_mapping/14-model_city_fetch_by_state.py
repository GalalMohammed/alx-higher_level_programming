#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module prints all City objects from the database hbtn_0e_14_usa

Example:
    $ ./14-model_city_fetch_by_state.py root root hbtn_0e_14_usa

"""


if __name__ == '__main__':
    from model_city import Base, City
    from model_state import State
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    import urllib.parse
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
                           sys.argv[1], urllib.parse.quote_plus(sys.argv[2]),
                           sys.argv[3]))
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    query = session.query(City).order_by(City.id)
    for _row in query.all():
        state_name = session.query(State).filter(
                State.id == _row.state_id).first().name
        print(state_name + ": (" + str(_row.id) + ") " + _row.name)
    session.close()
    engine.dispose()
