from pathlib import Path
import unittest
from filesystem_api.filesys_functions.info_functions import list_all_with_info, list_detail_with_info
import settings

# musi to byt relativni cesta
# nesmi se dostat do nadslozky


class InfoFunctionsTestCate(unittest.TestCase):


    def test_list_all(self):
        dir_content = list_all_with_info(path=settings.API_ROOT_DIR)
        self.assertTrue('file1' in dir_content)
        self.assertTrue('.filehidden' in dir_content)
        self.assertTrue('dir1' in dir_content)

    def test_list_one(self):
        file_info = list_detail_with_info(path=settings.API_ROOT_DIR.joinpath('file1'))
        self.assertTrue(file_info.get('size') is not None)