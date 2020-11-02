from pathlib import Path
from filesystem_api.api.path_functions import path_to_apipath
import unittest
import settings

# TODO: implement endpoints

class PathFunctionsTestCase(unittest.TestCase):

    def test_basic(self):
        s = path_to_apipath(path= settings.API_ROOT_DIR / 'dir1')