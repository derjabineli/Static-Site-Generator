import os
import shutil
from copy_static import copy_files
from generate_page import generate_pages_recursive

def main():
    if os.path.exists("public"):
        shutil.rmtree("public")
    copy_files("static", "public")
    generate_pages_recursive("content", "template.html", "public")
    

main()