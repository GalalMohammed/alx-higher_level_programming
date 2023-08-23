#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module defines State class.

Example:
    from model_state import Base, State

"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """class inherits from Base."""
    __tablename__ = 'state'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
