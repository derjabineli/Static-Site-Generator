import re
from blocks import markdown_to_blocks, block_to_block_type
from htmlnode import ParentNode, LeafNode
from markdown_utils import text_to_textnodes

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_children = []
    for block in blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case "heading":
                html_children.append(block_to_heading(block))
            case "unordered_list":
                html_children.append(block_to_ul(block))
            case "ordered_list":
                html_children.append(block_to_ol(block))
            case "code":
                html_children.append(block_to_code(block))
            case "quote":
                html_children.append(block_to_quote(block))
            case "paragraph":
                html_children.append(block_to_paragraph(block))

    html_node = ParentNode("div", html_children)
    return html_node

def text_to_children(text):
    nodes = text_to_textnodes(text)
    children = []
    for node in nodes:
        children.append(node.text_node_to_html_node())
    return children

def block_to_heading(block):
    heading = re.findall(r"^#{1,6} ", block)[0]
    text = block[len(heading):]
    html_children = text_to_children(text)
    return ParentNode(f"h{len(heading)-1}", html_children)
    
def block_to_ul(block):
    children = []
    lines = block.split("\n")
    for line in lines:
        children.append(text_to_li(line[2:]))
    return ParentNode("ul", children)

def block_to_ol(block):
    children = []
    lines = block.split("\n")
    for line in lines:
        children.append(text_to_li(line[3:]))
    return ParentNode("ol", children)

def text_to_li(text):
    children = text_to_children(text)
    return ParentNode("li", children)

def block_to_code(block):
    text = block.split("```")
    inner_text = text[1].strip()
    code_html = LeafNode("code", inner_text)
    return ParentNode("pre", [code_html])

def block_to_quote(block):
    lines = block.split("\n")
    text = ""
    for line in lines:
        text += line[2:]
        text += " "
    text = text.rstrip()
    html_children = text_to_children(text)
    return ParentNode("blockquote", html_children)

def block_to_paragraph(block):
    html_children = text_to_children(block)
    return ParentNode("p", html_children)