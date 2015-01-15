import unittest
import os
import tempfile
import filetypes

class TestFileTypes(unittest.TestCase):
    """
    Test cases for the filetypes function
    """
    
    def setUp(self):
        self.testdir = tempfile.mkdtemp("testdir")
        os.chdir(self.testdir) 
        
    def test_emptydir(self):
        filetypes.count_filetypes()
        self.assertEqual(filetypes.count_filetypes(), {}, "values not equal")
               
    def test_dirwithfilesandsubdirs(self):
        self.file_names = ["file1.txt", "file1.doc", "file2.doc", "foo.bar.csv"]
        self.subdirs = ["foo.dir", "bar.dir"]
        
        for d in self.subdirs:
            os.mkdir(d)
            
        for fn in self.file_names:
            f = open(fn, "w")
            f.close()  
        self.assertEqual(filetypes.count_filetypes(), {'csv' : 1, 'doc' : 2, 'txt' : 1 }, "values not equal")

    def TearDown(self):
        os.remove(self.testdir)
        
if __name__ == "__main__":
    unittest.main()
        
        
        