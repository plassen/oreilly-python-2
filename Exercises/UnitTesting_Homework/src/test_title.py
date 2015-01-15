"""
Demonstrates the unittest module in action.
"""

import unittest

def title(s):
    "How close is this function to str.title()?"
    return s[0].upper()+s[1:].lower()

class TestTitle(unittest.TestCase):
    
    def test_title(self):
        for test_case in ["hello","Hello","hELLO","HELLO","hElLo"]:
            self.assertEqual(title(test_case), test_case.title(), "Title of "+title(test_case)+" should be "+test_case.title())
       
if __name__ == "__main__":
    unittest.main()