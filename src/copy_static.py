import os
import shutil

def copy_files(src, dst):
    if not os.path.exists(dst):
        os.mkdir(dst)
    
    directory = os.listdir(src)
    for item in directory:
        src_path = os.path.join(src, item)
        dst_path = os.path.join(dst, item)
        print(f"{src_path} --> {dst_path}")
        if os.path.isfile(src_path):
            shutil.copy(src_path, dst_path)
            continue
        copy_files(src_path, dst_path)