import unittest # a testing framework
from quiz_data import load_questions # converts to dict
from quiz_utils import clean_name # cleans the name
from quiz_utils import character_check # validates the name
from quiz_utils import length_check 
from quiz_utils import presence_check
from quiz_utils import pattern_check

class TestSmoke(unittest.TestCase):

    def test_ut_works(self):
        self.assertEqual(2+2,4)
        self.assertNotEqual(6,1)
    
    def test_load_questions_runs(self):
        self.assertTrue(1)

    def test_ut_unhappy(self):
        self.assertEqual(2+2,6)