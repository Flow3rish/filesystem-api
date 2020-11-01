from pathlib import Path
from src.api.path_functions import path_to_apipath
import unittest
from src.constants import API_ROOT_DIR

# TODO: implement endpoints

class PathFunctionsTestCase(unittest.TestCase):

    def test_basic(self):
        s = path_to_apipath(path= API_ROOT_DIR / 'dir1')