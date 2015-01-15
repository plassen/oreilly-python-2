"""
test what happens when a test fails
"""
import unittest
class TCase(unittest.TestCase):

    def setUp(self):
        print('\nsetUp here')  #don't do this at home - tests should never print

    def test_pass_1(self):
        print('test_pass_1')
        self.assertEqual(1,1)
        
    def test_pass_2(self):
        print('test_pass_2')
        self.assertEqual(1,1)
        
    def test_fail_1(self):
        print('test_fail_1')
        self.assertEqual(1,2)
        
    def test_fail_2(self):
        print('test_fail_2')
        self.assertEqual(1,2)  
        
    def tearDown(self):
        print('tearDown here')

if __name__ == "__main__":
    unittest.main() 