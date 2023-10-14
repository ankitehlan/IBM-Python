import unittest as ut

from src.add_program import squarer, doubler
class TestTestDemo(ut.TestCase):
    def test_square(self):
        '''test squarer'''
        self.assertEqual(squarer(2), 4)
    
    def test_doubler(self):
        '''test doubler'''
        self.assertEqual(doubler(2), 4)
    
ut.main()