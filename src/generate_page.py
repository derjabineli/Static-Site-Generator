import re
import os
from markdown_to_html import markdown_to_html_node

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
     if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)
     directory = os.listdir(dir_path_content)
     for item in directory:
          print(item)
          src_path = os.path.join(dir_path_content, item)
          if os.path.isfile(src_path):
               generate_page(src_path, template_path, os.path.join(dest_dir_path, "index.html"))
               continue
          generate_pages_recursive(src_path, template_path, os.path.join(dest_dir_path, item))
     

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    from_file = open(from_path, "r")
    markdown = from_file.read()
    from_file.close()

    template_file = open(template_path, "r")
    template_content = template_file.read()
    template_file.close()

    html = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)

    template_content = template_content.replace("{{ Title }}", title)
    template_content = template_content.replace("{{ Content }}", html)

    path_name = os.path.dirname(dest_path)
    if not os.path.exists(path_name):
        os.mkdir(path_name) 
    with open(dest_path, 'w') as file: 
            file.write(template_content) 

def extract_title(markdown):
    match = re.search(r"^#\s+(.+)$", markdown, re.MULTILINE)
    if match:
        return match.group(1).strip()
    raise Exception("Markdown must have heading")

generate_page("content/index.md", "template.html", "public/index.html")