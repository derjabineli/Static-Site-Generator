import os
import shutil
from copy_static import copy_files

def main():
    if os.path.exists("public"):
        shutil.rmtree("public")
    copy_files("static", "public")
    

main()