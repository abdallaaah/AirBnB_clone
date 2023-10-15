#!/usr/bin/python3
""" this is the Base Model for the Airbnb projct """
import uuid
from datetime import datetime as date
import json


class BaseModel():
    """ thee base Model for id and create&update time"""
    def __init__(self, *args, **kwargs):
        """ the init function to intalize """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ('created_at', 'updated_at'):
                        value = date.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = date.now()
            self.updated_at = date.now()

    def __str__(self):
        """ the string human representation of the object """

        return f"[{__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ the Save method to update the updated_at """
        self.updated_at = date.now()
        #storge.save()

    def to_dict(self):
        """ first piece of the serialization/deserialization process"""
        dictt = {
                'my_number': self.my_number,
                'name': self.name,
                '__class__': __class__.__name__,
                'updated_at': self.updated_at.isoformat(),
                'id': self.id,
                'created_at': self.created_at.isoformat(),
                }
        return dictt
