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
        self.check_count_and_configure(self.created_configure, self.correct_configure)

    def test_configure_copy_without_dir(self):
        build_path = os.path.join("..", "temp2")
        Configuretor.create_configuration(build_path)

        self.check_count_and_configure(os.listdir(build_path), self.correct_configure)

        shutil.rmtree(build_path)

    def check_count_and_configure(self, created_configure:list, correct_configure:list):
        self.assertEqual(len(created_configure), len(correct_configure), created_configure)
        for created_dir in self.created_configure:
            self.assertTrue(created_dir in correct_configure, created_configure)


    @property
    def created_configure(self):
        return os.listdir(self.BUILD_PATH)

    @property
    def correct_configure(self):
        return os.listdir(Configuretor.TEMPLATES_PATH)


if __name__ == '__main__':
    unittest.main()
