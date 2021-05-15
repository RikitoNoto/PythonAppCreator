import unittest
import shutil
import os
import sys
sys.path.append("..")

from src import Configuretor

class TestConfigure(unittest.TestCase):
    BUILD_PATH = os.path.join("..","temp")

    def setUp(self):
        Configuretor.create_configuration(self.BUILD_PATH)

    def tearDown(self):
        shutil.rmtree(self.BUILD_PATH)
        os.mkdir(self.BUILD_PATH)

    def test_configure_copy(self):
        self.assertEqual(len(self.created_configure), len(self.correct_configure), self.created_configure)
        for created_configure in self.created_configure:
            self.assertTrue(created_configure in self.correct_configure, self.created_configure)

    @property
    def created_configure(self):
        return os.listdir(self.BUILD_PATH)

    @property
    def correct_configure(self):
        return os.listdir(Configuretor.TEMPLATES_PATH)


if __name__ == '__main__':
    unittest.main()
