import re
import os
from markdown_to_html import markdown_to_html_node


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