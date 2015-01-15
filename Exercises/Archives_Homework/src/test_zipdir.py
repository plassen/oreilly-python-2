import unittest
import os
import shutil
import zipfile
import zipdir 
import tempfile

class TestZipdir(unittest.TestCase):

    def setUp(self):
        self.path = tempfile.mkdtemp() 
        self.zipdir_filename = os.path.join(self.path, "test_zipdir.zip")
             
    def test_emptydir(self):
        """
        Test with an empty directory
        """

        zipdir.zipdir(self.zipdir_filename, self.path)
        zf = zipfile.ZipFile(self.zipdir_filename, "r")
        files_in_archive = zf.namelist()
        zf.close()
        observed = set([f.replace("\\","/") for f in files_in_archive])
        expected = set([])
        self.assertEqual(observed, expected)
    
    def test_fileandsubdir(self):
        """
        Test with a directory containing files and a subdirectory with files
        """
        self.zip_dir = os.path.basename(self.path)
        self.expected_files = [self.zip_dir+"/a.txt", self.zip_dir+"/b.txt"]
        self.subdir = os.path.join(self.path, "d1")
        self.subdir_files = ["c.txt", "d.txt"]
        
        os.mkdir(self.subdir)
            
        for fn in self.expected_files:
            f = open(os.path.join(self.path, os.path.basename(fn)), "w")
            f.close()
            
        for fn in self.subdir_files:
            f = open(os.path.join(self.subdir, fn), "w")
            f.close()   
            
        zipdir.zipdir(self.zipdir_filename, self.path)
        zf = zipfile.ZipFile(self.zipdir_filename, "r")
        files_in_archive = zf.namelist()
        zf.close()
        observed = set([f.replace("\\","/") for f in files_in_archive])
        expected = set(self.expected_files)
        self.assertEqual(observed, expected)
        
    def tearDown(self):
        try:
            shutil.rmtree(self.path, ignore_errors=True)
        except IOError:
            pass
    
if __name__ == "__main__":
    unittest.main()