#!/usr/bin/python3
import unittest
from datetime import datetime
from . import BaseModel

class TestBaseModel(unittest.TestCase):

    def test_id_generation(self):
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.id, obj2.id)
    
    def test_created_at_and_updated_at(self):
        obj = BaseModel()
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_save_updates_updated_at(self):
        obj = BaseModel()
        original_updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(original_updated_at, obj.updated_at)

    def test_to_dict(self):
        obj = BaseModel()
        obj_dict = obj.to_dict()

        self.assertIsInstance(obj_dict, dict)
        self.assertIn('__class__', obj_dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertIn('id', obj_dict)
        self.assertEqual(obj_dict['id'], obj.id)
        self.assertIn('created_at', obj_dict)
        self.assertEqual(obj_dict['created_at'], obj.created_at.isoformat())
        self.assertIn('updated_at', obj_dict)
        self.assertEqual(obj_dict['updated_at'], obj.updated_at.isoformat())

if __name__ == '__main__':
    unittest.main()

