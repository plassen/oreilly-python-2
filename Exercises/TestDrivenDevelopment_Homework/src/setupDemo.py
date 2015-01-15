"""
Demonstration of setUp and tearDown
The tests do not actually test anything - this is a demo.
"""

import unittest
import tempfile
import shutil
import glob
import os

class FileTest(unittest.TestCase):
    
    def setUp(self):
        self.origdir = os.getcwd()
        self.dirname = tempfile.mkdtemp("testdir")
        os.chdir(self.dirname)
        
    def test_1(self):
        "Verify creation of files is possible"
        test_files = ['this.txt', 'that.txt', 'th_other.txt']
        
        for filename in test_files:
            f = open(filename, "w")
            f.write("Some text\n")
            f.close()
            self.assertTrue(f.closed)
        dir_files = os.listdir(self.dirname)
        
        for dir_file in dir_files:
            self.assertIn(dir_file, test_files, "Test directory should contain only test files") 
    
    def test_2(self):
        "Verify that the current directory is empty"
        self.assertEqual(glob.glob("*"), [], "Directory not empty")
        
    def test_3(self):
        "Verify creation of a 1,000,000 byte file is possible"
        test_file = "million_dollar_file.txt"
        f = open(test_file, "wb")
        for i in range(1000000):
            f.write(bytes(1))
        f.close()
        stat_info = os.stat(test_file)
        self.assertEqual(stat_info.st_size, 1000000, "The file is a "+str(stat_info.st_size)+" bytes file. Should be 1000000 bytes long")    
        
    def tearDown(self):
        os.chdir(self.origdir)
        shutil.rmtree(self.dirname)
        
if __name__ == "__main__":
    unittest.main()