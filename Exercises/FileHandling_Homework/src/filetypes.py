import os
import glob

def count_filetypes(path = "."):
    """
    Print number of files in provided directory by extension
    """ 
    filetype_counter = {}
    
    files = glob.glob(os.path.join(path, "*"))
    
    for f in files:
        if (os.path.isfile(f)):           
            extension = f.split('.')[-1]
            if (extension in filetype_counter):
                filetype_counter[extension] += 1
            else:
                filetype_counter[extension] = 1
    
    return filetype_counter