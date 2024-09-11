import os
import shutil
from copy_static import copy_files
from generate_page import generate_page

def main():
    if os.path.exists("public"):
        shutil.rmtree("public")
    copy_files("static", "public")
    generate_page("content/index.md", "template.html", "public/index.html")
    

main()