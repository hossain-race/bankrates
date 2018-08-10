# author: Mahmud Ahsan
# github: https://github.com/mahmudahsan
# blog: http://thinkdiff.net
# web: http://pythonbangla.com
# license: MIT License
# unit testing

import unittest 

from constants import *
from banks.ibbl import IBBL
from helper import verify_https_issue

class IBBLTestCase(unittest.TestCase):
    def setUp(self):
        verify_https_issue()
        self._ibbl = IBBL(url=BANK_URLS['ibbl'])
        self._ibbl.retrieve_webpage()
    
    def test_retrieve_webpage(self):
        self.assertTrue(len(self._ibbl._data) > 0)

    def test_scrap_webpage_data(self):
        self.assertEqual(1, 0)  

    def test_str(self):
        self.assertEqual(1, 0)  

    def test_create_html_file(self):
        self.assertEqual(1, 0)  

if __name__ == '__main__':
    unittest.main()