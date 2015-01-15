import zipfile
import glob
import os.path

def zipdir(fn, d = "."):
    (upper_dir, base_dir) = os.path.split(d)
    os.chdir(upper_dir) 
    files = glob.glob(base_dir+"/*")  
    zippable_files = []
    for f in files:
        if (os.path.isfile(f)):  
            zippable_files.append(f) 
    zf = zipfile.ZipFile(fn, "w", zipfile.ZIP_DEFLATED)
    for fn_to_archive in zippable_files:
        zf.write(fn_to_archive)
    zf.close()
