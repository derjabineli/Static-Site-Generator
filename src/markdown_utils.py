from textnode import TextNode
import re

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        
        text_string = old_node.text
        sections = text_string.split(delimiter)
        if len(sections) % 2 == 0:
            raise Exception("Invalid markdown syntax")
        for i in range (len(sections)):
            current_section = sections[i]
            if current_section == "":
                continue
            if i % 2 == 0:
                node = TextNode(current_section, text_type_text)
            else:
                node = TextNode(current_section, text_type)
            new_nodes.append(node)
    return new_nodes

def extract_markdown_images(text):
    images = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return images

def extract_markdown_links(text):
    links = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)
    return links

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        node_text = old_node.text
        images = extract_markdown_images(node_text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        for image in images:
            sections = node_text.split(f"![{image[0]}]({image[1]})", 1)
            if sections[0] != '':
                new_nodes.append(TextNode(sections[0], text_type_text))
            new_nodes.append(TextNode(image[0], text_type_image, image[1]))
            node_text = sections[1]
        if node_text != '':
            new_nodes.append(TextNode(node_text, text_type_text))
    return new_nodes
        

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        node_text = old_node.text
        links = extract_markdown_links(node_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = node_text.split(f"[{link[0]}]({link[1]})", 1)
            if sections[0] != '':
                new_nodes.append(TextNode(sections[0], text_type_text))
            new_nodes.append(TextNode(link[0], text_type_link, link[1]))
            node_text = sections[1]
        if node_text != '':
            new_nodes.append(TextNode(node_text, text_type_text))
    return new_nodes

def text_to_textnodes(text):
    new_nodes = [TextNode(text, text_type_text)]
    new_nodes = split_nodes_delimiter(new_nodes, "**", text_type_bold)
    new_nodes = split_nodes_delimiter(new_nodes, "*", text_type_italic)
    new_nodes = split_nodes_delimiter(new_nodes, "`", text_type_code)
    new_nodes = split_nodes_image(new_nodes)
    new_nodes = split_nodes_link(new_nodes)
    return new_nodes