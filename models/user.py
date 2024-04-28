#!/usr/bin/python3
""" user Model """
from . import base_model
class User(base_model.BaseModel):
    """class include email and password and other fields"""

    email = ''
    password = ''
    first_name = ''
    last_name = ''
