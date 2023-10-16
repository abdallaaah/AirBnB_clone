#!/usr/bin/python3
import unittest
import os
from . import BaseModel
from . import FileStorage


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()
        self.base_model = BaseModel()
        self.base_model.save()
        self.storage.new(self.base_model)
        self.storage.save()

    def tearDown(self):
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_all(self):
        all_objects = self.storage.all()
        self.assertTrue(isinstance(all_objects, dict))
        self.assertIn(f"BaseModel.{self.base_model.id}", all_objects)

    def test_new(self):
        new_model = BaseModel()
        self.storage.new(new_model)
        all_objects = self.storage.all()
        self.assertIn(f"BaseModel.{new_model.id}", all_objects)

    def test_save(self):
        with open("file.json", "r") as file:
            data = file.read()
            self.assertIn(self.base_model.id, data)

    def test_reload(self):
        self.storage.reload()
        all_objects = self.storage.all()
        self.assertTrue(isinstance(all_objects, dict))
        self.assertIn(f"BaseModel.{self.base_model.id}", all_objects)


if __name__ == "__main__":
    unittest.main()
